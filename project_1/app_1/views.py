from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def main_view(request):
    return render(request,'app_1/index.html')
def main_contact(request):
    return render(request,'app_1/contact.html')
def main_menu(request):
    return render(request,'app_1/index.html')
def main_mon(request):
    return render(request,'app_1/monday.html')
def main_tue(request):
    return render(request,'app_1/tuesday.html')
def main_wed(request):
    return render(request,'app_1/wednesday.html')
def main_thur(request):
    return render(request,'app_1/thursday.html')
def main_fri(request):
    return render(request,'app_1/friday.html')
def main_sat(request):
    return render(request,'app_1/saturday.html')
def main_sun(request):
    return render(request,'app_1/sunday.html')

