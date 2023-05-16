from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="admins_add"),
    path('admin/updt/' , views.adminupdt , name="admins_updt"),
    path('admin/updtself/' , views.adminupdtself , name="admins_updtself"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="admins_list"),

    # 数据插入
    path('insert/' , views.insert , name="adminsinsert"),

    # 数据插入
    path('update/' , views.update , name="adminsupdate"),

    # 删除数据
    path('delete/' , views.delete , name="adminsdelete"),




]
