from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),

    path("servicecategory", views.ServiceCategoryDetail, name="servicecategorydetail"),
    path("servicecategoryadd", views.ServiceCategoryAdd, name="servicecategoryadd"),
    path("servicecategoryupdate/<int:servicecategory_id>", views.ServiceCategoryUpdate, name="servicecategoryupdate"),
    path("servicecategorydelete/<int:servicecategory_id>", views.ServiceCategoryDelete, name="servicecategorydelete"),
    
    path("servicelist", views.ServiceListDetail, name="servicelistdetail"),
    path("servicelistadd", views.ServiceListAdd, name="servicelistadd"),
    path("servicelistupdate/<int:servicelist_id>", views.ServiceListUpdate, name="servicelistupdate"),
    path("servicelistdelete/<int:servicelist_id>", views.ServiceListDelete, name="servicelistdelete"),
]
