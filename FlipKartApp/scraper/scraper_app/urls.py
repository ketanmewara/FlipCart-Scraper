from django.urls import path
from . import views


app_name = "products"

urlpatterns = [
    path("", views.product_form, name="product_form"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
]
