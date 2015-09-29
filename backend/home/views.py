from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request,'home/index.html', {'nombre':'Brenda'})

def info(request):
    return render(request,'home/info.html', {'nombre':'luis'})
