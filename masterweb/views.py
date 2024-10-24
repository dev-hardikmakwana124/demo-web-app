from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>This is first page as Home..</h1>")