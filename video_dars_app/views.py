from django.shortcuts import render
from .models import Card,Test

# Create your views here.
def home(request):
    cards=Card.objects.all()
    # test=Test.objects.create(title="test",batafsil="test batafsil")
    # test.save()
    return render(request, 'index.html', {'cards':cards})

def mavzular(request,title):
    card=Card.objects.get(title=title)
    return render(request, 'mavzular.html', {'card':card})