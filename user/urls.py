from django.urls import path
from django.contrib.auth import views as auth_views


from .import views

urlpatterns = [
    
    path('register/',views.register, name='blog-register'),
    # path('about/',views.about, name='blog-about'),
    path('',auth_views.LoginView.as_view(template_name='user/login.html'), name='blog-login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='user/logout.html'), name='blog-logout'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='user/password_reset.html'), name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='password_reset_complete'),

    
    path('profile/',views.profile, name='blog-profile')



]