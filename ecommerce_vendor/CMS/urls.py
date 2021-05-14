from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("pagegroup", views.PageGroupDetail, name="pagegroupdetail"),
    path("pagegroupadd", views.PageGroupAdd, name="pagegroupadd"),
    path("pagegroupupdate/<int:page_group_id>", views.PageGroupUpdate, name="pagegroupupdate"),
    path("pagegroupdelete/<int:page_group_id>", views.PageGroupDelete, name="pagegroupdelete"),
    
    path("page", views.PageDetail, name="pagedetail"),
    path("pageadd", views.PageAdd, name="pageadd"),
    path("pageupdate/<int:page_id>", views.PageUpdate, name="pageupdate"),
    path("pagedelete/<int:page_id>", views.PageDelete, name="pagedelete"),

    path("banner", views.BannerDetail, name="bannerdetail"),
    path("banneradd", views.BannerAdd, name="banneradd"),
    path("bannerupdate/<int:banner_id>", views.BannerUpdate, name="bannerupdate"),
    path("bannerdelete/<int:banner_id>", views.BannerDelete, name="bannerdelete"),

    path("blog", views.BlogDetail, name="blogdetail"),
    path("blogadd", views.BlogAdd, name="blogadd"),
    path("blogupdate/<int:blog_id>", views.BlogUpdate, name="blogupdate"),
    path("blogdelete/<int:blog_id>", views.BlogDelete, name="blogdelete"),

    path("testimonial", views.TestimonialDetail, name="testimonialdetail"),
    path("testimonialadd", views.TestimonialAdd, name="testimonialadd"),
    path("testimonialupdate/<int:testimonial_id>", views.TestimonialUpdate, name="testimonialupdate"),
    path("testimonialdelete/<int:testimonial_id>", views.TestimonialDelete, name="testimonialdelete"),
    
    path("newsevent", views.NewsEventDetail, name="newseventdetail"),
    path("newseventadd", views.NewsEventAdd, name="newseventadd"),
    path("newseventupdate/<int:newsevent_id>", views.NewsEventUpdate, name="newseventupdate"),
    path("newseventdelete/<int:newsevent_id>", views.NewsEventDelete, name="newseventdelete"),
    
    path("contactus", views.ContactUsDetail, name="contactusdetail"),
    path("contactusupdate/<int:contactus_id>", views.ContactUsUpdate, name="contactusupdate"),
]
