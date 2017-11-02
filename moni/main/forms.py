from django.forms import ModelForm
from .models import LoanApplication


class LoanApplicationForm(ModelForm):
    class Meta:
        model = LoanApplication
        exclude = ['approved', 'error']
