from django.urls import path
from .views import ContactListView, ContactDetailView, ContactCreateView


app_name = 'contacts'
urlpatterns = [
    path('', ContactListView.as_view(), name='index'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact'),
    path('create/', ContactCreateView.as_view(), name='create'),
]
