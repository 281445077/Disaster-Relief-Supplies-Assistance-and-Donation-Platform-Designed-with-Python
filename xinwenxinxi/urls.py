from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="xinwenxinxi_add"),
    path('admin/updt/' , views.adminupdt , name="xinwenxinxi_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="xinwenxinxi_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="xinwenxinxi_detail"),
    # 前台列表页面
    path('' , views.index , name="xinwenxinxiindex"),
    # 前台详情页面
    path('detail/' , views.detail , name="xinwenxinxidetail"),

    # 数据插入
    path('insert/' , views.insert , name="xinwenxinxiinsert"),

    # 数据插入
    path('update/' , views.update , name="xinwenxinxiupdate"),

    # 删除数据
    path('delete/' , views.delete , name="xinwenxinxidelete"),




]
