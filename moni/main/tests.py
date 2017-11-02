# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client, TestCase
from django.urls import reverse
from .forms import LoanApplicationForm


class MyTests(TestCase):
    def setUp(self):
        self.c = Client()

    def test_ok_data_forms(self):
        form_data = {
            'document_number': 1111111,
            'name': 'Test',
            'surname': 'Test',
            'gender': 'M',
            'email': 'test@test.com',
            'amount': 100
        }
        form = LoanApplicationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_bad_document_number_forms(self):
        form_data = {
            'document_number': 'pepe',
            'name': 'Test',
            'surname': 'Test',
            'gender': 'M',
            'email': 'test@test.com',
            'amount': 100
        }
        form = LoanApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_bad_email_forms(self):
        form_data = {
            'document_number': 1111111,
            'name': 'Test',
            'surname': 'Test',
            'gender': 'M',
            'email': 'test@test',
            'amount': 100
        }
        form = LoanApplicationForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_loan_application_form(self):
        form_data = {
            'document_number': 1111111,
            'name': 'Test',
            'surname': 'Test',
            'gender': 'M',
            'email': 'test@test.com',
            'amount': 100
        }
        response = self.c.post(reverse('index'), form_data)
        self.assertEqual(response.status_code, 200)
