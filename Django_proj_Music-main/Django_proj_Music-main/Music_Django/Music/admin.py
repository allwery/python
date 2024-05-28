from django.contrib import admin


from .models import Buyer, Place, Concert, Buying


class BuyerModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    list_display_links = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'last_name', 'email']

    class Meta:
        model = Buyer


class ConcertModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_concert', 'place', 'singer']
    list_display_links = ['name', 'singer']
    list_filter = ['name', 'date_concert', 'place', 'singer']
    search_fields = ['name', 'date_concert', 'place', 'singer']
    list_editable = ['date_concert', 'place']

    class Meta:
        model = Concert


class PlaceModelAdmin(admin.ModelAdmin):
    list_display = ['place', 'cost']
    list_display_links = ['place']
    search_fields = ['place__id']
    list_editable = ['cost']
    class Meta:
        model = Place


class BuyingModelAdmin(admin.ModelAdmin):
    list_display = ['buy_date', 'concert', 'buyer', 'place']
    list_display_links = ['buy_date', 'concert', 'buyer']
    list_filter = ['buy_date', 'concert', 'buyer']
    search_fields = ['buy_date', 'concert', 'buyer', 'place']

    class Meta:
        model = Buying


admin.site.register(Buyer, BuyerModelAdmin)
admin.site.register(Concert, ConcertModelAdmin)
admin.site.register(Place, PlaceModelAdmin)
admin.site.register(Buying, BuyingModelAdmin)