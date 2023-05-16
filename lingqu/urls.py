from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="lingqu_add"),
    path('admin/updt/' , views.adminupdt , name="lingqu_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="lingqu_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="lingqu_detail"),
    # 后台捐赠用户页面
    path('admin/juanzengyonghu/' , views.juanzengyonghu , name="lingqu_juanzengyonghu"),
    # 后台登记人页面
    path('admin/dengjiren/' , views.dengjiren , name="lingqu_dengjiren"),

    # 数据插入
    path('insert/' , views.insert , name="lingquinsert"),

    # 数据插入
    path('update/' , views.update , name="lingquupdate"),

    # 删除数据
    path('delete/' , views.delete , name="lingqudelete"),




]
