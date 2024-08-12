from django.urls import path
from .views import create_contact, contact_list, delete_contact

urlpatterns = [
    path('contacts/', create_contact, name='contact-create'),
    path('contact-list/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', delete_contact, name='contact-delete'),
]
