from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about(request):
    response_str = "This is the about page" + "<a href='/rango'>Rango</a>"
    return HttpResponse(response_str)
