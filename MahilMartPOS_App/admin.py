from django.contrib import admin
from .models import Category, Supplier
from django.contrib import admin
from .models import Customer,ComputerAlias
from .models import Billing
from django.contrib import admin
from .models import Company, CompanyActivity

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'email')
    search_fields = ('name', 'contact_person')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'cell', 'email', 'date_joined')
    search_fields = ('name', 'cell', 'email')

admin.site.register(ComputerAlias)




@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'short_name', 'created_at')


@admin.register(CompanyActivity)
class CompanyActivityAdmin(admin.ModelAdmin):
    list_display = ('company', 'action', 'user', 'created_at')
    list_filter = ('company', 'created_at')
    search_fields = ('action', 'user__username')
