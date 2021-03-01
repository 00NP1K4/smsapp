from django.contrib import messages
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .sendsms import sendsms

@login_required(login_url = 'login')
def index(request):
    context = {
    }
    return render(request, 'dashboard.html', context)

def add(request):
    count = 0
    contacts = Contact.objects.all()
    tos = To.objects.all()
    form = ToForm()
    if request.method == 'POST':
        form = ToForm(request.POST or none)
        if form.is_valid():
            form.save()
            return redirect('/add-to-send')
    for i in tos:
        count += 1
    
    m = [i.number for i in tos]
    
    if len(tos) == 0:
        check = False   
    else: check = True

    context = {
        'form' : form,
        'tos' : tos,
        'count' : count,
        'contacts' : contacts,
        'm' : m,
        'check' : check
    }
    return render(request, 'smscontact.html', context)

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Username or Password is incorrect!")

    context = {
    }
    return render(request, 'signin.html', context)

def logoutuser(request):

    logout(request)
    
    return redirect('login')

def contacts(request):
    contacts = Contact.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(contacts, 10)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    context = {
        "contacts": contacts,
    }
    return render(request, 'contacts.html', context)

def text_message(request):
    count = 0
    tos = To.objects.all()
    if request.method == 'POST':
        message = request.POST.get('message')
        for i in tos:
            num = "+234" +  i.number[1:]
            #print(num)
            try:
                message = sendsms(message, num)
                messages.add_message(request, messages.SUCCESS, f'Message was sent successfully! ({message} | {num})')
            except:
                messages.add_message(request, messages.ERROR, f'Message not sent! ({num})')
                redirect('confirm')
        
        for i in tos:
            i.delete()

        return redirect('confirm')

    for i in tos:
        count += 1
    

    context = {
        'tos' : tos,
        'count' : count,
    }
    return render(request, "text.html", context)

def add_contact(request):
    
    form = AddContactForm()
    if request.method == 'POST':
        form = AddContactForm(request.POST or none)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact created Successfully!'.upper())
            return redirect('/contacts')
    context = {
        'form':form
    }
    return render(request, 'add.html', context)

def delete_contact(request,pk):
    queryset = Contact.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        messages.success(request, f'Contact "{queryset.name}" Deleted Successfully!'.upper())
        return redirect('/contacts')
    context = {
        'queryset':queryset
    }
    return render(request, 'delete.html', context)

def update_contact(request,pk):
    queryset = Contact.objects.get(id=pk)
    form = ContactUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = ContactUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, f'Contact "{queryset.name}" Successfully Updated!'.upper())
            return redirect('/contacts')
    context = {
        'form':form
    }
    return render(request, 'add.html', context)

def from_contact(request,pk):
    queryset = Contact.objects.get(id=pk)
    i = To(number=queryset.number)
    i.save()
    return redirect('/add-to-send')

def delete_send(request,pk):
    queryset = To.objects.get(id=pk)
    queryset.delete()
    return redirect('/add-to-send')

def confirm(request):

    context = {
    }
    
    return render(request, 'confirm.html', context)