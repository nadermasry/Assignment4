from django.urls import path
from .views import home, createcontact, delete_contact, edit_contact

urlpatterns = [
 path('createcontact/', createcontact , name='createcontact'),
 path('', home),
 path('delete_contact/<int:pk>/', delete_contact, name='delete_contact'),
 path('edit/<int:pk>/', edit_contact, name='edit'),
]
