from django.urls import path
from App import views

app_name = 'App'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('reset_pwd/', views.reset_password, name='reset')
]
