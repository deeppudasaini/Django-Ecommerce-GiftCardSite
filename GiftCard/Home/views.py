from django.shortcuts import render,redirect
from .models import GiftCard
# Create your views here.
def Index(request):
    
    return redirect('/index')
def Home(request):
    some=GiftCard.objects.all()[:5]
    latest=GiftCard.objects.last()
    context={
        'some':some,
        'latest':latest,
    }
    return render(request,'index.html',context)
def Card(request):
    some=GiftCard.objects.all()[:5]
    latest=GiftCard.objects.last()
    context={
        'some':some,
        'latest':latest,
        'all':GiftCard.objects.all()
    }
    return render(request,'watches.html',context)
def About(request):
    return render(request,'about.html')
def Contact(request):
    return render(request,'contact.html')
