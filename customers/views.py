from urllib import request
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm

# Create your views here.
def create(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('read')
    return render(request,'customers/create_form.html',{'form': form})

def read(request):
    customers= Customer.objects.all()
    return render (request, 'customers/customers.html',{'customers':customers})

def update(request, id):
    customer=Customer.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance = customer)
    if form.is_valid() and request.POST:
       form.save()
       return redirect('read') 
    return render(request, 'customers/edit_form.html',{'form':form})

def delete(request,id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect('read')