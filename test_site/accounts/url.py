from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import change_status



urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboards/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView,name="register_url"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('status_info/', views.status_info, name='status_info'),
    path('change_status/', views.change_status, name = 'change_status')
]