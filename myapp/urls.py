from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('make_appoint/',views.make_appoint,name='make_appoint'),
    path('verify_otp/',views.verify_otp,name='verify_otp')

]