from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Juanji
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
    if request.GET.get("wuliugongsi"):
        qs = qs.filter(wuliugongsi__contains=request.GET.get("wuliugongsi"))
    if request.GET.get("wuliudanhao"):
        qs = qs.filter(wuliudanhao__contains=request.GET.get("wuliudanhao"))
    if request.GET.get("juanjizhuangtai"):
        qs = qs.filter(juanjizhuangtai=request.GET.get("juanjizhuangtai"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Juanji.objects)

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

    return render(request , "juanji/admin/list.html" , locals() , )
# 捐赠人列表页面
def juanzengren(request):
    qs = getWhere(request,Juanji.objects)
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

    return render(request , "juanji/admin/juanzengren.html" , locals() , )




#后台添加页面
def adminadd(request):

    if 'id' in request.GET:
        id = request.GET.get('id')
        readMap = Juanzeng.objects.get(pk = id)
    return render(request , "juanji/admin/add.html",locals())






def adminupdt(request):
    id = request.GET.get("id")
    mmm = Juanji.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "juanji/admin/updt.html" , locals())




# 后台详情页面
def admindetail(request):
    id = request.GET.get("id")
    map = Juanji.objects.get(pk=id)
    return render(request , "juanji/admin/detail.html" , locals())



def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Juanji.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):

    post = request.POST.copy()
    data = {
        'juanzengid_id': utils.input(request,'juanzengid',utils.input(request,'juanzengid_id',0)),
        'bianhao': utils.input(request,'bianhao',''),
        'biaoti': utils.input(request,'biaoti',''),
        'wupin': utils.input(request,'wupin',''),
        'wupinleibie_id': utils.input(request,'wupinleibie',utils.input(request,'wupinleibie_id',0)),
        'shuliang': utils.input(request,'shuliang',''),
        'juanzengren': utils.input(request,'juanzengren',''),
        'wuliugongsi': utils.input(request,'wuliugongsi',''),
        'wuliudanhao': utils.input(request,'wuliudanhao',''),
        'beizhu': utils.input(request,'beizhu',''),
        'juanjizhuangtai': utils.input(request,'juanjizhuangtai',''),

    }
    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])
    if data['juanzengren'] == '':
        data['juanzengren'] = utils.session(request, "username")


    model = Juanji(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Juanji.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'juanzengid_id': utils.input(request,'juanzengid',utils.input(request,'juanzengid_id',0)),
        'bianhao': utils.input(request,'bianhao',old.bianhao),
        'biaoti': utils.input(request,'biaoti',old.biaoti),
        'wupin': utils.input(request,'wupin',old.wupin),
        'wupinleibie_id': utils.input(request,'wupinleibie',utils.input(request,'wupinleibie_id',0)),
        'shuliang': utils.input(request,'shuliang','').strip(),
        'juanzengren': utils.input(request,'juanzengren',old.juanzengren),
        'wuliugongsi': utils.input(request,'wuliugongsi',old.wuliugongsi),
        'wuliudanhao': utils.input(request,'wuliudanhao',old.wuliudanhao),
        'beizhu': utils.input(request,'beizhu',old.beizhu),
        'juanjizhuangtai': utils.input(request,'juanjizhuangtai',old.juanjizhuangtai),
        'addtime': old.addtime,

    }

    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])


    model = Juanji(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



