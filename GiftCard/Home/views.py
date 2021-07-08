from django.shortcuts import render,redirect
from .models import GiftCard,Message
from django.contrib import messages
import stripe,os
from flask import Flask, redirect

app = Flask(__name__)
stripe.api_key = "sk_test_51JB2UKC0eOISt08XgpA2p6kl0YRhJf1XuFMK1RQCgCwBiEopmL9KmpoIFzYJ28EzvkOQDjzldyTUSF4o8WTVwIhe0044FoXQQd"
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
def Checkout(request):
    session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=[{
      'price_data': {
        'currency': 'usd',
        'product_data': {
          'name': 'T-shirt',
        },
        'unit_amount': 2000,
      },
      'quantity': 1,
    }],
    mode='payment',
    success_url='https://127.0.0.1/index',
    cancel_url='https://127.0.0.1/contact',
  )

    return render(request,'card.html')
