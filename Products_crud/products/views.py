from django.shortcuts import render,redirect,get_object_or_404
from .forms import ProductForm
from django.contrib import messages
from .models import Product

# Create your views here.

def products_list(request):
    products = Product.objects.all()
    return render(request,'products_list.html',{'products':products})

def products_create(request):
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'product added successful!')
            return redirect('products_list')
        
    return render(request,'products_create.html',{'form': form})

def products_update(request,pk):
    product = get_object_or_404(Product,pk=pk)
    form= ProductForm(instance=product)

    # context = {
    #     "form" : ProductForm(instance=product)
    # }
    
    if request.method == "POST":
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
        else:
            form = ProductForm(instance=product)
    return render(request,'products_create.html',{'form':form})

def products_delete(request,pk):
    product = get_object_or_404(Product,pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect('products_list')
    return render(request,'product_confirm_delete.html',{'product':product})