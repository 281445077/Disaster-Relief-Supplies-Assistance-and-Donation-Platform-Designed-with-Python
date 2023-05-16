from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="juanzengshenhe_add"),
    path('admin/updt/' , views.adminupdt , name="juanzengshenhe_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="juanzengshenhe_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="juanzengshenhe_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="juanzengshenhe_juanzengren"),

    # 数据插入
    path('insert/' , views.insert , name="juanzengshenheinsert"),

    # 数据插入
    path('update/' , views.update , name="juanzengshenheupdate"),

    # 删除数据
    path('delete/' , views.delete , name="juanzengshenhedelete"),




]
