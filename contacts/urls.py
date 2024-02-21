from django.urls import path
from .views import (ContactListView, ContactDetailView, 
                    ContactCreateView, ContactUpdateView,
                    ContactDeleteView)


app_name = 'contacts'
urlpatterns = [
    path('', ContactListView.as_view(), name='index'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact'),
    path('create/', ContactCreateView.as_view(), name='create'),
    path('contact/<int:pk>/update', ContactUpdateView.as_view(), name='contact-update'),
    path('contact/<int:pk>/delete', ContactDeleteView.as_view(), name='contact-delete'),
]
