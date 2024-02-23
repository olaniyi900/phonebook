from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import PersonContact
from django.urls import reverse_lazy


# api import

from rest_framework import viewsets
from .serializers import PersonContactSerializer

class PersonContactViewset(viewsets.ModelViewSet):
    queryset = PersonContact.objects.all()
    serializer_class = PersonContactSerializer
    

class ContactListView(ListView):
    model = PersonContact
    context_object_name = "contacts"
    template_name = 'contacts/index.html'
    paginate_by = 20


class ContactDetailView(DetailView):
    model = PersonContact
    context_object_name = "contact"
    template_name = "contacts/deatail.html"

class ContactCreateView(CreateView):
    model = PersonContact
    template_name = 'contacts/form.html'
    fields = '__all__'

class ContactUpdateView(UpdateView):
    model = PersonContact
    template_name = 'contacts/form.html'
    fields = '__all__'


class ContactDeleteView(DeleteView):
    model = PersonContact
    context_object_name = "contact"
    template_name = 'contacts/delete.html'
    success_url = reverse_lazy('contacts:index')