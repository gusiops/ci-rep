from django.shortcuts import render

def index_page(request):
    return render(request, 'index.html')
def vlad_page(request):
    return render(request, 'index2.html')