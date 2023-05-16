from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="shenlingshenhe_add"),
    path('admin/updt/' , views.adminupdt , name="shenlingshenhe_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="shenlingshenhe_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="shenlingshenhe_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="shenlingshenhe_juanzengren"),
    # 后台申请用户页面
    path('admin/shenqingyonghu/' , views.shenqingyonghu , name="shenlingshenhe_shenqingyonghu"),
    # 后台审核人页面
    path('admin/shenheren/' , views.shenheren , name="shenlingshenhe_shenheren"),

    # 数据插入
    path('insert/' , views.insert , name="shenlingshenheinsert"),

    # 数据插入
    path('update/' , views.update , name="shenlingshenheupdate"),

    # 删除数据
    path('delete/' , views.delete , name="shenlingshenhedelete"),




]
