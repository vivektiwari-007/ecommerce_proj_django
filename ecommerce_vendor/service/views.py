from django.shortcuts import render, redirect
from .models import ServiceCategory, ServiceList
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/admin/')
def index(request):
    return render(request, "cms/index.html")


@login_required(login_url='/admin/')
def ServiceCategoryDetail(request):
    servicecategory = ServiceCategory.objects.all()
    count1 = ServiceCategory.objects.filter(is_active=True).count()
    count2 = ServiceCategory.objects.filter(is_active=False).count()
    return render(request, 'service/servicecategorydetail.html', {'servicecategory':servicecategory, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def ServiceCategoryAdd(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        is_active = request.POST['is_active']
        parent_id = request.POST['parent_id']
        sort_order = request.POST['sort_order']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_description = request.POST['meta_tag_description']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        servicecategory = ServiceCategory(name=name, image=image, is_active=is_active,
        parent_id=parent_id, sort_order=sort_order, meta_tag_title=meta_tag_title, 
        meta_tag_description=meta_tag_description, meta_tag_keyword=meta_tag_keyword,
        created_by=created_by, modified_by=modified_by)
        servicecategory.save()
        return redirect(ServiceCategoryDetail)
    sc = ServiceCategory.objects.all()
    return render(request, 'service/servicecategoryadd.html',{'sc':sc})


@login_required(login_url='/admin/')
def ServiceCategoryUpdate(request, servicecategory_id):
    servicecategory = ServiceCategory.objects.get(servicecategory_id=servicecategory_id)
    if request.method == "POST":
        name = request.POST['name']
        # image = request.FILES['image']
        is_active = request.POST['is_active']
        parent_id = request.POST['parent_id']
        sort_order = request.POST['sort_order']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_description = request.POST['meta_tag_description']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = servicecategory.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = servicecategory.image
        servicecategory = ServiceCategory(servicecategory_id=servicecategory_id, name=name, image=image, is_active=is_active,
        parent_id=parent_id, sort_order=sort_order, meta_tag_title=meta_tag_title, 
        meta_tag_description=meta_tag_description, meta_tag_keyword=meta_tag_keyword,
        created_by=created_by, modified_by=modified_by, created_date=created_date)
        servicecategory.save()
        return redirect(ServiceCategoryDetail)
    sc = ServiceCategory.objects.all()
    return render(request, 'service/servicecategoryadd.html', {'servicecategory':servicecategory, 'sc':sc})


@login_required(login_url='/admin/')
def ServiceCategoryDelete(request, servicecategory_id):
    servicecategory = ServiceCategory.objects.get(servicecategory_id=servicecategory_id)
    servicecategory.delete()
    return redirect(ServiceCategoryDetail)


@login_required(login_url='/admin/')
def ServiceListDetail(request):
    servicelist = ServiceList.objects.all()
    count1 = ServiceList.objects.filter(is_active=True).count()
    count2 = ServiceList.objects.filter(is_active=False).count()
    return render(request, 'service/servicelistdetail.html', {'servicelist':servicelist, 'count1':count1, 'count2':count2})


@login_required(login_url='/admin/')
def ServiceListAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        category_id = request.POST['category_id']
        print(category_id)
        service_id = ServiceCategory.objects.get(pk=category_id)
        image = request.FILES['image']
        is_active = request.POST['is_active']
        cost = request.POST['cost']
        phone_number = request.POST['phone_number']
        product_description = request.POST['product_description']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_description = request.POST['meta_tag_description']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        servicelist = ServiceList(title=title, category_id=service_id, image=image, 
            is_active=is_active, cost=cost, phone_number=phone_number, product_description=product_description,
            meta_tag_title=meta_tag_title, meta_tag_description=meta_tag_description, meta_tag_keyword=meta_tag_keyword,
            created_by=created_by, modified_by=modified_by)
        servicelist.save()
        return redirect(ServiceListDetail)
    sc = ServiceCategory.objects.all()
    return render(request, 'service/servicelistadd.html',{'sc':sc})


@login_required(login_url='/admin/')
def ServiceListUpdate(request, servicelist_id):
    servicelist = ServiceList.objects.get(servicelist_id=servicelist_id)
    if request.method == "POST":
        title = request.POST['title']
        category_id = request.POST['category_id']
        print(category_id)
        service_id = ServiceCategory.objects.get(pk=category_id)
        # image = request.FILES['image']
        is_active = request.POST['is_active']
        cost = request.POST['cost']
        phone_number = request.POST['phone_number']
        product_description = request.POST['product_description']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_description = request.POST['meta_tag_description']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = servicelist.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = servicelist.image
        servicelist = ServiceList(servicelist_id=servicelist_id, title=title, category_id=service_id, image=image, 
            is_active=is_active, cost=cost, phone_number=phone_number, product_description=product_description,
            meta_tag_title=meta_tag_title, meta_tag_description=meta_tag_description, meta_tag_keyword=meta_tag_keyword,
            created_by=created_by, modified_by=modified_by, created_date=created_date)
        servicelist.save()
        return redirect(ServiceListDetail)
    sc = ServiceCategory.objects.all()
    return render(request, 'service/servicelistadd.html',{'servicelist':servicelist,'sc':sc})


@login_required(login_url='/admin/')
def ServiceListDelete(request, servicelist_id):
    servicelist = ServiceList.objects.get(servicelist_id=servicelist_id)
    servicelist.delete()
    return redirect(ServiceListDetail)