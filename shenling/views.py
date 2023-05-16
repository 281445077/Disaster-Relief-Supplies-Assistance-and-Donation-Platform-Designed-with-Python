from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Shenling
from common.utils import input
from common import utils,models as commonModels


from juanzeng.models import Juanzeng
from wupinleibie.models import Wupinleibie

# Create your views here.

def getWhere(request,qs):
    if request.GET.get("juanzengid"):
        qs = qs.filter(juanzengid=request.GET.get("juanzengid"))
    if request.GET.get("biaoti"):
        qs = qs.filter(biaoti__contains=request.GET.get("biaoti"))
    if request.GET.get("wupin"):
        qs = qs.filter(wupin__contains=request.GET.get("wupin"))
    if request.GET.get("wupinleibie"):
        qs = qs.filter(wupinleibie=request.GET.get("wupinleibie"))
    if request.GET.get("shenlingrenxingming"):
        qs = qs.filter(shenlingrenxingming__contains=request.GET.get("shenlingrenxingming"))
    if request.GET.get("shenlingrenxingbie"):
        qs = qs.filter(shenlingrenxingbie=request.GET.get("shenlingrenxingbie"))
    if request.GET.get("shenlingzhuangtai"):
        qs = qs.filter(shenlingzhuangtai=request.GET.get("shenlingzhuangtai"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Shenling.objects)

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

    return render(request , "shenling/admin/list.html" , locals() , )
# 捐赠人列表页面
def juanzengren(request):
    qs = getWhere(request,Shenling.objects)
    qs = qs.filter(juanzengren=request.session['username'])

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

    return render(request , "shenling/admin/juanzengren.html" , locals() , )
# 申请用户列表页面
def shenqingyonghu(request):
    qs = getWhere(request,Shenling.objects)
    qs = qs.filter(shenqingyonghu=request.session['username'])

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

    return render(request , "shenling/admin/shenqingyonghu.html" , locals() , )




#后台添加页面
def adminadd(request):

    if 'id' in request.GET:
        id = request.GET.get('id')
        readMap = Juanzeng.objects.get(pk = id)
    return render(request , "shenling/admin/add.html",locals())


# 前台添加页面
def add(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");


    if 'id' in request.GET:
        id = request.GET.get('id')
        readMap = Juanzeng.objects.get(pk = id)

    return render(request , "shenling/add.html",locals())




def adminupdt(request):
    id = request.GET.get("id")
    mmm = Shenling.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "shenling/admin/updt.html" , locals())




# 后台详情页面
def admindetail(request):
    id = request.GET.get("id")
    map = Shenling.objects.get(pk=id)
    return render(request , "shenling/admin/detail.html" , locals())



def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Shenling.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");

    post = request.POST.copy()
    data = {
        'juanzengid_id': utils.input(request,'juanzengid',utils.input(request,'juanzengid_id',0)),
        'bianhao': utils.input(request,'bianhao',''),
        'biaoti': utils.input(request,'biaoti',''),
        'wupin': utils.input(request,'wupin',''),
        'wupinleibie_id': utils.input(request,'wupinleibie',utils.input(request,'wupinleibie_id',0)),
        'shuliang': utils.input(request,'shuliang',''),
        'juanzengren': utils.input(request,'juanzengren',''),
        'shenlingrenxingming': utils.input(request,'shenlingrenxingming',''),
        'shenlingrenxingbie': utils.input(request,'shenlingrenxingbie',''),
        'shenlingrendianhua': utils.input(request,'shenlingrendianhua',''),
        'shenlingrendizhi': utils.input(request,'shenlingrendizhi',''),
        'shenqingmiaoshu': utils.input(request,'shenqingmiaoshu',''),
        'shenlingzhuangtai': utils.input(request,'shenlingzhuangtai',''),
        'shenqingyonghu': utils.input(request,'shenqingyonghu',''),

    }
    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])
    if data['juanzengren'] == '':
        data['juanzengren'] = utils.session(request, "username")
    if data['shenqingyonghu'] == '':
        data['shenqingyonghu'] = utils.session(request, "username")


    model = Shenling(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Shenling.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'juanzengid_id': utils.input(request,'juanzengid',utils.input(request,'juanzengid_id',0)),
        'bianhao': utils.input(request,'bianhao',old.bianhao),
        'biaoti': utils.input(request,'biaoti',old.biaoti),
        'wupin': utils.input(request,'wupin',old.wupin),
        'wupinleibie_id': utils.input(request,'wupinleibie',utils.input(request,'wupinleibie_id',0)),
        'shuliang': utils.input(request,'shuliang','').strip(),
        'juanzengren': utils.input(request,'juanzengren',old.juanzengren),
        'shenlingrenxingming': utils.input(request,'shenlingrenxingming',old.shenlingrenxingming),
        'shenlingrenxingbie': utils.input(request,'shenlingrenxingbie',old.shenlingrenxingbie),
        'shenlingrendianhua': utils.input(request,'shenlingrendianhua',old.shenlingrendianhua),
        'shenlingrendizhi': utils.input(request,'shenlingrendizhi',old.shenlingrendizhi),
        'shenqingmiaoshu': utils.input(request,'shenqingmiaoshu',old.shenqingmiaoshu),
        'shenlingzhuangtai': utils.input(request,'shenlingzhuangtai',old.shenlingzhuangtai),
        'shenqingyonghu': utils.input(request,'shenqingyonghu',old.shenqingyonghu),
        'addtime': old.addtime,

    }

    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])


    model = Shenling(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



