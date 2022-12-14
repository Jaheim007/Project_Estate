from django.urls import path

from Authentication import views

urlpatterns = [
    path('login/' , views.Login.as_view() , name="login"),
    path('register/', views.Register.as_view()  , name="register" ),
    path('logout/' , views.Logout.as_view() , name='logout'),
    path('profile/' , views.Profile.as_view() , name='profile'),
    path('edit_profile/' , views.Edit_Profile.as_view() , name='edit_profile'),
    path('add/' , views.AddProperty.as_view() , name='add'),
    path('password_change/' , views.PasswordChange.as_view() , name='password_change'),
    path('password_reset/', views.PasswordReset.as_view() , name='password_reset'),

    
]