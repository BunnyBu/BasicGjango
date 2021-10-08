from django.shortcuts import render

def main(request):
    return render(request, 'chairshop/index.html')

def contacts(request):
    return render(request, 'chairshop/contact.html')