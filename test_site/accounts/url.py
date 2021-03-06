from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', views.indexView, name='home'),
    path('dashboards/', views.dashboardView, name="dashboard"),
    path('login/', LoginView.as_view(), name="login_url"),
    path('register/', views.registerView, name="register_url"),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('status_info/', views.status_info, name='status_info'),
    path('change_status/', views.change_status, name='change_status'),
    path('account/', views.account, name='personal_account'),
    path('register/validate_username/', views.validate_username,
         name='validate_username'),
    path('ajax_btn/', views.ajax_btn, name='ajax_btn'),
]
