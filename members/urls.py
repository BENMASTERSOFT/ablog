from django.urls import path
from . views import UserRegisterView, UserEditView, PasswordsChangeView, Password_success
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('register/', UserRegisterView.as_view(), name="register"),
   path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
   # path('password/', auth_views.PasswordsChangeView.as_view(template_name='registration/change-password.html')),
   path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password_change'),
   path('password_success', Password_success,name='password_success'),

  ]
