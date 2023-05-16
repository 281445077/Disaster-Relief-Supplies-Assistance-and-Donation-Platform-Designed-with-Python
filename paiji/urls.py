from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="paiji_add"),
    path('admin/updt/' , views.adminupdt , name="paiji_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="paiji_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="paiji_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="paiji_juanzengren"),
    # 后台申请用户页面
    path('admin/shenqingyonghu/' , views.shenqingyonghu , name="paiji_shenqingyonghu"),
    # 后台操作人页面
    path('admin/caozuoren/' , views.caozuoren , name="paiji_caozuoren"),

    # 数据插入
    path('insert/' , views.insert , name="paijiinsert"),

    # 数据插入
    path('update/' , views.update , name="paijiupdate"),

    # 删除数据
    path('delete/' , views.delete , name="paijidelete"),




]
