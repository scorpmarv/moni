from django.conf.urls import include, url
from django.contrib.auth.views import LoginView
from main.views import LogoutView

urlpatterns = [
    url(r'^', include('main.urls')),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/logout/$', LogoutView.as_view(), name='logout'),
]
