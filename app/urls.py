from django.urls import path
from .views import *

urlpatterns = [
    path("", homepage, name=""),
    path("home/", homepage, name="home"),
    path("about/", aboutpage, name="about"),
    path("service/", servicepage, name="service"),
    path("contact/", contactpage, name="contact"),
    path("register/", registerpage, name="register"),
    path("login/", loginpage, name="login"),
    path("logout/", logoutpage, name="logout"),
    path("registerdata/", registerdatapage, name="registerdata"),
    path("logindata/", logindatapage, name="logindata"),
    path("dash/", dashpage, name="dash"),
    path("querydata/", querydatapage, name="querydata"),
    path("shawtabledatabtn/", shawtabledatabtnpage, name="shawtabledatabtn"),
    path("EditDeleteData/", EditDeleteDatapage, name="EditDeleteData"),
]
