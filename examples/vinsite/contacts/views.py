from django.shortcuts import HttpResponse, render

# Create your views here.
# def index(request):
#     return HttpResponse('<h1>This is the contacts app homepage</h1>')

def index(request):
    context = {}
    context['title'] = 'This is another test!'
    # return HttpResponse(render(request, 'contacts/index.html', context))
    return render(request, 'contacts/index.html', context)

def view_all(request):
    return HttpResponse('<h1>This is where you will find all contacts</h1>')