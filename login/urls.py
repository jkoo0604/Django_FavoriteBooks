from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.index), 
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('ajax/validate-reg', views.testunique),
    path('ajax/validate-login', views.testlogin),
]