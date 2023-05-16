from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="shenling_add"),
    path('admin/updt/' , views.adminupdt , name="shenling_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="shenling_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="shenling_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="shenling_juanzengren"),
    # 后台申请用户页面
    path('admin/shenqingyonghu/' , views.shenqingyonghu , name="shenling_shenqingyonghu"),
    # 前台添加页面
    path('add/' , views.add , name="shenlingadd"),

    # 数据插入
    path('insert/' , views.insert , name="shenlinginsert"),

    # 数据插入
    path('update/' , views.update , name="shenlingupdate"),

    # 删除数据
    path('delete/' , views.delete , name="shenlingdelete"),




]
