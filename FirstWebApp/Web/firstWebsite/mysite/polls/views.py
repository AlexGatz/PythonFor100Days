from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, my name Juan! Welcome to polls, where the strippers play.")
    