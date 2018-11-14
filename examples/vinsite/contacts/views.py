from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>This is the contacts app homepage</h1>')

def view_all(request):
    return HttpResponse('<h1>This is where you will find all contacts</h1>')