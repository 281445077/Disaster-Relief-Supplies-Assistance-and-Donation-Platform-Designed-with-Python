from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Liuyanxinxi
from common.utils import input
from common import utils,models as commonModels




# Create your views here.

def getWhere(request,qs):




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Liuyanxinxi.objects)

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

    return render(request , "liuyanxinxi/admin/list.html" , locals() , )
# 收信人列表页面
def shouxinren(request):
    qs = getWhere(request,Liuyanxinxi.objects)
    qs = qs.filter(shouxinren=request.session['username'])

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
    page = list

    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()

    #context = {'list': list, 'page': list, 'paginator': paginator,
    #           'is_paginated': is_paginated,'page_range': page_range }

    return render(request , "liuyanxinxi/admin/shouxinren.html" , locals() , )
# 发信人列表页面
def faxinren(request):
    qs = getWhere(request,Liuyanxinxi.objects)
    qs = qs.filter(faxinren=request.session['username'])

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
    page = list

    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()

    #context = {'list': list, 'page': list, 'paginator': paginator,
    #           'is_paginated': is_paginated,'page_range': page_range }

    return render(request , "liuyanxinxi/admin/faxinren.html" , locals() , )




#后台添加页面
def adminadd(request):

    return render(request , "liuyanxinxi/admin/add.html",locals())


# 前台添加页面
def add(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");



    return render(request , "liuyanxinxi/add.html",locals())




def adminupdt(request):
    id = request.GET.get("id")
    mmm = Liuyanxinxi.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "liuyanxinxi/admin/updt.html" , locals())







def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Liuyanxinxi.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");

    post = request.POST.copy()
    data = {
        'shouxinren': utils.input(request,'shouxinren',''),
        'xinxineirong': utils.input(request,'xinxineirong',''),
        'faxinren': utils.input(request,'faxinren',''),
        'huifuneirong': utils.input(request,'huifuneirong',''),

    }
    if data['shouxinren'] == '':
        data['shouxinren'] = utils.session(request, "username")
    if data['faxinren'] == '':
        data['faxinren'] = utils.session(request, "username")


    model = Liuyanxinxi(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Liuyanxinxi.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'shouxinren': utils.input(request,'shouxinren',old.shouxinren),
        'xinxineirong': utils.input(request,'xinxineirong',old.xinxineirong),
        'faxinren': utils.input(request,'faxinren',old.faxinren),
        'huifuneirong': utils.input(request,'huifuneirong',old.huifuneirong),
        'addtime': old.addtime,

    }



    model = Liuyanxinxi(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



