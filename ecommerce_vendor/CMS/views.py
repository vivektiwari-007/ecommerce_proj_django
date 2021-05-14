from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PageGroup, Page, Banner, Blog, Testimonial, NewsEvent, ContactUs
from myapp.models import Permission
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/admin/')
def index(request):
    return render(request, "cms/index.html")


@login_required(login_url='/admin/')
def PageGroupDetail(request):
    pagegroup = PageGroup.objects.all()
    count1= PageGroup.objects.filter(is_active=True).count()
    count2= PageGroup.objects.filter(is_active=False).count()
    permission = Permission.objects.all()
    print(permission)
    return render(request, 'cms/pagegroupdetail.html', {'pagegroup':pagegroup,'count1':count1, 'count2':count2, 'permission':permission})


@login_required(login_url='/admin/')
def PageGroupAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        pagegroup = PageGroup(title=title, is_active=active, created_by=created_by, modified_by=modified_by)
        pagegroup.save()
        return redirect(PageGroupDetail)
    permission = Permission.objects.all()
    return render(request, 'cms/pagegroupadd.html', {'permission':permission})


@login_required(login_url='/admin/')
def PageGroupUpdate(request, page_group_id):
    pagegroup = PageGroup.objects.get(page_group_id=page_group_id)
    if request.method == "POST":
        title = request.POST['title']
        active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = pagegroup.created_date
        pagegroup = PageGroup(page_group_id=page_group_id, title=title, is_active=active, created_by=created_by, modified_by=modified_by, created_date=created_date)
        pagegroup.save()
        return redirect(PageGroupDetail)
    return render(request, 'cms/pagegroupadd.html', {'pagegroup':pagegroup})


@login_required(login_url='/admin/')
def PageGroupDelete(request, page_group_id):
    pagegroup = PageGroup.objects.get(page_group_id=page_group_id)
    pagegroup.delete()
    return redirect(PageGroupDetail)


@login_required(login_url='/admin/')
def PageDetail(request):
    page = Page.objects.all()
    count1= Page.objects.filter(is_active=True).count()
    count2= Page.objects.filter(is_active=False).count()
    return render(request, 'cms/pagedetail.html', {'page':page,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def PageAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        intro = request.POST['intro']
        page_group_id = request.POST['page_group_id']
        page_id = PageGroup.objects.get(pk=page_group_id)
        active = request.POST['is_active']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_discripation = request.POST['meta_tag_discripation']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        page = Page(title=title, page_group_id_id=page_id, is_active=active, meta_tag_title=meta_tag_title, 
            meta_tag_discripation=meta_tag_discripation, meta_tag_keyword=meta_tag_keyword, 
            created_by=created_by, modified_by=modified_by, sort_order=sort_order, intro=intro)
        page.save()
        print(page)
        return redirect(PageDetail)
    pagegroup = PageGroup.objects.all()
    return render(request, 'cms/pageadd.html', {'pagegroup':pagegroup})


@login_required(login_url='/admin/')
def PageUpdate(request, page_id):
    page = Page.objects.get(page_id=page_id)
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        intro = request.POST['intro']
        page_group_id = request.POST['page_group_id']
        pages_id = PageGroup.objects.get(pk=page_group_id)
        active = request.POST['is_active']
        meta_tag_title = request.POST['meta_tag_title']
        meta_tag_discripation = request.POST['meta_tag_discripation']
        meta_tag_keyword = request.POST['meta_tag_keyword']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = page.created_date
        page = Page(page_id=page_id, title=title, sort_order=sort_order, intro=intro, page_group_id_id=pages_id, is_active=active, meta_tag_title=meta_tag_title, 
                    meta_tag_discripation=meta_tag_discripation, meta_tag_keyword=meta_tag_keyword, 
                    created_by=created_by, modified_by=modified_by, created_date=created_date)
        page.save()
        return redirect(PageDetail)
    pagegroup = PageGroup.objects.all()
    return render(request, 'cms/pageadd.html', {'page':page,'pagegroup':pagegroup})


@login_required(login_url='/admin/')
def PageDelete(request, page_id):
    page = Page.objects.get(page_id=page_id)
    page.delete()
    return redirect(PageDetail)


@login_required(login_url='/admin/')
def BannerDetail(request):
    banner = Banner.objects.all()
    count1= Banner.objects.filter(is_active=True).count()
    count2= Banner.objects.filter(is_active=False).count()
    return render(request, 'cms/bannerdetail.html', {'banner':banner,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def BannerAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        url = request.POST['url']
        image = request.FILES['image']
        is_active = request.POST['is_active']
        content = request.POST['content']
        position = request.POST['position']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        banner = Banner(title=title, sort_order=sort_order, url=url, image=image, 
        is_active=is_active, content=content, position=position,
        created_by=created_by, modified_by=modified_by)
        banner.save()
        return redirect(BannerDetail)
    return render(request, 'cms/banneradd.html')


@login_required(login_url='/admin/')
def BannerUpdate(request, banner_id):
    banner = Banner.objects.get(banner_id=banner_id)
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        url = request.POST['url']
        # image = request.FILES['image']
        is_active = request.POST['is_active']
        content = request.POST['content']
        position = request.POST['position']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = banner.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = banner.image
        banner = Banner(banner_id=banner_id, title=title, sort_order=sort_order, url=url, image=image, 
        is_active=is_active, content=content, position=position,
        created_by=created_by, modified_by=modified_by, created_date=created_date)
        banner.save()
        return redirect(BannerDetail)
    return render(request, 'cms/banneradd.html', {'banner':banner})


@login_required(login_url='/admin/')
def BannerDelete(request, banner_id):
    banner = Banner.objects.get(banner_id=banner_id)
    banner.delete()
    return redirect(BannerDetail)


@login_required(login_url='/admin/')
def BlogDetail(request):
    blog = Blog.objects.all()
    count1= Blog.objects.filter(is_active=True).count()
    count2= Blog.objects.filter(is_active=False).count()
    return render(request, 'cms/blogdetail.html', {'blog':blog,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def BlogAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        image = request.FILES['image']
        is_active = request.POST['is_active']
        content = request.POST['content']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        blog = Blog(title=title, sort_order=sort_order, image=image, is_active=is_active,
        content=content, created_by=created_by, modified_by=modified_by)
        blog.save()
        return redirect(BlogDetail)
    return render(request, 'cms/blogadd.html')


@login_required(login_url='/admin/')
def BlogUpdate(request, blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    if request.method == "POST":
        title = request.POST['title']
        sort_order = request.POST['sort_order']
        # image = request.FILES['image']
        is_active = request.POST['is_active']
        content = request.POST['content']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = blog.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = blog.image
        blog = Blog(blog_id=blog_id, title=title, sort_order=sort_order, image=image, is_active=is_active,
        content=content, created_by=created_by, modified_by=modified_by, created_date=created_date)
        blog.save()
        return redirect(BlogDetail)
    return render(request, 'cms/blogadd.html', {'blog':blog})


@login_required(login_url='/admin/')
def BlogDelete(request, blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    blog.delete()
    return redirect(BlogDetail)


@login_required(login_url='/admin/')
def TestimonialDetail(request):
    testimonial = Testimonial.objects.all()
    count1= Testimonial.objects.filter(is_active=True).count()
    count2= Testimonial.objects.filter(is_active=False).count()
    return render(request, 'cms/testimonialdetail.html', {'testimonial':testimonial,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def TestimonialAdd(request):
    if request.method == "POST":
        name = request.POST['name']
        image = request.FILES['image']
        is_active = request.POST['is_active']
        discription = request.POST['discription']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        testimonial = Testimonial(name=name, image=image, is_active=is_active, discription=discription,
        created_by=created_by, modified_by=modified_by)
        testimonial.save()
        return redirect(TestimonialDetail)
    return render(request, 'cms/testimonialadd.html')


@login_required(login_url='/admin/')
def TestimonialUpdate(request, testimonial_id):
    testimonial = Testimonial.objects.get(testimonial_id=testimonial_id)
    if request.method == "POST":
        name = request.POST['name']
        # image = request.FILES['image']
        is_active = request.POST['is_active']
        discription = request.POST['discription']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = testimonial.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = testimonial.image
        testimonial = Testimonial(testimonial_id=testimonial_id, name=name, image=image, is_active=is_active, discription=discription,
        created_by=created_by, modified_by=modified_by, created_date=created_date)
        testimonial.save()
        return redirect(TestimonialDetail)
    return render(request, 'cms/testimonialadd.html', {'testimonial':testimonial})


@login_required(login_url='/admin/')
def TestimonialDelete(request, testimonial_id):
    testimonial = Testimonial.objects.get(testimonial_id=testimonial_id)
    testimonial.delete()
    return redirect(TestimonialDetail)


@login_required(login_url='/admin/')
def NewsEventDetail(request):
    newsevent = NewsEvent.objects.all()
    count1= NewsEvent.objects.filter(is_active=True).count()
    count2= NewsEvent.objects.filter(is_active=False).count()
    return render(request, 'cms/newseventdetail.html', {'newsevent':newsevent,'count1':count1,'count2':count2})


@login_required(login_url='/admin/')
def NewsEventAdd(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']
        content = request.POST['content']
        is_active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        newsevent = NewsEvent(title=title, image=image, content=content, is_active=is_active,
        created_by=created_by, modified_by=modified_by)
        newsevent.save()
        return redirect(NewsEventDetail)
    return render(request, 'cms/newseventadd.html')


@login_required(login_url='/admin/')
def NewsEventUpdate(request, newsevent_id):
    newsevent = NewsEvent.objects.get(newsevent_id=newsevent_id)
    if request.method == "POST":
        title = request.POST['title']
        # image = request.FILES['image']
        content = request.POST['content']
        is_active = request.POST['is_active']
        created_by = request.POST['created_by']
        modified_by = request.POST['modified_by']
        created_date = newsevent.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = newsevent.image
        newsevent = NewsEvent(newsevent_id=newsevent_id, title=title, image=image, content=content, is_active=is_active,
        created_by=created_by, modified_by=modified_by, created_date=created_date)
        newsevent.save()
        return redirect(NewsEventDetail)
    return render(request, 'cms/newseventadd.html', {'newsevent':newsevent})


@login_required(login_url='/admin/')
def NewsEventDelete(request, newsevent_id):
    newsevent = NewsEvent.objects.get(newsevent_id=newsevent_id)
    newsevent.delete()
    return redirect(NewsEventDetail)


@login_required(login_url='/admin/')
def ContactUsDetail(request):
    contactus = ContactUs.objects.all()
    return render(request, 'cms/contactusdetail.html', {'contactus':contactus})


@login_required(login_url='/admin/')
def ContactUsUpdate(request, contactus_id):
    contactus = ContactUs.objects.get(contactus_id=contactus_id)
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        start_day = request.POST['start_day']
        end_day = request.POST['end_day']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        created_date = contactus.created_date
        if request.FILES:
            image = request.FILES['image']
        else:
            image = contactus.image
        contact = ContactUs(contactus_id=contactus_id, name=name, email=email, mobile=mobile, start_day=start_day,
         end_day=end_day, start_time=start_time, end_time=end_time, image=image, created_date=created_date)
        contact.save()
        return redirect(ContactUsDetail)
    cont = ContactUs.objects.all()
    return render(request, 'cms/contactusadd.html', {'contactus':contactus, 'cont':cont})

