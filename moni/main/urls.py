from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.LoanApplicationForm.as_view(), name='index'),
    url(r'^admin/$', views.LoanApplicationAdmin.as_view(), name='admin-list'),
    url(r'^admin/edit/(?P<pk>\d+)/$', views.LoanApplicationAdminEdit.as_view(), name='admin-edit'),
    url(r'^admin/delete/(?P<pk>\d+)/$', views.LoanApplicationAdminDelete.as_view(), name='admin-delete'),
]
