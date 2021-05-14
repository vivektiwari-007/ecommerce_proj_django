import json as simplejson
from django.shortcuts import render, redirect
from .models import Category, Brand, Product, Coupon, ProductMultiImage, ProductVarientInfo
from setting.models import Varient
from django.contrib.auth.decorators import login_required
from datetime import date
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
import itertools
# Create your views here.
def index(request):
    return render(request, 'catalog/index.html')


@login_required(login_url='/admin/')
def CategoryDetail(request):
    category  = Category.objects.all()
    count1 = Category.objects.filter(is_active=True).count()
    count2 = Category.objects.filter(is_active=False).count()
    return render(request, 'catalog/categorydetail.html', {'category':category, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def CategoryAdd(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        is_active = request.POST['is_active']
        parent_id = request.POST['parent_id']
        sort_order = request.POST['sort_order']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_discripation = request.POST['meta_tag_discripation']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        category = Category(name=name, image=image, is_active=is_active, parent_id=parent_id,
            sort_order=sort_order, meta_tag_title=meta_tag_title, meta_tag_discripation=meta_tag_discripation,
            meta_tag_keyword=meta_tag_keyword, created_by=created_by, modified_by=modified_by)
        category.save()
        return redirect(CategoryDetail)
    cat = Category.objects.all()
    return render(request, 'catalog/categoryadd.html',{'cat':cat})


@login_required(login_url='/admin/')
def CategoryUpdate(request, category_id):
    category = Category.objects.get(category_id=category_id)
    if request.method == "POST":
        name = request.POST['name']
        is_active = request.POST['is_active']
        parent_id = request.POST['parent_id']
        sort_order = request.POST['sort_order']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_discripation = request.POST['meta_tag_discripation']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = category.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = category.image
        category = Category(category_id=category_id,name=name, image=image, is_active=is_active, parent_id=parent_id,
            sort_order=sort_order, meta_tag_title=meta_tag_title, meta_tag_discripation=meta_tag_discripation,
            meta_tag_keyword=meta_tag_keyword, created_by=created_by, modified_by=modified_by, created_date=created_date)
        category.save()
        return redirect(CategoryDetail)
    cat = Category.objects.all()
    return render(request, 'catalog/categoryadd.html',{'cat':cat,'category':category})


@login_required(login_url='/admin/')
def CategoryDelete(request, category_id):
    category = Category.objects.get(category_id=category_id)
    category.delete()
    return redirect(CategoryDetail)


@login_required(login_url='/admin/')
def BrandDetail(request):
    brand = Brand.objects.all()
    count1 = Brand.objects.filter(is_active=True).count()
    count2 = Brand.objects.filter(is_active=False).count()
    return render(request, 'catalog/branddetail.html', {'brand':brand, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def BrandAdd(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        sort_order = request.POST['sort_order']
        is_active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        brand = Brand(name=name, image=image, sort_order=sort_order, is_active=is_active,
            created_by=created_by, modified_by=modified_by)
        brand.save()
        return redirect(BrandDetail)
    return render(request, 'catalog/brandadd.html')


@login_required(login_url='/admin/')
def BrandUpdate(request, brand_id):
    brand = Brand.objects.get(brand_id=brand_id)
    if request.method == "POST":
        name = request.POST['name']
        sort_order = request.POST['sort_order']
        is_active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = brand.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = brand.image
        brand = Brand(brand_id=brand_id, name=name, image=image, sort_order=sort_order, is_active=is_active,
            created_by=created_by, modified_by=modified_by, created_date=created_date)
        brand.save()
        return redirect(BrandDetail)
    return render(request, 'catalog/brandadd.html', {'brand':brand})


@login_required(login_url='/admin/')
def BrandDelete(request,brand_id):
    brand = Brand.objects.get(brand_id=brand_id)
    brand.delete()
    return redirect(BrandDetail)


@login_required(login_url='/admin/')
def ProductDetail(request):
    product = Product.objects.all()
    count1 = Product.objects.filter(is_active=True).count()
    count2 = Product.objects.filter(is_active=False).count()
    return render(request, 'catalog/productdetail.html', {'product':product, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def ProductAdd(request):
    if request.method == "POST":
        name = request.POST.get('name')
        sku = request.POST.get('sku')
        product_slug = request.POST.get('product_slug')
        page_content = request.POST.get('page_content')
        image = request.FILES['image']
        upc = request.POST.get('upc')
        quentity = request.POST.get('quentity')
        out_of_stock = request.POST.get('out_of_stock')
        date_available = request.POST.get('date_available')
        is_active = request.POST.get('is_active')
        sort_order = request.POST.get('sort_order')
        postal_code_verification = request.POST.get('postal_code_verification')
        if postal_code_verification == "on":
            postal_code_verification = True
        else:
            postal_code_verification = False
        related_product = request.POST.get('related_product')
        tax_type = request.POST.get('taxvalue')
        product_cost = request.POST.get('product_cost')
        add_product_cost = request.POST.get('add_product_cost')
        total_cost = request.POST.get('total_cost')
        meta_tag_title = request.POST.get('meta_tag_title')
        meta_tag_discripation = request.POST.get('meta_tag_discripation')
        meta_tag_keyword = request.POST.get('meta_tag_keyword')
        required_shipping = request.POST.get('required_shipping')
        width = request.POST.get('width')
        height = request.POST.get('height')
        length = request.POST.get('length')
        weight = request.POST.get('weight')
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        product = Product(name=name, sku=sku, product_slug=product_slug, page_content=page_content, image=image, 
                upc=upc, quentity=quentity, out_of_stock=out_of_stock, date_available=date_available, is_active=is_active, sort_order=sort_order, 
                postal_code_verification=postal_code_verification, related_product=related_product, tax_type=tax_type,
                product_cost=product_cost, add_product_cost=add_product_cost, total_cost=total_cost, meta_tag_title=meta_tag_title, meta_tag_discripation=meta_tag_discripation, 
                meta_tag_keyword=meta_tag_keyword, required_shipping=required_shipping, width=width, height=height, length=length, weight=weight, created_by=created_by, modified_by=modified_by)
        product.save()
        multiimage = request.FILES.getlist('multiimage')
        for multii in multiimage:
            ProductMultiImage.objects.create(product_id=product, multiimage=multii)
        varient_image = request.FILES.getlist('varient_image')
        varient_name = request.POST.getlist('varient_name')
        varient_sku = request.POST.getlist('varient_sku')
        varient_price = request.POST.getlist('varient_price')
        varient_barcode = request.POST.getlist('varient_barcode')
        varient_inventory = request.POST.getlist('varient_inventory')
        varient_status = request.POST.getlist('varient_status')
        for (image,name,sku,price,barcode,inventory,status) in itertools.zip_longest(varient_image,varient_name,varient_sku,varient_price,varient_barcode,varient_inventory,varient_status):
            if status == "on":
                status = True
            else:
                status = False
            ProductVarientInfo.objects.create(product_id=product, varientinfo_image=image, varientinfo_name=name, varientinfo_sku=sku, varientinfo_price=price, varientinfo_barcode=barcode, varientinfo_inventory=inventory, varientinfo_status=status)
        for x in request.POST.getlist('category_id[]'):
            product.category_id.add(x)
        for y in request.POST.getlist('brand_id[]'):
            product.brand_id.add(y)
        return redirect(ProductDetail)
    category = Category.objects.all()
    brand = Brand.objects.all()
    prod = Product.objects.all()
    varient = Varient.objects.all()
    return render(request, 'catalog/productadd.html', {'category':category, 'brand':brand, 'prod':prod, 'varient':varient})


@login_required(login_url='/admin/')
def ProductUpdate(request, product_id):
    product = Product.objects.get(product_id=product_id)
    if request.method == "POST":
        name = request.POST['name']
        sku = request.POST['sku']
        product_slug = request.POST['product_slug']
        page_content = request.POST['page_content']
        upc = request.POST['upc']
        quentity = request.POST['quentity']
        out_of_stock = request.POST['out_of_stock']
        date_available = request.POST['date_available']
        is_active = request.POST['is_active']
        sort_order = request.POST['sort_order']
        postal_code_verification = request.POST.get('postal_code_verification')
        related_product = request.POST['related_product']
        tax_type = request.POST.get('taxvalue')
        product_cost = request.POST['product_cost']
        add_product_cost = request.POST['add_product_cost']
        total_cost = request.POST['total_cost']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_discripation = request.POST['meta_tag_discripation']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        required_shipping = request.POST.get('required_shipping')
        width = request.POST.get('width')
        height = request.POST.get('height')
        length = request.POST.get('length')
        weight = request.POST.get('weight')
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = product.created_date
        print(product.productmultiimage_set.all())
        for pv in product.productvarientinfo_set.all():
            print(pv.varientinfo_image)
        if request.FILES:
            if request.FILES.get('image'):
                image = request.FILES['image']
            else:
                image = product.image
            if request.FILES.getlist('multiimage'):
                multiimage = request.FILES.getlist('multiimage')
            # if request.FILES.getlist('varient_image'):
            #     varient_image = request.FILES.getlist('varient_image')
            # else:
            #     for pv in product.productvarientinfo_set.all():
            #         varient_image = pv.varientinfo_image
            #     return varient_image
        else:
            image = product.image
        product = Product(product_id=product_id, name=name, sku=sku, product_slug=product_slug, page_content=page_content, image=image, 
                upc=upc, quentity=quentity, out_of_stock=out_of_stock, date_available=date_available, is_active=is_active, sort_order=sort_order, 
                postal_code_verification=postal_code_verification, related_product=related_product, tax_type=tax_type,
                product_cost=product_cost, add_product_cost=add_product_cost, total_cost=total_cost, meta_tag_title=meta_tag_title, meta_tag_discripation=meta_tag_discripation, 
                meta_tag_keyword=meta_tag_keyword, required_shipping=required_shipping, width=width, height=height, length=length, weight=weight, created_by=created_by, modified_by=modified_by, created_date=created_date)
        product.save()
        if request.FILES.getlist('multiimage'):
            product.productmultiimage_set.clear()
            for multii in multiimage:
                ProductMultiImage.objects.create(product_id=product, multiimage=multii)
        varient_image = request.FILES.getlist('varient_image')
        varient_sku = request.POST.getlist('varient_sku')
        varient_price = request.POST.getlist('varient_price')
        varient_barcode = request.POST.getlist('varient_barcode')
        varient_inventory = request.POST.getlist('varient_inventory')
        varient_status = request.POST.getlist('varient_status')
        product.productvarientinfo_set.clear()
        for (image,sku,price,barcode,inventory,status) in itertools.zip_longest(varient_image,varient_sku,varient_price,varient_barcode,varient_inventory,varient_status):
            if status == "on":
                status = True
            else:
                status = False
            ProductVarientInfo.objects.create(product_id=product, varientinfo_image=image, varientinfo_sku=sku, varientinfo_price=price, varientinfo_barcode=barcode, varientinfo_inventory=inventory, varientinfo_status=status)
        product.category_id.clear()
        for x in request.POST.getlist('category_id[]'):
            product.category_id.add(x)
        product.brand_id.clear()
        for y in request.POST.getlist('brand_id[]'):
            product.brand_id.add(y)
        return redirect(ProductDetail)
    category = Category.objects.all()
    product_category = []
    for i in product.category_id.all():
        product_category.append(i.category_id)
    brand = Brand.objects.all()
    product_brand = []
    for j in product.brand_id.all():
        product_brand.append(j.brand_id)
    prod = Product.objects.all()
    varient = Varient.objects.all()
    productvarientinfo = ProductVarientInfo.objects.all()
    return render(request, 'catalog/productadd.html', {'category':category, 'brand':brand, 'prod':prod, 'product':product, 'product_category': product_category, 'product_brand':product_brand, 'varient':varient, 'productvarientinfo':productvarientinfo})


@login_required(login_url='/admin/')
def ProductDelete(request, product_id):
    product = Product.objects.get(product_id=product_id)
    product.delete()
    return redirect(ProductDetail)


@login_required(login_url='/admin/')
def CouponDetail(request):
    coupon = Coupon.objects.all()
    count1 = Coupon.objects.filter(is_active=True).count()
    count2 = Coupon.objects.filter(is_active=False).count()
    return render(request, 'catalog/coupondetail.html', {'coupon':coupon,'count1':count1,'count2':count2})


import datetime
@login_required(login_url='/admin/')
def CouponAdd(request):
    if request.method == "POST":
        coupon_code = request.POST.get('coupon_code')
        coupon_description = request.POST.get('coupon_description')
        coupon_type = request.POST.get('coupon_type')
        coupon_value = request.POST.get('coupon_value')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        d0 = date.fromisoformat(start_date)
        d1 = date.fromisoformat(end_date)
        delta = d1 - d0
        day_left = delta.days
        minimum_purchase_amount = request.POST.get('minimum_purchase_amount')
        maximum_purchase_amount = request.POST.get('maximum_purchase_amount')
        email = request.POST.get('email')
        coupon_limit_use = request.POST.get('coupon_limit_use')
        no_of_times_use_discount = request.POST.get('no_of_times_use_discount')
        is_active = request.POST.get('is_active')
        coupne_code_apply_all_item_in_the_cart = request.POST.get('coupne_code_apply_all_item_in_the_cart')
        no_of_item_cart_apply_coupon = request.POST.get('no_of_item_cart_apply_coupon')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        coupon = Coupon(coupon_code=coupon_code, coupon_description=coupon_description, coupon_type=coupon_type, coupon_value=coupon_value, 
                        start_date=start_date, end_date=end_date, day_left=day_left, minimum_purchase_amount=minimum_purchase_amount, maximum_purchase_amount=maximum_purchase_amount, 
                        email=email, coupon_limit_use=coupon_limit_use, no_of_times_use_discount=no_of_times_use_discount, is_active=is_active, 
                        coupne_code_apply_all_item_in_the_cart=coupne_code_apply_all_item_in_the_cart, no_of_item_cart_apply_coupon=no_of_item_cart_apply_coupon,
                        created_by=created_by, modified_by=modified_by)
        coupon.save()
        for x in request.POST.getlist('product_id[]'):
            coupon.product_id.add(x)
        return redirect(CouponDetail)
    product = Product.objects.all()
    return render(request, 'catalog/couponadd.html', {'product':product})


@login_required(login_url='/admin/')
def CouponUpdate(request, coupon_id):
    coupon = Coupon.objects.get(coupon_id=coupon_id)
    if request.method == "POST":
        coupon_code = request.POST.get('coupon_code')
        coupon_description = request.POST.get('coupon_description')
        coupon_type = request.POST.get('coupon_type')
        coupon_value = request.POST.get('coupon_value')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        d0 = date.fromisoformat(start_date)
        d1 = date.fromisoformat(end_date)
        delta = d1 - d0
        day_left = delta.days
        minimum_purchase_amount = request.POST.get('minimum_purchase_amount')
        maximum_purchase_amount = request.POST.get('maximum_purchase_amount')
        email = request.POST.get('email')
        coupon_limit_use = request.POST.get('coupon_limit_use')
        no_of_times_use_discount = request.POST.get('no_of_times_use_discount')
        is_active = request.POST.get('is_active')
        coupne_code_apply_all_item_in_the_cart = request.POST.get('coupne_code_apply_all_item_in_the_cart')
        no_of_item_cart_apply_coupon = request.POST.get('no_of_item_cart_apply_coupon')
        created_by = request.POST.get('created_by')
        modified_by = request.POST.get('modified_by')
        created_date = coupon.created_date
        coupon = Coupon(coupon_id=coupon_id, coupon_code=coupon_code, coupon_description=coupon_description, coupon_type=coupon_type, coupon_value=coupon_value, 
                        start_date=start_date, end_date=end_date, day_left=day_left, minimum_purchase_amount=minimum_purchase_amount, maximum_purchase_amount=maximum_purchase_amount, 
                        email=email, coupon_limit_use=coupon_limit_use, no_of_times_use_discount=no_of_times_use_discount, is_active=is_active, 
                        coupne_code_apply_all_item_in_the_cart=coupne_code_apply_all_item_in_the_cart, no_of_item_cart_apply_coupon=no_of_item_cart_apply_coupon,
                        created_by=created_by, modified_by=modified_by, created_date=created_date)
        coupon.save()
        for x in request.POST.getlist('product_id[]'):
            coupon.product_id.add(x)
        return redirect(CouponDetail)
    product = Product.objects.all()
    return render(request, 'catalog/couponadd.html', {'product':product,'coupon':coupon})


@login_required(login_url='/admin/')
def CouponDelete(request, coupon_id):
    coupon = Coupon.objects.get(coupon_id=coupon_id)
    coupon.delete()
    return redirect(CouponDetail)


def VarientInfo(request):
    name = request.GET.get('varient')
    data = Varient.objects.get(pk=int(name))
    name = data.name
    data = data.varient_value   
    return JsonResponse(data, safe=False)



