from django.urls import path
from .views import ContactListView, ContactDetailView


app_name = 'contacts'
urlpatterns = [
    path('', ContactListView.as_view(), name='index'),
    path('contact/<int:pk>', ContactDetailView.as_view(), name='contact'),
]
