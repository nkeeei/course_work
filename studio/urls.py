from django.urls import path
from .views import home, equipment, engineer, event, register, user_login, user_logout, schedule, studiodate, \
    delete_session, change_session, service, print_pdf, user_sessions, print_user_pdf

urlpatterns = [
    path('',home,name='home'),
    path('equipment',equipment,name='equipment'),
    path('engineer',engineer,name='engineer'),
    path('event',event,name='event'),
    path('service',service,name='service'),
    path('schedule/<str:date>',schedule,name='schedule'),
    path('studiodate',studiodate,name='studiodate'),
    path('register', register, name='register'),
    path('logout', user_logout, name='logout'),
    path('login', user_login, name='login'),
    path('delete/<int:pk>',delete_session,name='delete_session'),
    path('change/<int:pk>',change_session,name='change_session'),
    path('print/<str:date>',print_pdf,name = 'print_pdf'),
    path('user_sessions/<int:id>',user_sessions,name = 'user_sessions'),
    path('print_user_pdf/<int:id>',print_user_pdf,name = 'print_user_pdf'),
]
