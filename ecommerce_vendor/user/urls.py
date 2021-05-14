from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="userindex"),
    path("register/", views.register, name="userregister"),
    path("login/", views.login, name="userlogin"),
    path("logout/", views.logout, name="userlogout"),


    path("product_detail/", views.product_detail, name="product_detail"),
    # path("password_reset_email/", views.password_reset_email, name="password_reset_email"),

    # path("user_password_reset/", views.password_reset, name="user_password_reset_user"),


    path('user_password_reset/',auth_views.UserPasswordResetView.as_view(template_name='registration/password_reset.html'),name='user_password_reset_user'),
    path('user_password_reset/done/',auth_views.UserPasswordResetDoneView.as_view(template_name='registration/user_password_reset_done.html'),name='user_password_reset_done'),
    path('user_reset/<uidb64>/<token>/',auth_views.UserPasswordResetConfirmView.as_view(template_name='registration/user_password_reset_confirm.html'),name='user_password_reset_confirm'),
    path('user_reset/done/',auth_views.UserPasswordResetCompleteView.as_view(template_name='registration/user_password_reset_complete.html'),name='user_password_reset_complete'),
    # path('reset_password', ResetPasswordRequestView.as_view(), name="reset_password"),
]	
