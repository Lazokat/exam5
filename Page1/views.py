from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'Page1/home.html')

@login_required
def create_view(request):
    if request.method=="POST":
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/list/')

    else:
        form=PostForm()
        return render(request,'Page1/create_view.html',{'form':form})

def viewss(request):
    context={}
    context['dataset']=Products.objects.all()
    return render(request,'Page1/list_view.html',context)
@login_required
def delete_view(request,id):
    object=get_object_or_404(Products,id=id)
    if request.method=="POST":
        object.delete()
        return redirect('/list/')
    context={}
    return render(request,'Page1/delete.html',context)
@login_required
def update_view(request,id):
    obj=get_object_or_404(Products,id=id)
    form=PostForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/list/')
    context={}
    context["form"]=form
    return render(request,'Page1/update.html',context)

@login_required
def add_to_cart(request,product_id):
    try:
        cart_item = Cart.objects.get(user=request.user, id=product_id)
        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            messages.success(request, "Item added to your cart.")
    except:
        Cart.objects.create(user=request.user, id=product_id)
        messages.success(request, "Item added to your cart.")
    return redirect("cart_detail")
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id)
    if cart_item.user == request.user:
        cart_item.delete()
        messages.success(request, "Item removed from your cart.")
    return redirect("cart_detail")
@login_required
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = [item.quantity * item.product.price for item in cart_items]
    sum2=sum(total_price)

    context = {
        "cart_items": cart_items,
        "sum":sum2
    }

    return render(request, "Page1/cart_detail.html", context)
@login_required
def product_detail(request,product_id):
    product = Products.objects.filter(id=product_id)

    if request.method == "POST":
        messages.success(request, f"{product.name} added to your cart.")
        return redirect("add_to_cart", id=product_id)

    context = {
        "products": product,
    }
    return render(request,'Page1/product_detail.html',context)