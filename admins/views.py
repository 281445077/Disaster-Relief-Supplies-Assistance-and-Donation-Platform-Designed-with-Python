from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Admins
from common.utils import input
from common import utils,models as commonModels




# Create your views here.

def getWhere(request,qs):
    if request.GET.get("username"):
        qs = qs.filter(username__contains=request.GET.get("username"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Admins.objects)

    qs = qs.all()
    # 分页数
    pagesize = input(request, "pagesize", 12)
    # 分页获取数据
    paginator = Paginator(qs, pagesize)
    # 获取当前page页码，默认为1
    page = request.GET.get('page', 1)
    try:
        list = paginator.page(page)  # 分页
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)

    is_paginated = True if paginator.num_pages > 1 else False
    page_range = paginator.get_elided_page_range(page, on_each_side=3, on_ends=2)

    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    page = list

    #context = {'list': list, 'page': list, 'paginator': paginator,
    #           'is_paginated': is_paginated,'page_range': page_range }

    return render(request , "admins/admin/list.html" , locals() , )




#后台添加页面
def adminadd(request):

    return render(request , "admins/admin/add.html",locals())






def adminupdt(request):
    id = request.GET.get("id")
    mmm = Admins.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "admins/admin/updt.html" , locals())


def adminupdtself(request):
    id = request.session['id']
    mmm = Admins.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")

    return render(request, "admins/admin/updtself.html" , locals())





def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Admins.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):

    post = request.POST.copy()
    data = {
        'username': utils.input(request,'username',''),
        'pwd': utils.input(request,'pwd',''),

    }


    model = Admins(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Admins.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'username': utils.input(request,'username',old.username),
        'pwd': utils.input(request,'pwd',old.pwd),

    }



    model = Admins(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)


