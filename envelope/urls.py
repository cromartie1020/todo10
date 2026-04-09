from django.urls import path
from .views import envelopeForm
urlpatterns=[
    path('',envelopeForm,name='envelope'),
]