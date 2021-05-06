from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login,logout
from .models import *
from .forms import UserRegisterForm, UserLoginForm, StudioSessionForm, StudioSessionDateForm
from django.contrib.auth import login,logout
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from fpdf import FPDF


def home(request):
    studio_image = StudioImage.objects.all()[0]
    studio = Studio.objects.get(id=1)
    engineer = SoundEngineer.objects.all()[0]
    services = Service.objects.all()
    return render(request,'home.html',{'engineer':engineer, 'studio_image':studio_image, 'studio': studio,'services':services})


def equipment(request):
    equipments = Equipment.objects.exclude(pk=4)
    studio = Studio.objects.get(id=1)
    return render(request,'equipment.html',{'equipment': equipments,'studio': studio})


def engineer(request):
    engineer1 = SoundEngineer.objects.all()[0]
    engineer2 = SoundEngineer.objects.all()[1]
    studio = Studio.objects.get(id=1)
    return render(request,'engineer.html',{'engineer1': engineer1, 'engineer2':engineer2,'studio': studio})


def event(request):
    events = Event.objects.all()[0]
    studio = Studio.objects.get(id=1)
    return render(request,'event.html',{'events': events,'studio': studio})


def service(request):
    services = Service.objects.all()[0:4]
    studio = Studio.objects.get(id=1)
    return render(request,'service.html',{'services':services,'studio':studio})

def register(request):
    studio = Studio.objects.get(id=1)
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request,'register.html',{'form':form,'studio': studio})


def user_login(request):
    studio = Studio.objects.get(id=1)
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = UserLoginForm()
    else:
        form = UserLoginForm()
    return render(request,'login.html',{'form':form,'studio': studio})


def user_logout(request):
    logout(request)
    return redirect('home')


def studiodate(request):
    if request.method == 'GET':
        form = StudioSessionDateForm(request.GET)
        if form.is_valid():
            date = form.cleaned_data['date']
            print(date)
            return redirect('schedule', date=date)
    else:
        form = StudioSessionDateForm()


    studio = Studio.objects.get(id=1)
    return render(request, 'schedule_start.html', {'form': form, 'studio': studio})



@login_required
def schedule(request,date):
    studio = Studio.objects.get(id=1)

    sessions = StudioSession.objects.filter(date=date)
    if request.method == 'POST':
        form = StudioSessionForm(request.POST)
        if form.is_valid():
            form.save(request.user,date=date,studio=studio)

            addr_from = "korobyko@bk.ru"  # Адресат
            addr_to = "korobyko@bk.ru"  # Получатель
            password = "Workaut03012001"  # Пароль

            msg = MIMEMultipart()  # Создаем сообщение
            msg['From'] = addr_from  # Адресат
            msg['To'] = addr_to  # Получатель
            msg['Subject'] = 'Новая заявка на студию: "' + str(studio.name)+'"'     # Тема сообщения

            user_username = request.user.username
            user_lastname = request.user.last_name
            user_email = request.user.email


            body = 'НОВАЯ ЗАЯВКА !\n'+"Дата: " + str(date) + "\nВремя: от " + str(form.cleaned_data['time'])+ ":00 до "+ str(int(form.cleaned_data['time']) + int(form.cleaned_data['count_hours'])) + ":00\nКол-во часов: " + str(form.cleaned_data['count_hours']) + "\nПользователь: " + str(user_username) +"\n" + str(user_lastname) +"\n" +  str(user_email)
            msg.attach(MIMEText(body, 'CHECKIT'))  # Добавляем в сообщение текст

            server = smtplib.SMTP('smtp.mail.ru', 587)  # Создаем объект SMTP
            #server.set_debuglevel(True)  # Включаем режим отладки - если отчет не нужен, строку можно закомментировать
            server.starttls()  # Начинаем шифрованный обмен по TLS
            server.login(addr_from, password)  # Получаем доступ
            server.send_message(msg)  # Отправляем сообщение
            server.quit()  # Выходим

            return redirect('schedule', date=date)
    else:
        form = StudioSessionForm()


    return render(request, 'schedule.html', {'form': form, 'studio': studio, 'sessions':sessions,'date':date})


def delete_session(request,pk):
    session = StudioSession.objects.get(pk=pk)
    date = session.date
    session.delete()
    return redirect('schedule', date=date)


def change_session(request,pk):
    session = StudioSession.objects.get(pk=pk)
    date = session.date
    if session.is_active == False:
        session.is_active=True
    else:
        session.is_active=False
    session.save()
    return redirect('schedule', date=date)


def print_pdf(requset,date):
    sessions = StudioSession.objects.filter(date=date, is_active=True)
    document = FPDF()
    document.add_page()

    array = []
    for session in sessions:
        dos = int(session.time) + int(session.count_hours)
        line = 'USER: ' + str(session.user) + "\n"+"TIME: from " + str(session.time) + ':00 \nto ' + str(dos) + ":00 " + "COUNT OF HOURS: " + str(session.count_hours) +'\n\n\n'
        array.append(line)
    document.set_font('Arial', 'B', 15)
    document.cell(40, 10, 'DATE: ' + str(date),0,  1)
    document.set_font('helvetica', size=12)
    for el in array:
        document.cell(40, 10, el, 0, 1)
    document.output("{}.pdf".format(date))
    return redirect('schedule', date=date)


def user_sessions(request,id):
    sessions = StudioSession.objects.filter(user_id=id)
    studio = Studio.objects.get(id=1)
    return render(request,'sessions.html',{'sessions':sessions,'studio':studio})


def print_user_pdf(requset,id):
    sessions = StudioSession.objects.filter(user_id=id)
    document = FPDF()
    document.add_page()
    array = []
    for session in sessions:
        dos = int(session.time) + int(session.count_hours)
        if session.is_active:
            status='confirmed'
        else:
            status='under consideration'
        line = 'STUDIO: "'+str(session.studio.name)+'" DATE: ' + str(session.date) + 'USER: ' + str(session.user) + "\n" + " From " + str(
            session.time) + ':00 \nTo ' + str(
            dos) + ":00 " +'| ' + str(status)  +'\n\n\n'
        array.append(line)
    document.set_font('Arial', 'B', 15)
    document.set_font('helvetica', size=12)
    for el in array:
        document.cell(50, 15, el, 2, 1)
    document.output("{}.pdf".format(sessions[0].user.username))
    return redirect('user_sessions', id=id)
