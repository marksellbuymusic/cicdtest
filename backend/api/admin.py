from django.contrib import admin
from .models import CtMusic


# Register your models here.
# @admin.register(ApiAccount)
# class AccountAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "is_manager"]
#     search_fields = ["user__username__icontains"]

admin.site.register(CtMusic)
