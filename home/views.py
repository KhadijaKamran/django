from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        'Name': 'Khadija'
    }
    return render(request, 'index.html', context)

def workexperience(request):
    return render(request, 'workexperience.html')

    #return HttpResponse("this is Khadija's Work Experience")

def documents(request):
    return render(request, 'documents.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        contact = Contact(name=name, description=desc)
        contact.save()
    return render(request, 'contact.html')
