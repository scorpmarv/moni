# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import requests
from django.contrib.auth import logout
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import LoanApplication
from .forms import LoanApplicationForm


class BaseLoanApplicationView(PermissionRequiredMixin):
    success_url = reverse_lazy('admin-list')
    model = LoanApplication
    permission_required = 'is_staff'


class LoanApplicationAdmin(BaseLoanApplicationView, ListView):
    paginate_by = 10


class LoanApplicationAdminEdit(BaseLoanApplicationView, UpdateView):
    fields = '__all__'


class LoanApplicationAdminDelete(BaseLoanApplicationView, DeleteView):
    pass


class LoanApplicationForm(CreateView):
    template_name = 'main/index.html'
    form_class = LoanApplicationForm

    def form_valid(self, form):
        moni_api_url = 'http://scoringservice.moni.com.ar:7001/api/v1/scoring/'
        response = requests.get(moni_api_url, form.cleaned_data)
        if response.ok:
            params = response.json()
        else:
            params = {'approved': False, 'error': True}

        approved, error = params['approved'], params['error']
        form.instance.approved = approved
        form.instance.error = error
        self.object = form.save()

        success = False
        if approved and not error:
            success = True
            msg = 'Su solicitud ha sido aprobada.'
        elif error:
            msg = 'Hubo un error al procesar su solicitud.'
        else:
            msg = 'Su solicitud ha sido rechazada.'

        context = {
            'msg': msg,
            'success': success,
            'form': form
        }
        return self.render_to_response(self.get_context_data(**context))


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('index'))
