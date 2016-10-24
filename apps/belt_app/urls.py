from django.conf.urls import url, include
# from django.contrib import admin
from .import views
urlpatterns = [
    url(r'^$',views.index,name="index"),

    url(r'^register$',views.register,name="register"),
    url(r'^login$',views.login,name="login"),
    url(r'^show$',views.show,name="show"),
    # url(r'^add$',views.add,name="add"),
    url(r'^addtrip$',views.addtrip,name="addtrip"),
    url(r'^join/(?P<id>\d+)$',views.join,name="join"),
    url(r'^logout$',views.logout,name="logout"),
    url(r'^goback$',views.goback,name="goback"),
    url(r'^destination/(?P<id>\d+)$',views.destination,name="destination"),
]
