from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="liuyanxinxi_add"),
    path('admin/updt/' , views.adminupdt , name="liuyanxinxi_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="liuyanxinxi_list"),
    # 后台收信人页面
    path('admin/shouxinren/' , views.shouxinren , name="liuyanxinxi_shouxinren"),
    # 后台发信人页面
    path('admin/faxinren/' , views.faxinren , name="liuyanxinxi_faxinren"),
    # 前台添加页面
    path('add/' , views.add , name="liuyanxinxiadd"),

    # 数据插入
    path('insert/' , views.insert , name="liuyanxinxiinsert"),

    # 数据插入
    path('update/' , views.update , name="liuyanxinxiupdate"),

    # 删除数据
    path('delete/' , views.delete , name="liuyanxinxidelete"),




]
