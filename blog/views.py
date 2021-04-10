from django.http import HttpResponse

def about(request):
    return HttpResponse("This is About Page")

def home(request):
    return HttpResponse("This is Home Page")