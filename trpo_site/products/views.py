from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


class ProductWorker:
    @classmethod
    def product_list(cls, request):
        products = Product.objects.all()

        # Обработка фильтрации
        name = request.GET.get('name')
        category = request.GET.get('category')
        min_price = request.GET.get('min_price')
        max_price = request.GET.get('max_price')
        min_quantity = request.GET.get('min_quantity')
        max_quantity = request.GET.get('max_quantity')
        incoming_date = request.GET.get('incoming_date')

        if name:
            products = products.filter(name__icontains=name)
        if category:
            products = products.filter(category__icontains=category)
        if min_price:
            products = products.filter(price__gte=min_price)
        if max_price:
            products = products.filter(price__lte=max_price)
        if min_quantity:
            products = products.filter(quantity__gte=min_quantity)
        if max_quantity:
            products = products.filter(quantity__lte=max_quantity)
        if incoming_date:
            products = products.filter(incoming_date__date=incoming_date)

        return render(request, 'products/product_list.html', {'products': products})

    @classmethod
    def product_add(cls, request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('product_list')
        else:
            form = ProductForm()
        return render(request, 'products/product_form.html', {'form': form})

    @classmethod
    def product_edit(cls, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            form = ProductForm(request.POST, instance=product)
            if form.is_valid():
                form.save()
                return redirect('product_list')
        else:
            form = ProductForm(instance=product)
        return render(request, 'products/product_form.html', {'form': form})

    @classmethod
    def product_delete(cls, request, pk):
        product = get_object_or_404(Product, pk=pk)
        if request.method == 'POST':
            product.delete()
            return redirect('product_list')
        return render(request, 'products/product_confirm_delete.html', {'product': product})
