from django.urls import path

from . import views

urlpatterns = [
    path("counties", views.CountyApi.as_view(), name="counties"),
    path("sub-counties", views.SubCountyApi.as_view(), name="sub-counties"),
    path("wards", views.WardApi.as_view(), name="wards"),
]
