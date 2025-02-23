from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product, CartItem
from django.contrib import messages

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})

def product_detail_view(request, pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'marketplace/product_detail.html', {'product': product})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total = item.product.price * item.quantity 
    return render(request, 'marketplace/view_cart.html', {'cart_items': cart_items, 'total_price': total_price})


@csrf_exempt
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if not created:
                cart_item.quantity += quantity
            else:
                cart_item.quantity = quantity
            cart_item.save()
            return JsonResponse({'message': f'{quantity} {product.name}(s) added to your cart.'})
    return JsonResponse({'message': 'Failed to add item to cart.'}, status=400)


@csrf_exempt
def update_cart(request, product_id):
    if request.method == 'POST':
        try:
            action = request.POST.get('action')
            quantity = int(request.POST.get('quantity', 1))
            product_id = int(request.POST.get('product_id'))
            product = Product.objects.get(id=product_id)
            cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
            if action == 'increment':
                cart_item.quantity += 1
            elif action == 'decrement':
                cart_item.quantity -= 1 if cart_item.quantity > 1 else 0
            cart_item.save()
            return redirect('view_cart')
        except Exception as e:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=405)

