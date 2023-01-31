from django.shortcuts import render, redirect
from .models import Product
from .scraper_views import scrape_product

def product_form(request):
    if request.method == "POST":
        url = request.POST["url"]
        title, description, price = scrape_product(url)
        product = Product.objects.create(
            url=url,
            title=title,
            description=description,
            price=price,
        )
        
    return render(request, "product_form.html")

def product_detail(request):
    product = Product.objects.get()
    return render(request, "product_detail.html", {"product": product})


