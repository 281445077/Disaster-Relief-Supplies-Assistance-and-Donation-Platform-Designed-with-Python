from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="wupinleibie_add"),
    path('admin/updt/' , views.adminupdt , name="wupinleibie_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="wupinleibie_list"),

    # 数据插入
    path('insert/' , views.insert , name="wupinleibieinsert"),

    # 数据插入
    path('update/' , views.update , name="wupinleibieupdate"),

    # 删除数据
    path('delete/' , views.delete , name="wupinleibiedelete"),




]
