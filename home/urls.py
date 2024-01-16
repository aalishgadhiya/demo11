from django.urls import path
from home import views
urlpatterns = [
    path("",views.index,name = "home"),
    path("aboutus",views.about_us,name="aboutUs"),
    path("contectus",views.contect_us,name="contectus")
]
