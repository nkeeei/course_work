

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone

from studio.models import StudioSession


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Имя пользователя',help_text='Введите корректное имя пользователя' , widget=forms.TextInput(
        attrs={'class':'form-control'}))

    email = forms.CharField(label='E-mail',widget=forms.EmailInput(
                                   attrs={'class': 'form-control'}))

    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,12}$',message="format: '+999999999'. Up to 12 digits allowed.")
    last_name = forms.CharField(validators=[phone_regex], max_length=17, label='Номер телефона',widget=forms.TextInput(
        attrs={'class':'form-control'}))

    password1 = forms.CharField(label='Пароль',widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    password2 = forms.CharField(label='Подтверждение пароля',widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username','email','last_name','password1','password2')



class StudioSessionDateForm(forms.Form):
    cur_year = timezone.now().year
    year_range = tuple([i for i in range(cur_year, cur_year + 1)])
    date = forms.DateField(label='Выбери дату',
                           widget=forms.SelectDateWidget(years=year_range,attrs={'class': 'form-control'}),
                           initial=timezone.now(),error_messages={'required': ''})


class StudioSessionForm(forms.ModelForm):
    time_choices = [('10', '10:00'),
                    ('11', '11:00'),
                    ('12', '12:00'),
                    ('13', '13:00'),
                    ('14', '14:00'),
                    ('15', '15:00'),
                    ('16', '16:00'),
                    ('17', '17:00'),
                    ('18', '18:00'),
                    ('19', '19:00'),
                    ('20', '20:00'),
                    ('21', '21:00'),
                    ('22', '22:00'),
                    ('23', '23:00'),
                    ('24', '24:00'),
                    ]

   #cur_year = timezone.now().year
    #cur_day = timezone.now().day
    #cur_month = timezone.now().month
    cur_time = timezone.now().hour
    #year_range = tuple([i for i in range(cur_year, cur_year + 1)])
    #month_range = tuple([z for z in range(cur_month, cur_month + 2)])
    #days_range = tuple([j for j in range(cur_day,cur_day + 8)])

    #name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    time = forms.ChoiceField(label='Выбери время',choices=time_choices,initial=cur_time,error_messages={'required': ''})
    count_hours = forms.CharField(label='Впиши кол-во часов', max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = StudioSession
        fields = ('time', 'count_hours')

    def save(self, user,date,studio):
        obj = super(StudioSessionForm, self).save(commit=False)
        obj.user = user
        obj.date = date
        obj.studio = studio
        return obj.save()