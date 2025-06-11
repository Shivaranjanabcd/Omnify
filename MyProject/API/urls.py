from django.urls import path
from APP.views import *
urlpatterns = [
   path("class/",Class_view.as_view(), name="class"),
   path("show/",Show.as_view(), name="show"),
]
