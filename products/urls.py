from django.urls import path

from .views import *


urlpatterns = [
    path("product", ProductView.as_view()),
    path("product/<int:pk>", ProductDetailView.as_view()),
    path("productcategory", ProductCategoryView.as_view()),
    path("productcategory/<int:pk>", ProductCategoryDetailView.as_view()),
    path("comment", CommentView.as_view()),
    path("comment/<int:pk>", CommentDetailView.as_view())
]