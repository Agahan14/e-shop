from django.urls import path

from .views import *


urlpatterns = [
    path("carts", CartView.as_view()),
    path("carts/<int:pk>", CartDetailView.as_view()),
    path("cart-item", CartItemView.as_view()),
    path("cart-item/<int:pk>", CartItemDetailView.as_view()),
    path("orders", OrderView.as_view()),
    path("orders/<int:pk>", OrderDetailView.as_view()),
]