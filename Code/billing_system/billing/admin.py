from django.contrib import admin
from .models import Invoice

# Check if Invoice is already registered
if admin.site.is_registered(Invoice):
    admin.site.unregister(Invoice)  # Unregister first

# Now register Invoice safely
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at")  # Adjust fields as needed

admin.site.register(Invoice, InvoiceAdmin)
