from django.http import HttpResponse

# Create your views here.

def default(request):
    return HttpResponse({"<h2> My E-Commerce site </h2>"})