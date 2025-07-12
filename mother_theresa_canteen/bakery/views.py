from django.shortcuts import render, get_object_or_404
from .models import BakeryModel


def b_product_list(request):
    ob_products = BakeryModel.objects.all()
    return render(request, 'b_product_list.html', {'b_products': ob_products})

def b_product_detail(request, pk):
    ob_product = get_object_or_404(BakeryModel, pk=pk)
    return render(request, 'b_product_detail.html', {'b_product': ob_product})
