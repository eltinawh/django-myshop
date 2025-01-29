from django.contrib import admin
from coupons.models import Coupon


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        "code",
        "valid_from",
        "valid_to",
        "discount",
        "active"
    ]
    list_filte = ["active", "valid_from", "valid_to"]
    search_fields = ["code"]