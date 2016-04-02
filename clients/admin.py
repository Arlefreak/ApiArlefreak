from django.contrib import admin
from .models import Client, Payment, Phone, Email

class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0

class EmailInline(admin.TabularInline):
    model = Email
    extra = 0

class PhoneInline(admin.TabularInline):
    model = Phone
    extra = 0

class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'dateAdquired'

    list_display = (
        'name',
        'dateAdquired',
        'phone',
        'email',
    )
    list_display_links = (
        'name',
        'dateAdquired',
        'phone',
        'email',
    )
    # list_filter = (
    #     'category',
    #     'publish',
    # )
    inlines = [
        PhoneInline,
        EmailInline,
        PaymentInline
    ]

class PaymentAdmin(admin.ModelAdmin):
    date_hierarchy = 'dateSet'
    list_display = (
        'client',
        'money',
        'dateSet',
        'dateExpiration',
        'status',
    )
    list_display_links = (
        'client',
        'money',
        'dateSet',
        'dateExpiration',
    )
    list_filter = (
        'client',
        'status',
    )
    list_editable = (
        'status',
    )


admin.site.register(Client, ClientAdmin)
admin.site.register(Payment, PaymentAdmin)
