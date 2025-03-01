from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Customer, Invoice, InvoiceItem
from django.http import HttpResponse

def generate_invoice_pdf(request):
    return HttpResponse("Invoice PDF generation not implemented yet")

# Debugging message to ensure views.py is loaded
print("Views file is loaded successfully!")

def home(request):
    return render(request, 'billing/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, "billing/product_list.html", {"products": products})

def create_invoice(request):
    customers = Customer.objects.all()
    products = Product.objects.all()
    
    if request.method == "POST":
        customer_id = request.POST.get("customer")
        selected_products = request.POST.getlist("products")
        quantities = request.POST.getlist("quantities")

        # Ensure a customer is selected
        customer = get_object_or_404(Customer, id=customer_id)
        invoice = Invoice.objects.create(customer=customer, total_amount=0)

        total = 0
        for product_id, qty in zip(selected_products, quantities):
            product = get_object_or_404(Product, id=product_id)
            subtotal = int(qty) * product.price
            InvoiceItem.objects.create(invoice=invoice, product=product, quantity=qty, price=product.price)
            total += subtotal

        invoice.total_amount = total
        invoice.save()

        return redirect("invoice_detail", invoice_id=invoice.id)

    return render(request, "billing/create_invoice.html", {"customers": customers, "products": products})

def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    invoice_items = InvoiceItem.objects.filter(invoice=invoice)
    return render(request, "billing/invoice_detail.html", {"invoice": invoice, "invoice_items": invoice_items})
