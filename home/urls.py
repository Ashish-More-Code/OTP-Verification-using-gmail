from django.urls import path
from home.views import *

urlpatterns = [
    path('', home),
    path('register/',register),
    path('logout/',signout),
    path('checkotp/<int:id>/',checkOtp),
    path('dashboard/', dashbord)
]   