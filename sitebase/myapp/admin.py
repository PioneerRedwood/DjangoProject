from django.contrib import admin
from .models import Brand, Headquarter


# class BrandInline(admin.StackedInline):
#     model = Brand
#     extra = 3


class BrandAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {
    #         'fields': ('brand_name', 'sector', 'mutual')
    #     }),
    #     ('Advanced options', {
    #         'fields': ('sector',),
    #         'classes': ('collapse',)
    #     }),
    # ]
    # inlines = [BrandInline]
    list_display = ('brand_name', 'sector', 'mutual')
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class HeadquarterAdmin(admin.ModelAdmin):
    list_display = ('mutual', 'address')
    list_filter = ['mutual']
    search_fields = ['mutual']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Headquarter, HeadquarterAdmin)
