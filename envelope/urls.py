# -*- coding: utf-8 -*-

from django.urls import path

from envelope.views import ContactView


urlpatterns = [
    path('', ContactView.as_view(), name='envelope-contact'),
]
