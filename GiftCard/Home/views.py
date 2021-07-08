from django.shortcuts import render,redirect
from .models import GiftCard,Message
from django.contrib import messages
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
def SingleCard(request,idOfCard):
    context={
        'cardDetails':GiftCard.objects.filter(id=idOfCard)[0]
    }
    return render(request,'card.html',context)    
    
def Contact(request):   
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['number']
        message=request.POST['message']
        singleRow=Message(name=name,phone=phone,message=message,email=email)
        singleRow.save()
        messages.success(request, 'Your Message has been sent')
    else:
        return render(request,"contact.html")
    return render(request,'contact.html')
