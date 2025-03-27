from django.urls import path
from.views import home
from.views import signin
from.views import signup
from.views import Signout
from.views import destination
from.views import about
from.views import cultures
urlpatterns = [
path("" , home,name="home"),
path("signin" , signin ,name="signin"),
path("signup" , signup , name="signup"),
path("Signout" , Signout , name="Signout"),
  path("destination" , destination ,name="destination"),
  path("about" , about ,name="about"),
  path("cultures" , cultures , name="cultures") , 
  
]
