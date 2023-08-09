from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return render(request,'app_1/index.html')
def main_contact(request):
    return render(request,'app_1/contact.html')
def main_menu(request):
    return render(request,'app_1/index.html')
