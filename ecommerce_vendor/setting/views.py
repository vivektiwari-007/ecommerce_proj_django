from django.shortcuts import render, redirect
from .models import Role, Country, Zone, DeliveryLocation, Language, Currency, Tax, OrderStatus, StockStatus, EmailTemplate, HomePage, GeneralSetting, Varient, Seo, Social

# Create your views here.
def index(request):
    return render(request, 'setting/index.html')


def RoleDetail(request):
    role = Role.objects.all()
    count1 = Role.objects.filter(is_active=True).count()
    count2 = Role.objects.filter(is_active=False).count()
    return render(request, 'setting/roledetail.html', {'role':role, 'count1':count1, 'count2':count2})


def RoleAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        role = Role(name=name, is_active=is_active,created_by=created_by, modified_by=modified_by)
        role.save()
        return redirect(RoleDetail)
    return render(request, 'setting/roleadd.html')


def RoleUpdate(request, role_id):
    role = Role.objects.get(role_id=role_id)
    if request.method == "POST":
        name = request.POST.get('name')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = role.created_date
        role = Role(role_id=role_id, name=name, is_active=is_active,created_by=created_by, modified_by=modified_by, created_date=created_date)
        role.save()
        return redirect(RoleDetail)
    return render(request, 'setting/roleadd.html', {'role':role})


def RoleDelete(request, role_id):
    role = Role.objects.get(role_id=role_id)
    role.delete()
    return redirect(RoleDetail)


def CountryDetail(request):
    country = Country.objects.all()
    count1 = Country.objects.filter(is_active=True).count()
    count2 = Country.objects.filter(is_active=False).count()
    return render(request, 'setting/countrydetail.html', {'country':country, 'count1':count1, 'count2':count2})


def CountryAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        iso_code_1 = request.POST.get('iso_code_1')
        iso_code_2 = request.POST.get('iso_code_2')
        postal_code_required = request.POST.get('postal_code_required')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        country = Country(name=name, iso_code_1=iso_code_1, iso_code_2=iso_code_2, postal_code_required=postal_code_required, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by)
        country.save()
        return redirect(CountryDetail)
    return render(request, 'setting/countryadd.html')


def CountryUpdate(request, country_id):
    country = Country.objects.get(country_id=country_id)
    if request.method == "POST":
        name = request.POST.get('name')
        iso_code_1 = request.POST.get('iso_code_1')
        iso_code_2 = request.POST.get('iso_code_2')
        postal_code_required = request.POST.get('postal_code_required')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = country.created_date
        country = Country(country_id=country_id, name=name, iso_code_1=iso_code_1, iso_code_2=iso_code_2, postal_code_required=postal_code_required, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by, created_date=created_date)
        country.save()
        return redirect(CountryDetail)
    return render(request, 'setting/countryadd.html', {'country':country})


def CountryDelete(request, country_id):
    country = Country.objects.get(country_id=country_id)
    country.delete()
    return redirect(CountryDetail)


def ZoneDetail(request):
    zone = Zone.objects.all()
    count1 = Zone.objects.filter(is_active=True).count()
    count2 = Zone.objects.filter(is_active=False).count()
    return render(request, 'setting/zonedetail.html', {'zone':zone,'count1':count1,'count2':count2})


def ZoneAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        country_id = request.POST.get('country_id')
        country = Country.objects.get(pk=country_id)
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        zone = Zone(name=name, code=code, country_id=country, is_active=is_active, created_by=created_by, modified_by=modified_by)
        zone.save()
        return redirect(ZoneDetail)
    country = Country.objects.all()
    return render(request, 'setting/zoneadd.html', {'country':country})


def ZoneUpdate(request, zone_id):
    zone = Zone.objects.get(zone_id=zone_id)
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        country_id = request.POST.get('country_id')
        country = Country.objects.get(pk=country_id)
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = zone.created_date
        zone = Zone(zone_id=zone_id, name=name, code=code, country_id=country, is_active=is_active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        zone.save()
        return redirect(ZoneDetail)
    country = Country.objects.all()
    return render(request, 'setting/zoneadd.html', {'country':country, 'zone':zone})


def ZoneDelete(request, zone_id):
    zone = Zone.objects.get(zone_id=zone_id)
    zone.delete()
    return redirect(ZoneDetail)


def DeliveryLocationDetail(request):
    deliverylocation = DeliveryLocation.objects.all()
    count1 = DeliveryLocation.objects.filter(is_active=True).count()
    count2 = DeliveryLocation.objects.filter(is_active=False).count()
    return render(request, 'setting/deliverylocationdetail.html', {'deliverylocation':deliverylocation,'count1':count1,'count2':count2})


def DeliveryLocationAdd(request):
    if request.method == "POST":
        delivery_location = request.POST.get('delivery_location')
        pincode = request.POST.get('pincode')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        deliverylocation = DeliveryLocation(delivery_location=delivery_location, pincode=pincode, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by)
        deliverylocation.save()
        return redirect(DeliveryLocationDetail)
    return render(request, 'setting/deliverylocationadd.html')


def DeliveryLocationUpdate(request, deliverylocation_id):
    delivery = DeliveryLocation.objects.get(deliverylocation_id=deliverylocation_id)
    if request.method == "POST":
        delivery_location = request.POST.get('delivery_location')
        pincode = request.POST.get('pincode')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = delivery.created_date
        deliverylocation = DeliveryLocation(deliverylocation_id=deliverylocation_id, delivery_location=delivery_location, pincode=pincode, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by, created_date=created_date)
        deliverylocation.save()
        return redirect(DeliveryLocationDetail)
    return render(request, 'setting/deliverylocationadd.html', {'delivery':delivery})


def DeliveryLocationDelete(request, deliverylocation_id):
    delivery = DeliveryLocation.objects.get(deliverylocation_id=deliverylocation_id)
    delivery.delete()
    return redirect(DeliveryLocationDetail)


def LanguageDetail(request):
    language = Language.objects.all()
    count1 = Language.objects.filter(is_active=True).count()
    count2 = Language.objects.filter(is_active=False).count()
    return render(request, 'setting/languagedetail.html', {'language':language,'count1':count1,'count2':count2})


def LanguageAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        sort_order = request.POST.get('sort_order')
        image = request.FILES['image']
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        language = Language(name=name, code=code, sort_order=sort_order, image=image, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by)
        language.save()
        return redirect(LanguageDetail)
    return render(request, 'setting/languageadd.html')


def LanguageUpdate(request, language_id):
    language = Language.objects.get(language_id=language_id)
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        sort_order = request.POST.get('sort_order')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = language.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = language.image
        language = Language(language_id=language_id, name=name, code=code, sort_order=sort_order, image=image, is_active=is_active, 
                            created_by=created_by, modified_by=modified_by, created_date=created_date)
        language.save()
        return redirect(LanguageDetail)
    return render(request, 'setting/languageadd.html', {'language':language})


def LanguageDelete(request, language_id):
    language = Language.objects.get(language_id=language_id)
    language.delete()
    return redirect(LanguageDetail)


def CurrencyDetail(request):
    currency = Currency.objects.all()
    count1 = Currency.objects.filter(is_active=True).count()
    count2 = Currency.objects.filter(is_active=False).count()
    return render(request, 'setting/currencydetail.html', {'currency':currency,'count1':count1,'count2':count2})


def CurrencyAdd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        code = request.POST.get('code')
        symbol_left = request.POST.get('symbol_left')
        symbol_right = request.POST.get('symbol_right')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        currency = Currency(title=title, code=code, symbol_left=symbol_left, symbol_right=symbol_right, is_active=is_active, created_by=created_by, modified_by=modified_by)
        currency.save()
        return redirect(CurrencyDetail)
    return render(request, 'setting/currencyadd.html')


def CurrencyUpdate(request, currency_id):
    currency = Currency.objects.get(currency_id=currency_id)
    if request.method == "POST":
        title = request.POST.get('title')
        code = request.POST.get('code')
        symbol_left = request.POST.get('symbol_left')
        symbol_right = request.POST.get('symbol_right')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = currency.created_date
        currency = Currency(currency_id=currency_id, title=title, code=code, symbol_left=symbol_left, symbol_right=symbol_right, is_active=is_active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        currency.save()
        return redirect(CurrencyDetail)
    return render(request, 'setting/currencyadd.html', {'currency':currency})


def CurrencyDelete(request, currency_id):
    currency = Currency.objects.get(currency_id=currency_id)
    currency.delete()
    return redirect(CurrencyDetail)


def TaxDetail(request):
    tax = Tax.objects.all()
    count1 = Tax.objects.filter(is_active=True).count()
    count2 = Tax.objects.filter(is_active=False).count()
    return render(request, 'setting/taxdetail.html', {'tax':tax,'count1':count1,'count2':count2})


def TaxAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        value = request.POST.get('value')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        tax = Tax(name=name, value=value, is_active=is_active, created_by=created_by, modified_by=modified_by)
        tax.save()
        return redirect(TaxDetail)
    return render(request, 'setting/taxadd.html')


def TaxUpdate(request, tax_id):
    tax = Tax.objects.get(tax_id=tax_id)
    if request.method == "POST":
        name = request.POST.get('name')
        value = request.POST.get('value')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = tax.created_date
        tax = Tax(tax_id=tax_id, name=name, value=value, is_active=is_active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        tax.save()
        return redirect(TaxDetail)
    return render(request, 'setting/taxadd.html', {'tax':tax})


def TaxDelete(request, tax_id):
    tax = Tax.objects.get(tax_id=tax_id)
    tax.delete()
    return redirect(TaxDetail)


def OrderStatusDetail(request):
    orderstatus = OrderStatus.objects.all()
    count1 = OrderStatus.objects.filter(is_active=True).count()
    count2 = OrderStatus.objects.filter(is_active=False).count()
    return render(request, 'setting/orderstatusdetail.html', {'orderstatus':orderstatus,'count1':count1,'count2':count2})


def OrderStatusAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        select_color = request.POST.get('select_color')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        orderstatus = OrderStatus(name=name, priority=priority, select_color=select_color, is_active=is_active, 
                               created_by=created_by, modified_by=modified_by)
        orderstatus.save()
        return redirect(OrderStatusDetail)
    return render(request, 'setting/orderstatusadd.html')


def OrderStatusUpdate(request, orderstatus_id):
    orderstatus = OrderStatus.objects.get(orderstatus_id=orderstatus_id)
    if request.method == "POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        select_color = request.POST.get('select_color')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = orderstatus.created_date
        orderstatus = OrderStatus(orderstatus_id=orderstatus_id, name=name, priority=priority, select_color=select_color, is_active=is_active, 
                               created_by=created_by, modified_by=modified_by, created_date=created_date)
        orderstatus.save()
        return redirect(OrderStatusDetail)
    return render(request, 'setting/orderstatusadd.html', {'orderstatus':orderstatus})


def OrderStatusdelete(request, orderstatus_id):
    orderstatus = OrderStatus.objects.get(orderstatus_id=orderstatus_id)
    orderstatus.delete()
    return redirect(OrderStatusDetail)


def StockStatusDetail(request):
    stockstatus = StockStatus.objects.all()
    count1 = StockStatus.objects.filter(is_active=True).count()
    count2 = StockStatus.objects.filter(is_active=False).count()
    return render(request, 'setting/stockstatusdetail.html', {'stockstatus':stockstatus,'count1':count1,'count2':count2})


def StockStatusAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        stockstatus = StockStatus(name=name, is_active=is_active, created_by=created_by, modified_by=modified_by)
        stockstatus.save()
        return redirect(StockStatusDetail)
    return render(request, 'setting/stockstatusadd.html')


def StockStatusUpdate(request, stockstatus_id):
    stockstatus = StockStatus.objects.get(stockstatus_id=stockstatus_id)
    if request.method == "POST":
        name = request.POST.get('name')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = stockstatus.created_date
        stockstatus = StockStatus(stockstatus_id=stockstatus_id, name=name, is_active=is_active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        stockstatus.save()
        return redirect(StockStatusDetail)
    return render(request, 'setting/stockstatusadd.html', {'stockstatus':stockstatus})


def StockStatusDelete(request, stockstatus_id):
    stockstatus = StockStatus.objects.get(stockstatus_id=stockstatus_id)
    stockstatus.delete()
    return redirect(StockStatusDetail)


def EmailTemplateDetail(request):
    emailtemplate = EmailTemplate.objects.all()
    count1 = EmailTemplate.objects.filter(is_active=True).count()
    count2 = EmailTemplate.objects.filter(is_active=False).count()
    return render(request, 'setting/emailtemplatedetail.html', {'emailtemplate':emailtemplate,'count1':count1,'count2':count2})


def EmailTemplateAdd(request):
    if request.method == "POST":
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        emailtemplate = EmailTemplate(title=title, subject=subject, content=content, is_active=is_active, created_by=created_by, modified_by=modified_by)
        emailtemplate.save()
        return redirect(EmailTemplateDetail)
    return render(request, 'setting/emailtemplateadd.html')


def EmailTemplateUpdate(request, emailtemplate_id):
    emailtemplate = EmailTemplate.objects.get(emailtemplate_id=emailtemplate_id)
    if request.method == "POST":
        title = request.POST.get('title')
        subject = request.POST.get('subject')
        content = request.POST.get('content')
        is_active = request.POST.get('is_active')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = emailtemplate.created_date
        emailtemplate = EmailTemplate(emailtemplate_id=emailtemplate_id, title=title, subject=subject, content=content, is_active=is_active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        emailtemplate.save()
        return redirect(EmailTemplateDetail)
    return render(request, 'setting/emailtemplateadd.html', {'emailtemplate':emailtemplate})


def EmailTemplateDelete(request, emailtemplate_id):
    emailtemplate = EmailTemplate.objects.get(emailtemplate_id=emailtemplate_id)
    emailtemplate.delete()
    return redirect(EmailTemplateDetail)


def GeneralSettingdetail(request):
    general = GeneralSetting.objects.all()
    homepage = HomePage.objects.all()
    contry = Country.objects.all()
    zone = Zone.objects.all()
    language = Language.objects.all()
    currency = Currency.objects.all()
    return render(request, 'setting/generalsetting.html', {'general':general,'homepage':homepage, 'contry':contry, 'zone':zone, 'language':language, 'currency':currency})


def GeneralSettingUpdate(request, generalsetting_id):
    generalsetting = GeneralSetting.objects.get(generalsetting_id=generalsetting_id)
    if request.method == "POST":
        name = request.POST.get('name')
        owner_name = request.POST.get('owner_name')
        store_address = request.POST.get('store_address')
        country_id = request.POST.get('country_id')
        country = Country.objects.get(pk=country_id)
        zone_id = request.POST.get('zone_id')
        zone = Zone.objects.get(pk=zone_id)
        language_id = request.POST.get('language_id')
        language = Language.objects.get(pk=language_id)
        currency_id = request.POST.get('currency_id')
        currency = Currency.objects.get(pk=currency_id)
        maintenance = request.POST.get('maintenance')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = generalsetting.created_date
        if request.FILES:
            if request.FILES.get('store_logo'):
                store_logo = request.FILES['store_logo']
            else:
                store_logo = generalsetting.store_logo
            if request.FILES.get('store_email_logo'):
                store_email_logo = request.FILES['store_email_logo']
            else:
                store_email_logo = generalsetting.store_email_logo
            if request.FILES.get('store_invoice_logo'):
                store_invoice_logo = request.FILES['store_invoice_logo']
            else:
                store_invoice_logo = generalsetting.store_invoice_logo
        else:
            store_logo = generalsetting.store_logo
            store_email_logo = generalsetting.store_email_logo
            store_invoice_logo = generalsetting.store_invoice_logo
        general = GeneralSetting(generalsetting_id=generalsetting_id, name=name, owner_name=owner_name, store_address=store_address, 
                    country_id=country, zone_id=zone, language_id=language, currency_id=currency, maintenance=maintenance, 
                    created_by=created_by, modified_by=modified_by, created_date=created_date, store_logo=store_logo, 
                    store_email_logo=store_email_logo, store_invoice_logo=store_invoice_logo)
        general.save()
        return redirect(GeneralSettingdetail)
    return render(request, 'setting/generalsetting.html', {'generalsetting':generalsetting})


def HomePageSettingUpdate(request, homepage_id):
    homepage = HomePage.objects.get(homepage_id=homepage_id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        subscribe_title = request.POST.get('subscribe_title')
        subscribe_content = request.POST.get('subscribe_content')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = homepage.created_date
        if request.FILES:
            if request.FILES.get('image_right'):
                image_right = request.FILES['image_right']
            else:
                image_right = homepage.image_right
            if request.FILES.get('image_left'):
                image_left = request.FILES['image_left']
            else:
                image_left = homepage.image_left
            if request.FILES.get('subscribe_image'):
                subscribe_image = request.FILES['subscribe_image']
            else:
                subscribe_image = homepage.subscribe_image
        else:
            image_right = homepage.image_right
            image_left = homepage.image_left
            subscribe_image = homepage.subscribe_image
        homepage = HomePage(homepage_id=homepage_id, title=title, content=content, subscribe_title=subscribe_title, subscribe_content=subscribe_content, 
                            image_right=image_right, image_left=image_left, subscribe_image=subscribe_image, created_by=created_by, modified_by=modified_by, 
                            created_date=created_date)
        homepage.save()
        return redirect(GeneralSettingdetail)
    return render(request, 'setting/generalsetting.html', {'homepage':homepage})


def SiteSetting(request):
    varient = Varient.objects.all()
    seo = Seo.objects.all()
    social = Social.objects.all()
    return render(request, 'setting/sitesetting.html', {'varient':varient, 'seo':seo, 'social':social})


def VarientAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        print(name)
        sort_order = request.POST.get('sort_order')
        varient_value = request.POST.getlist('varient_value[]')
        sort_order_value = request.POST.getlist('sort_order_value[]')
        select_type = request.POST.get('select_type')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        varient = Varient(name=name, sort_order=sort_order, varient_value=varient_value, sort_order_value=sort_order_value, select_type=select_type, created_by=created_by, modified_by=modified_by)
        varient.save()
        return redirect(SiteSetting)
    return render(request, 'setting/varientadd.html')


def VarientUpdate(request, varient_id):
    varient = Varient.objects.get(varient_id=varient_id)
    if request.method == "POST":
        name = request.POST.get('name')
        sort_order = request.POST.get('sort_order')
        varient_value = request.POST.getlist('varient_value[]')
        sort_order_value = request.POST.getlist('sort_order_value[]')
        select_type = request.POST.get('select_type')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = varient.created_date
        varient = Varient(varient_id=varient_id, name=name, sort_order=sort_order, varient_value=varient_value, sort_order_value=sort_order_value,
                         select_type=select_type, created_by=created_by, modified_by=modified_by, created_date=created_date)
        varient.save()
        return redirect(SiteSetting)
    varient.varient_value = "".join("".join(varient.varient_value.split("['")).split("']")).split("', '")
    varient.sort_order_value = "".join("".join(varient.sort_order_value.split("['")).split("']")).split("', '")
    res = {}
    for key in varient.varient_value:
        for value in varient.sort_order_value:
            res[key] = value
            varient.sort_order_value.remove(value)
            break
    return render(request, 'setting/varientadd.html', {'varient':varient,'res':res})


def VarientDelete(request, varient_id):
    varient = Varient.objects.get(varient_id=varient_id)
    varient.delete()
    return redirect(SiteSetting)


def SeoUpdate(request, seo_id):
    seo = Seo.objects.get(seo_id=seo_id)
    if request.method == "POST":
        meta_title = request.POST.get('meta_title')
        meta_discriptor = request.POST.get('meta_discriptor')
        meta_keyword = request.POST.get('meta_keyword')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = seo.created_date
        seo = Seo(seo_id=seo_id, meta_title=meta_title, meta_discriptor=meta_discriptor, meta_keyword=meta_keyword, created_by=created_by, 
                modified_by=modified_by, created_date=created_date)
        seo.save()
        return redirect(SiteSetting)
    return render(request, 'setting/sitesetting.html', {'seo':seo})


def SocialUpdate(request, social_id):
    social = Social.objects.get(social_id=social_id)
    if request.method == "POST":
        instagram = request.POST.get('instagram')
        twitter = request.POST.get('twitter')
        facebook = request.POST.get('facebook')
        youtube = request.POST.get('youtube')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = social.created_date
        social = Social(social_id=social_id, instagram=instagram, twitter=twitter, facebook=facebook, youtube=youtube, created_by=created_by, 
                        modified_by=modified_by, created_date=created_date)
        social.save()
        return redirect(SiteSetting)
    return render(request, 'setting/sitesetting.html', {'social':social})