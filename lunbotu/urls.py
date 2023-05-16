from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="lunbotu_add"),
    path('admin/updt/' , views.adminupdt , name="lunbotu_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="lunbotu_list"),

    # 数据插入
    path('insert/' , views.insert , name="lunbotuinsert"),

    # 数据插入
    path('update/' , views.update , name="lunbotuupdate"),

    # 删除数据
    path('delete/' , views.delete , name="lunbotudelete"),




]
