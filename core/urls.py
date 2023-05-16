"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path , include
from common import views

urlpatterns = [
    path('admins/' , include('admins.urls')),
    path('xinwenfenlei/' , include('xinwenfenlei.urls')),
    path('xinwenxinxi/' , include('xinwenxinxi.urls')),
    path('youqinglianjie/' , include('youqinglianjie.urls')),
    path('liuyanxinxi/' , include('liuyanxinxi.urls')),
    path('lunbotu/' , include('lunbotu.urls')),
    path('yonghu/' , include('yonghu.urls')),
    path('juanzeng/' , include('juanzeng.urls')),
    path('juanzengshenhe/' , include('juanzengshenhe.urls')),
    path('juanji/' , include('juanji.urls')),
    path('juanjishenhe/' , include('juanjishenhe.urls')),
    path('chuli/' , include('chuli.urls')),
    path('xuqiuxinxi/' , include('xuqiuxinxi.urls')),
    path('xuqiushenhe/' , include('xuqiushenhe.urls')),
    path('juanzengwuzi/' , include('juanzengwuzi.urls')),
    path('lingqu/' , include('lingqu.urls')),
    path('shenling/' , include('shenling.urls')),
    path('shenlingshenhe/' , include('shenlingshenhe.urls')),
    path('paiji/' , include('paiji.urls')),
    path('qianshou/' , include('qianshou.urls')),
    path('wupinleibie/' , include('wupinleibie.urls')),
    path('common/' , include('common.urls')),

    path('' ,  views.index , name='index'),
    path('login/' ,  views.login , name='login'),
    path('logout/' ,  views.logout , name='logout'),
    path('main/' ,  views.main , name='main'),
    path('sy/' ,  views.adminsy , name='adminsy'),

#   内置管理界面
#   path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
