from django.urls import path
from .views import home, product_list, create_invoice, invoice_detail
from .views import generate_invoice_pdf

urlpatterns = [
    path("", home, name="home"),
    path("products/", product_list, name="product_list"),
    path("invoice/create/", create_invoice, name="create_invoice"),
    path("invoice/<int:invoice_id>/", invoice_detail, name="invoice_detail"),
    path('invoice/<int:invoice_id>/pdf/', generate_invoice_pdf, name='invoice_pdf'),

]





