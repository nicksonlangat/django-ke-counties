from django.contrib import admin

from .models import County, SubCounty, Ward

# Register your models here.


class CountyAdmin(admin.ModelAdmin):
    """
    County admin page
    """

    search_fields = ("name",)


class SubCountyAdmin(admin.ModelAdmin):
    """
    Sub county admin page
    """

    search_fields = (
        "name",
        "county__name",
    )
    list_filter = ("created_at", "updated_at", "county__name")
    list_display = ("id", "name", "county", "created_at", "updated_at")


class WardAdmin(admin.ModelAdmin):
    """
    Ward admin page
    """

    search_fields = ("name", "sub_county__name", "sub_county__county__name")
    list_filter = (
        "created_at",
        "updated_at",
        "sub_county__name",
        "sub_county__county__name",
    )
    list_display = ("id", "name", "sub_county", "created_at", "updated_at")


admin.site.register(County, CountyAdmin)
admin.site.register(SubCounty, SubCountyAdmin)
admin.site.register(Ward, WardAdmin)
