from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="xuqiuxinxi_add"),
    path('admin/updt/' , views.adminupdt , name="xuqiuxinxi_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="xuqiuxinxi_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="xuqiuxinxi_detail"),
    # 后台登记人页面
    path('admin/dengjiren/' , views.dengjiren , name="xuqiuxinxi_dengjiren"),
    # 前台列表页面
    path('' , views.index , name="xuqiuxinxiindex"),
    # 前台添加页面
    path('add/' , views.add , name="xuqiuxinxiadd"),
    # 前台详情页面
    path('detail/' , views.detail , name="xuqiuxinxidetail"),

    # 数据插入
    path('insert/' , views.insert , name="xuqiuxinxiinsert"),

    # 数据插入
    path('update/' , views.update , name="xuqiuxinxiupdate"),

    # 删除数据
    path('delete/' , views.delete , name="xuqiuxinxidelete"),




]
