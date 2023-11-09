
from django.urls import path
from . import views

urlpatterns = [
    path("vendors/", views.VendorList.as_view()),
    path("vendor/<int:pk>/", views.VendorDetail.as_view()),

    #Products
    path("products/", views.ProductList.as_view()),
    path("product/<int:pk>/", views.ProductDetail.as_view()),

    #Cusomer
    path("customers/", views.CusomerList.as_view()),
    path("customer/<int:pk>/", views.CustomerDetail.as_view()),
]
