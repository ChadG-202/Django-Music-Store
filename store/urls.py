from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('contact/', views.contact, name='contact'),
    path('checkout/', views.checkout, name='checkout'),
    path('send_request/', views.sendRequest, name="send_request"),
]