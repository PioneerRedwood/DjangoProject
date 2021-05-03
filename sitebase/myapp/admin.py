from django.contrib import admin
from .models import Brand, Headquarter, StoreAddress, Population


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


class StoreAddressAdmin(admin.ModelAdmin):
    list_display = ('sector', 'brand_name', 'do', 'sigu', 'dong', 'longitude', 'latitude')
    list_filter = ['brand_name']
    search_fields = ['brand_name']


class PopulationAdmin(admin.ModelAdmin):
    list_display = ('do', 'sigu', 'dong', 'population')
    list_filter = ['sigu']
    search_fields = ['do']


admin.site.register(Brand, BrandAdmin)
admin.site.register(Headquarter, HeadquarterAdmin)
admin.site.register(StoreAddress, StoreAddressAdmin)
admin.site.register(Population, PopulationAdmin)
