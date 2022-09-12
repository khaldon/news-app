from django.urls import path, reverse_lazy
from .views import SignupView 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', SignupView.as_view(), name="signup"),
    # path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name="login"),
    # path('logout/', auth_views.LogoutView.as_view()),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change_form.html')),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html')),
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_forms.html', success_url=reverse_lazy('password_reset_done')), name="password_reset"),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_dones.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= 'registration/password_reset_confirms.html')),
    # path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html")),


]


