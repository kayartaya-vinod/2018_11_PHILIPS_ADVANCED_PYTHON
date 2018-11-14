from django.shortcuts import HttpResponse, render, redirect
from .models import Contact

# Create your views here.
def index(request):
    context = {}
    context['title'] = 'Welcome to Contacts App'
    context['developed_by'] = 'Vinod'
    return render(request, 'contacts/home.html', context)

def view_all(request):

    data = Contact.objects.all()

    context = {}
    context['contacts'] = data
    return render(request, 'contacts/view-all.html', context)

def view_details(request, id):
    data = Contact.objects.get(pk=id)
    context = {}
    context['contact'] = data
    return render(request, 'contacts/details.html', context)

def contact_form(request):
    return render(request, 'contacts/contact-form.html')

def save_contact(request):
    c1 = Contact()
    c1.name = request.POST['name']
    c1.email = request.POST['email']
    c1.phone = request.POST['phone']
    c1.city = request.POST['city']
    c1.picture = request.POST['picture']

    c1.save()
    # return view_all(request)
    return redirect('view_all') # clientside redirection