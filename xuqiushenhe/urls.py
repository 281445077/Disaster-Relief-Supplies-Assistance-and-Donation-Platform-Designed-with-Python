from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="xuqiushenhe_add"),
    path('admin/updt/' , views.adminupdt , name="xuqiushenhe_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="xuqiushenhe_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="xuqiushenhe_detail"),
    # 后台登记人页面
    path('admin/dengjiren/' , views.dengjiren , name="xuqiushenhe_dengjiren"),
    # 后台审核人页面
    path('admin/shenheren/' , views.shenheren , name="xuqiushenhe_shenheren"),

    # 数据插入
    path('insert/' , views.insert , name="xuqiushenheinsert"),

    # 数据插入
    path('update/' , views.update , name="xuqiushenheupdate"),

    # 删除数据
    path('delete/' , views.delete , name="xuqiushenhedelete"),




]
