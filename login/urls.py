from django.urls import path,include
from django.contrib import admin 
from login import views as login_views
from django.contrib.auth import views as auth_views



app_name = 'login'  # here for namespacing of urls.

urlpatterns = [
	path("admin/",admin.site.urls),
    path("login/home/", login_views.home, name="home"), #here the link may seem wierd but its to help use django inbouilt home thiing see setting.py LOGIn_redirect_url
    path("profile/", login_views.profile, name="profile"),
    path("register/",login_views.register, name="register"),
    path("login/",auth_views.LoginView.as_view(template_name="login/login.html"),name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name="login/logout.html"),name='logout'),
    path("webhook",login_views.webhook,name="webhook"),


    # path("logout", views.logout_request, name="logout"),
    # path("login", views.login_request, name="login"),
]