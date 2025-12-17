from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello, World!</h1><p>My Django project is officially alive.</p>")
