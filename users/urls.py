from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import (


 	UserRegistrationView,
    UserProfileView,
    Userslistview,
#    UserDetailView,
 #   UpdateUserView,

	 )

urlpatterns = [    

  

   
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = "users/reset_password.html"), name ='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = "users/password_reset_sent.html"), name ='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = "users/password_reset_form.html"), name ='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "users/password_reset_done.html"), name ='password_reset_complete'),


    path('register_user/',UserRegistrationView.as_view(),name='register-user'),

    path('users/',Userslistview.as_view(),name="users"),
    path('profile/<int:pk>',UserProfileView.as_view(),name="user-profile"), 
    path('users/profile_edit/<int:pk>/',views.profile_edit,name="user-profile-edit"), 
    path('users/admin_user_update/<int:pk>/',views.admin_userprofile_update,name="admin-user-profile-update"),
     




 
#   
#   
#    path('users/adduser/',views.adduser,name="add-user"),
#    path('userdetail/<int:pk>/',UserDetailView.as_view(),name="user-detail"),
#    
#    # path('user_account/',UserAccountListView.as_view(),name='user-account')


  
   
  
]

