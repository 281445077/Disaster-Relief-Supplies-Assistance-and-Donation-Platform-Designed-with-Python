from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Xinwenxinxi
from common.utils import input
from common import utils,models as commonModels



from xinwenfenlei.models import Xinwenfenlei

# Create your views here.

def getWhere(request,qs):
    if request.GET.get("biaoti"):
        qs = qs.filter(biaoti__contains=request.GET.get("biaoti"))
    if request.GET.get("fenlei"):
        qs = qs.filter(fenlei=request.GET.get("fenlei"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Xinwenxinxi.objects)

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

    return render(request , "xinwenxinxi/admin/list.html" , locals() , )


# 前台列表页面
def index(request):
    qs = getWhere(request,Xinwenxinxi.objects)

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


    return render(request , "xinwenxinxi/index.html" , locals() , )


#后台添加页面
def adminadd(request):

    return render(request , "xinwenxinxi/admin/add.html",locals())






def adminupdt(request):
    id = request.GET.get("id")
    mmm = Xinwenxinxi.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "xinwenxinxi/admin/updt.html" , locals())




# 后台详情页面
def admindetail(request):
    id = request.GET.get("id")
    map = Xinwenxinxi.objects.get(pk=id)
    return render(request , "xinwenxinxi/admin/detail.html" , locals())

# 前台详情页面
def detail(request):
    id = request.GET.get("id")
    map = Xinwenxinxi.objects.get(pk=id)
    commonModels.execute("UPDATE xinwenxinxi SET dianjilv=dianjilv+1 WHERE id=%s" % (request.GET.get("id")))

    return render(request , "xinwenxinxi/detail.html" , locals())


def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Xinwenxinxi.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):

    post = request.POST.copy()
    data = {
        'biaoti': utils.input(request,'biaoti',''),
        'fenlei_id': utils.input(request,'fenlei',utils.input(request,'fenlei_id',0)),
        'tupian': utils.input(request,'tupian',''),
        'neirong': utils.input(request,'neirong',''),
        'tianjiaren': utils.input(request,'tianjiaren',''),
        'dianjilv': utils.input(request,'dianjilv',''),

    }
    if data['tianjiaren'] == '':
        data['tianjiaren'] = utils.session(request, "username")
    if data['dianjilv'] == '':
        data['dianjilv'] = 0
    else:
        data['dianjilv'] = int(data['dianjilv'])


    model = Xinwenxinxi(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Xinwenxinxi.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'biaoti': utils.input(request,'biaoti',old.biaoti),
        'fenlei_id': utils.input(request,'fenlei',utils.input(request,'fenlei_id',0)),
        'tupian': utils.input(request,'tupian',old.tupian),
        'neirong': utils.input(request,'neirong',old.neirong),
        'tianjiaren': utils.input(request,'tianjiaren',old.tianjiaren),
        'dianjilv': utils.input(request,'dianjilv','').strip(),
        'addtime': old.addtime,

    }

    if data['dianjilv'] == '':
        data['dianjilv'] = 0
    else:
        data['dianjilv'] = int(data['dianjilv'])


    model = Xinwenxinxi(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



