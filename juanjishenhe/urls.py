from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="juanjishenhe_add"),
    path('admin/updt/' , views.adminupdt , name="juanjishenhe_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="juanjishenhe_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="juanjishenhe_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="juanjishenhe_juanzengren"),

    # 数据插入
    path('insert/' , views.insert , name="juanjishenheinsert"),

    # 数据插入
    path('update/' , views.update , name="juanjishenheupdate"),

    # 删除数据
    path('delete/' , views.delete , name="juanjishenhedelete"),




]
