from django.urls import path
from profiles import views

urlpatterns = [
    path('<str:user_name>/', views.profileHome, name='profileHome'),
    path('<str:user_name>/sms', views.sms, name='sms'),

]
