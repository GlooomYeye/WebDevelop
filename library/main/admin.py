from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
         if request.user.is_superuser:
            return True
         return False
    def has_add_permission(self, request):
         if request.user.is_authenticated:
            return True
         return True

admin.site.register(Book)

# Register your models here.
