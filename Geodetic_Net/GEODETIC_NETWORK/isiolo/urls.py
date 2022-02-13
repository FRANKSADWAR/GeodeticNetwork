from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from isiolo import views

admin.site.site_header = "ISIOLO GEODETIC CONTROLS Portal"
admin.site.site_title = "ISIOLO GEODETIC CONTROLS Admin Portal"
admin.site.index_title = "ISIOLO GEODETIC CONTROL App"


urlpatterns = [

    ## AUTHENTICATION URLS-------
    path('',views.home_page,name='home'),

    path('login/',views.login_view,name='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('deactivated/',views.deactivate,name='deactivated'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/',views.register,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),

    path('reporting/',views.ReportTemplate.as_view(),name='reporting'),
    path('towns/',views.towns_data,name='towns'),
    path('isiolo/',views.isiolo, name='isiolo'),
    path('geodetic_controls/',views.geodetic_con,name='geodetic_controls'),
]