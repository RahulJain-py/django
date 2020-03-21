from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to personal website of Rahul Jain.")

def hello(request):
    return HttpResponse("Hello")