from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="juanzengwuzi_add"),
    path('admin/updt/' , views.adminupdt , name="juanzengwuzi_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="juanzengwuzi_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="juanzengwuzi_detail"),
    # 后台登记人页面
    path('admin/dengjiren/' , views.dengjiren , name="juanzengwuzi_dengjiren"),
    # 后台捐赠用户页面
    path('admin/juanzengyonghu/' , views.juanzengyonghu , name="juanzengwuzi_juanzengyonghu"),
    # 前台添加页面
    path('add/' , views.add , name="juanzengwuziadd"),

    # 数据插入
    path('insert/' , views.insert , name="juanzengwuziinsert"),

    # 数据插入
    path('update/' , views.update , name="juanzengwuziupdate"),

    # 删除数据
    path('delete/' , views.delete , name="juanzengwuzidelete"),




]
