from django.urls import path,include
from . import views
urlpatterns = [
    # 后台添加页面
    path('admin/add/' , views.adminadd , name="qianshou_add"),
    path('admin/updt/' , views.adminupdt , name="qianshou_updt"),
    # 后台列表页面
    path('admin/list/' , views.adminlist , name="qianshou_list"),
    # 后台详情页面
    path('admin/detail/' , views.admindetail , name="qianshou_detail"),
    # 后台捐赠人页面
    path('admin/juanzengren/' , views.juanzengren , name="qianshou_juanzengren"),
    # 后台申请用户页面
    path('admin/shenqingyonghu/' , views.shenqingyonghu , name="qianshou_shenqingyonghu"),

    # 数据插入
    path('insert/' , views.insert , name="qianshouinsert"),

    # 数据插入
    path('update/' , views.update , name="qianshouupdate"),

    # 删除数据
    path('delete/' , views.delete , name="qianshoudelete"),




]
