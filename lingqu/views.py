from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Lingqu
from common.utils import input
from common import utils,models as commonModels


from juanzengwuzi.models import Juanzengwuzi

# Create your views here.


def getWhere(request,qs):
    if request.GET.get("juanzengwuziid"):
        qs = qs.filter(juanzengwuziid=request.GET.get("juanzengwuziid"))
    if request.GET.get("xuqiubianhao"):
        qs = qs.filter(xuqiubianhao__contains=request.GET.get("xuqiubianhao"))
    if request.GET.get("biaoti"):
        qs = qs.filter(biaoti__contains=request.GET.get("biaoti"))
    if request.GET.get("juanzengwuzhi"):
        qs = qs.filter(juanzengwuzhi__contains=request.GET.get("juanzengwuzhi"))
    if request.GET.get("juanzengshuliang_start"):
        qs = qs.filter(juanzengshuliang__lte=request.GET.get("juanzengshuliang_start"))

    if request.GET.get("juanzengshuliang_end"):
        qs = qs.filter(juanzengshuliang__gte=request.GET.get("juanzengshuliang_start"))

    if request.GET.get("lingqubeizhu"):
        qs = qs.filter(lingqubeizhu__contains=request.GET.get("lingqubeizhu"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Lingqu.objects)

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

    return render(request , "lingqu/admin/list.html" , locals() , )
# 捐赠用户列表页面
def juanzengyonghu(request):
    qs = getWhere(request,Lingqu.objects)
    qs = qs.filter(juanzengyonghu=request.session['username'])

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

    return render(request , "lingqu/admin/juanzengyonghu.html" , locals() , )
# 登记人列表页面
def dengjiren(request):
    qs = getWhere(request,Lingqu.objects)
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

    return render(request , "lingqu/admin/dengjiren.html" , locals() , )




#后台添加页面
def adminadd(request):

    if 'id' in request.GET:
        id = request.GET.get('id')
        readMap = Juanzengwuzi.objects.get(pk = id)
    return render(request , "lingqu/admin/add.html",locals())






def adminupdt(request):
    id = request.GET.get("id")
    mmm = Lingqu.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "lingqu/admin/updt.html" , locals())




# 后台详情页面
def admindetail(request):
    id = request.GET.get("id")
    map = Lingqu.objects.get(pk=id)
    return render(request , "lingqu/admin/detail.html" , locals())



def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Lingqu.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):

    post = request.POST.copy()
    data = {
        'juanzengwuziid_id': utils.input(request,'juanzengwuziid',utils.input(request,'juanzengwuziid_id',0)),
        'xuqiuxinxiid_id': utils.input(request,'xuqiuxinxiid',utils.input(request,'xuqiuxinxiid_id',0)),
        'xuqiubianhao': utils.input(request,'xuqiubianhao',''),
        'biaoti': utils.input(request,'biaoti',''),
        'juanzengwuzhi': utils.input(request,'juanzengwuzhi',''),
        'juanzengshuliang': utils.input(request,'juanzengshuliang',''),
        'juanzengyonghu': utils.input(request,'juanzengyonghu',''),
        'dengjiren': utils.input(request,'dengjiren',''),
        'lingqubeizhu': utils.input(request,'lingqubeizhu',''),

    }
    if data['juanzengshuliang'] == '':
        data['juanzengshuliang'] = 0
    else:
        data['juanzengshuliang'] = int(data['juanzengshuliang'])
    if data['juanzengyonghu'] == '':
        data['juanzengyonghu'] = utils.session(request, "username")
    if data['dengjiren'] == '':
        data['dengjiren'] = utils.session(request, "username")


    model = Lingqu(**data)
    model.save(force_insert = True)

    try:
        commonModels.execute("update xuqiuxinxi set zhuangtai='已领取' where xuqiubianhao='%s'" % (request.POST.get("xuqiubianhao")))
        commonModels.execute("update juanzengwuzi set juanzengzhuangtai='已领取' where id='%s'" % (request.POST.get("juanzengwuziid")))
    except Exception as e:
        print("%s"% (e))

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Lingqu.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'juanzengwuziid_id': utils.input(request,'juanzengwuziid',utils.input(request,'juanzengwuziid_id',0)),
        'xuqiuxinxiid_id': utils.input(request,'xuqiuxinxiid',utils.input(request,'xuqiuxinxiid_id',0)),
        'xuqiubianhao': utils.input(request,'xuqiubianhao',old.xuqiubianhao),
        'biaoti': utils.input(request,'biaoti',old.biaoti),
        'juanzengwuzhi': utils.input(request,'juanzengwuzhi',old.juanzengwuzhi),
        'juanzengshuliang': utils.input(request,'juanzengshuliang','').strip(),
        'juanzengyonghu': utils.input(request,'juanzengyonghu',old.juanzengyonghu),
        'dengjiren': utils.input(request,'dengjiren',old.dengjiren),
        'lingqubeizhu': utils.input(request,'lingqubeizhu',old.lingqubeizhu),
        'addtime': old.addtime,

    }

    if data['juanzengshuliang'] == '':
        data['juanzengshuliang'] = 0
    else:
        data['juanzengshuliang'] = int(data['juanzengshuliang'])


    model = Lingqu(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



