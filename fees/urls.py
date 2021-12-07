from django.urls import path
from . import views

urlpatterns = [
    path('feesone', views.feesone),
    path('feestwo', views.feestwo),
]