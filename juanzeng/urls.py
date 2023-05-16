from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="juanzeng_add"),
    path('admin/updt/' , views.adminupdt , name="juanzeng_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="juanzeng_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="juanzeng_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="juanzeng_juanzengren"),
    # 前台列表页面
    path('' , views.index , name="juanzengindex"),
    # 前台添加页面
    path('add/' , views.add , name="juanzengadd"),
    # 前台详情页面
    path('detail/' , views.detail , name="juanzengdetail"),

    # 数据插入
    path('insert/' , views.insert , name="juanzenginsert"),

    # 数据插入
    path('update/' , views.update , name="juanzengupdate"),

    # 删除数据
    path('delete/' , views.delete , name="juanzengdelete"),




]
