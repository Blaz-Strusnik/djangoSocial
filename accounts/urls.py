from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^signup/$', views.SignUpView.as_view(), name='signup'),
]