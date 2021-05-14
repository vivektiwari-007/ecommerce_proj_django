from django.urls import path
from django.conf.urls import include, url
from myapp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('dashboard', views.index, name="index"),
    path('register', views.register, name="register"),
    path('', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    
    path('adminuserprofile', views.UserProfile, name="userprofile"),
    path('updateprofileview/<int:user_id>', views.UpdateProfileView, name="updateprofileview"),
    

    path('adminuser', views.UserDetail, name="userdetail"),
    path('adminuseradd', views.UserAdd, name="useradd"),
    path('adminduserupdate/<int:user_id>', views.UserUpdate, name="userupdate"),
    path('adminduserelete/<int:user_id>', views.UserDelete, name="userdelete"),


    path('adminusergroupadd', views.UserGroupAdd, name="usergroupadd"),
    path('adminusergroup', views.UserGroupDetail, name="usergroupdetail"),
    path('adminusergroupupdate/<int:group_id>', views.UserGroupUpdate, name="usergroupupdate"),
    path('adminusergroupdelete/<int:group_id>', views.UserGroupDelete, name="usergroupdelete"),

    path('permissionadd/<int:user_id>', views.PermissionAdd, name="permissionadd"),
    

    path('changepassword', views.ChangePassword, name="changepassword"),

    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='admin/registration/password_reset_form.html'),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='admin/registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='admin/registration/password_reset_confirm.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='admin/registration/password_reset_complete.html'),name='password_reset_complete'),
]
