from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("role", views.RoleDetail, name="roledetail"),
    path("roleadd", views.RoleAdd, name="roleadd"),
    path("roleupdate/<int:role_id>", views.RoleUpdate, name="roleupdate"),
    path("roledelete/<int:role_id>", views.RoleDelete, name="roledelete"),

    path("localization/country", views.CountryDetail, name="countrydetail"),
    path("localization/countryadd", views.CountryAdd, name="countryadd"),
    path("localization/countryupdate/<int:country_id>", views.CountryUpdate, name="countryupdate"),
    path("localization/countrydelete/<int:country_id>", views.CountryDelete, name="countrydelete"),

    path("localization/zone", views.ZoneDetail, name="zonedetail"),
    path("localization/zoneadd", views.ZoneAdd, name="zoneadd"),
    path("localization/zoneupdate/<int:zone_id>", views.ZoneUpdate, name="zoneupdate"),
    path("localization/zonedelete/<int:zone_id>", views.ZoneDelete, name="zonedelete"),

    path("localization/deliverylocation", views.DeliveryLocationDetail, name="deliverylocationdetail"),
    path("localization/deliverylocationadd", views.DeliveryLocationAdd, name="deliverylocationadd"),
    path("localization/deliverylocationupdate/<int:deliverylocation_id>", views.DeliveryLocationUpdate, name="deliverylocationupdate"),
    path("localization/deliverylocationdelete/<int:deliverylocation_id>", views.DeliveryLocationDelete, name="deliverylocationdelete"),

    path("localization/language", views.LanguageDetail, name="languagedetail"),
    path("localization/languageadd", views.LanguageAdd, name="languageadd"),
    path("localization/languageupdate/<int:language_id>", views.LanguageUpdate, name="languageupdate"),
    path("localization/languagedelete/<int:language_id>", views.LanguageDelete, name="languagedelete"),

    path("localization/currency", views.CurrencyDetail, name="currencydetail"),  
    path("localization/currencyadd", views.CurrencyAdd, name="currencyadd"),  
    path("localization/currencyupdate/<int:currency_id>", views.CurrencyUpdate, name="currencyupdate"),  
    path("localization/currencydelete/<int:currency_id>", views.CurrencyDelete, name="currencydelete"), 

    path("localization/tax", views.TaxDetail, name="taxdetail"), 
    path("localization/taxadd", views.TaxAdd, name="taxadd"), 
    path("localization/taxupdate/<int:tax_id>", views.TaxUpdate, name="taxupdate"), 
    path("localization/taxdelete/<int:tax_id>", views.TaxDelete, name="taxdelete"), 

    path("localization/orderstatus", views.OrderStatusDetail, name="orderstatusdetail"), 
    path("localization/orderstatusadd", views.OrderStatusAdd, name="orderstatusadd"), 
    path("localization/orderstatusupdate/<int:orderstatus_id>", views.OrderStatusUpdate, name="orderstatusupdate"), 
    path("localization/orderstatusdelete/<int:orderstatus_id>", views.OrderStatusdelete, name="orderstatusdelete"),

    path("localization/stockstatus", views.StockStatusDetail, name="stockstatusdetail"), 
    path("localization/stockstatusadd", views.StockStatusAdd, name="stockstatusadd"), 
    path("localization/stockstatusupdate/<int:stockstatus_id>", views.StockStatusUpdate, name="stockstatusupdate"), 
    path("localization/stockstatusdelete/<int:stockstatus_id>", views.StockStatusDelete, name="stockstatusdelete"), 

    path("localization/emailtemplate", views.EmailTemplateDetail, name="emailtemplatedetail"), 
    path("localization/emailtemplateadd", views.EmailTemplateAdd, name="emailtemplateadd"), 
    path("localization/emailtemplateupdate/<int:emailtemplate_id>", views.EmailTemplateUpdate, name="emailtemplateupdate"), 
    path("localization/emailtemplatedelete/<int:emailtemplate_id>", views.EmailTemplateDelete, name="emailtemplatedelete"), 

    path("generalsetting", views.GeneralSettingdetail, name="generalsetting"), 
    path("generalsettingupdate/<int:generalsetting_id>", views.GeneralSettingUpdate, name="generalsettingupdate"), 
    path("homepagesettingupdate/<int:homepage_id>", views.HomePageSettingUpdate, name="homepagesettingupdate"), 

    path("sitesetting", views.SiteSetting, name="sitesetting"), 
    path("varientadd", views.VarientAdd, name="varientadd"), 
    path("varientupdate/<int:varient_id>", views.VarientUpdate, name="varientupdate"), 
    path("varientdelete/<int:varient_id>", views.VarientDelete, name="varientdelete"),

    path("seoupdate/<int:seo_id>", views.SeoUpdate, name="seoupdate"), 
    path("socialupdate/<int:social_id>", views.SocialUpdate, name="socialupdate"), 
]
