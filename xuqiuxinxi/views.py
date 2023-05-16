from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Xuqiuxinxi
from common.utils import input
from common import utils,models as commonModels



from wupinleibie.models import Wupinleibie

# Create your views here.

def getWhere(request,qs):
    if request.GET.get("xuqiubianhao"):
        qs = qs.filter(xuqiubianhao__contains=request.GET.get("xuqiubianhao"))
    if request.GET.get("biaoti"):
        qs = qs.filter(biaoti__contains=request.GET.get("biaoti"))
    if request.GET.get("wuzhimingcheng"):
        qs = qs.filter(wuzhimingcheng__contains=request.GET.get("wuzhimingcheng"))
    if request.GET.get("wuzhileibie"):
        qs = qs.filter(wuzhileibie=request.GET.get("wuzhileibie"))
    if request.GET.get("zhuangtai"):
        qs = qs.filter(zhuangtai=request.GET.get("zhuangtai"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Xuqiuxinxi.objects)

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

    return render(request , "xuqiuxinxi/admin/list.html" , locals() , )
# 登记人列表页面
def dengjiren(request):
    qs = getWhere(request,Xuqiuxinxi.objects)
    qs = qs.filter(dengjiren=request.session['username'])

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

    return render(request , "xuqiuxinxi/admin/dengjiren.html" , locals() , )


# 前台列表页面
def index(request):
    qs = getWhere(request,Xuqiuxinxi.objects)

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


    return render(request , "xuqiuxinxi/index.html" , locals() , )


#后台添加页面
def adminadd(request):

    return render(request , "xuqiuxinxi/admin/add.html",locals())


# 前台添加页面
def add(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");



    return render(request , "xuqiuxinxi/add.html",locals())




def adminupdt(request):
    id = request.GET.get("id")
    mmm = Xuqiuxinxi.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "xuqiuxinxi/admin/updt.html" , locals())




# 后台详情页面
def admindetail(request):
    id = request.GET.get("id")
    map = Xuqiuxinxi.objects.get(pk=id)
    return render(request , "xuqiuxinxi/admin/detail.html" , locals())

# 前台详情页面
def detail(request):
    id = request.GET.get("id")
    map = Xuqiuxinxi.objects.get(pk=id)


    return render(request , "xuqiuxinxi/detail.html" , locals())


def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Xuqiuxinxi.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):
    if not utils.checkLogin(request):
        return utils.showError(request,"请登录后操作");

    post = request.POST.copy()
    data = {
        'xuqiubianhao': utils.input(request,'xuqiubianhao',''),
        'biaoti': utils.input(request,'biaoti',''),
        'wuzhimingcheng': utils.input(request,'wuzhimingcheng',''),
        'wuzhileibie_id': utils.input(request,'wuzhileibie',utils.input(request,'wuzhileibie_id',0)),
        'shuliang': utils.input(request,'shuliang',''),
        'xingming': utils.input(request,'xingming',''),
        'shoujihao': utils.input(request,'shoujihao',''),
        'lianxidizhi': utils.input(request,'lianxidizhi',''),
        'xuqiumiaoshu': utils.input(request,'xuqiumiaoshu',''),
        'zhuangtai': utils.input(request,'zhuangtai',''),
        'dengjiren': utils.input(request,'dengjiren',''),

    }
    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])
    if data['dengjiren'] == '':
        data['dengjiren'] = utils.session(request, "username")


    model = Xuqiuxinxi(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Xuqiuxinxi.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'xuqiubianhao': utils.input(request,'xuqiubianhao',old.xuqiubianhao),
        'biaoti': utils.input(request,'biaoti',old.biaoti),
        'wuzhimingcheng': utils.input(request,'wuzhimingcheng',old.wuzhimingcheng),
        'wuzhileibie_id': utils.input(request,'wuzhileibie',utils.input(request,'wuzhileibie_id',0)),
        'shuliang': utils.input(request,'shuliang','').strip(),
        'xingming': utils.input(request,'xingming',old.xingming),
        'shoujihao': utils.input(request,'shoujihao',old.shoujihao),
        'lianxidizhi': utils.input(request,'lianxidizhi',old.lianxidizhi),
        'xuqiumiaoshu': utils.input(request,'xuqiumiaoshu',old.xuqiumiaoshu),
        'zhuangtai': utils.input(request,'zhuangtai',old.zhuangtai),
        'dengjiren': utils.input(request,'dengjiren',old.dengjiren),
        'addtime': old.addtime,

    }

    if data['shuliang'] == '':
        data['shuliang'] = 0
    else:
        data['shuliang'] = int(data['shuliang'])


    model = Xuqiuxinxi(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



