from django.contrib import admin

from hotels.models import City, Hotel


# Register your models here.

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    pass

