from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import PersonContact

# Create your views here.
# def index(request):
#     return render(request, 'contacts/index.html')

class ContactListView(ListView):
    model = PersonContact
    context_object_name = "contacts"
    template_name = 'contacts/index.html'
    paginate_by = 20


class ContactDetailView(DetailView):
    model = PersonContact
    context_object_name = "contact"
    template_name = "contacts/deatail.html"