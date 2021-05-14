from django.contrib import admin
from .models import Role, Country, Zone, DeliveryLocation, Language, Currency, Tax, OrderStatus, StockStatus, EmailTemplate, HomePage, GeneralSetting, Varient, Seo, Social

# Register your models here.
admin.site.register(Role)
admin.site.register(Country)
admin.site.register(Zone)
admin.site.register(DeliveryLocation)
admin.site.register(Language)
admin.site.register(Currency)
admin.site.register(Tax)
admin.site.register(OrderStatus)
admin.site.register(StockStatus)
admin.site.register(EmailTemplate)
admin.site.register(HomePage)
admin.site.register(GeneralSetting)
admin.site.register(Varient)
admin.site.register(Seo)
admin.site.register(Social)