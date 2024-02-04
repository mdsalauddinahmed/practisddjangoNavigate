from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse('this is Home page')
def about(request):
    return HttpResponse('this is about page')
def portfolio(request):
    return HttpResponse('this is portfolio page')