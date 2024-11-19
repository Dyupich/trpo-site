from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm


class ProductWorker:
    @classmethod
    def product_list(cls, request):
        products = Product.objects.all()
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
