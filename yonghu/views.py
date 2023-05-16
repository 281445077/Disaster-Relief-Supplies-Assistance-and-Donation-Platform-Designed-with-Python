from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from .models import Yonghu
from common.utils import input
from common import utils,models as commonModels




# Create your views here.

def getWhere(request,qs):
    if request.GET.get("yonghuming"):
        qs = qs.filter(yonghuming__contains=request.GET.get("yonghuming"))




    orderby = input(request, "order", "id")
    sort = input(request, "sort", "DESC").upper()
    if sort == "DESC":
        qs = qs.order_by("-" + orderby)
    else:
        qs = qs.order_by(orderby)

    return qs


# 管理员列表页面
def adminlist(request):
    qs = getWhere(request,Yonghu.objects)

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

    return render(request , "yonghu/admin/list.html" , locals() , )




#后台添加页面
def adminadd(request):

    return render(request , "yonghu/admin/add.html",locals())


# 前台添加页面
def add(request):



    return render(request , "yonghu/add.html",locals())




def adminupdt(request):
    id = request.GET.get("id")
    mmm = Yonghu.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")


    return render(request, "yonghu/admin/updt.html" , locals())


def adminupdtself(request):
    id = request.session['id']
    mmm = Yonghu.objects.get(pk = id)
    if mmm == None:
        return utils.showError(request,"没有找到相关数据")

    return render(request, "yonghu/admin/updtself.html" , locals())





def delete(request):
    ids = request.GET.getlist("id")

    for id in ids:
        map = Yonghu.objects.get(pk = id)

        map.delete()

    return utils.showSuccess(request,"删除成功")


    return utils.showSuccess(request,"批量处理成功")

def insert(request):

    post = request.POST.copy()
    data = {
        'yonghuming': utils.input(request,'yonghuming',''),
        'mima': utils.input(request,'mima',''),
        'xingming': utils.input(request,'xingming',''),
        'nicheng': utils.input(request,'nicheng',''),
        'xingbie': utils.input(request,'xingbie',''),
        'shoujihao': utils.input(request,'shoujihao',''),
        'youxiang': utils.input(request,'youxiang',''),
        'shenfenzheng': utils.input(request,'shenfenzheng',''),
        'dizhi': utils.input(request,'dizhi',''),
        'aixinjifen': utils.input(request,'aixinjifen',''),

    }
    if data['aixinjifen'] == '':
        data['aixinjifen'] = 0
    else:
        data['aixinjifen'] = float(data['aixinjifen'])


    model = Yonghu(**data)
    model.save(force_insert = True)

    referer = utils.input(request,"referer" , request.headers.get('referer'))

    return utils.showSuccess(request , "添加成功" , referer)

def update(request):
    charuid = request.POST.get('id')
    post = request.POST.copy()
    old = Yonghu.objects.get(pk = charuid)
    data = {
        'id': charuid,
        'yonghuming': utils.input(request,'yonghuming',old.yonghuming),
        'mima': utils.input(request,'mima',old.mima),
        'xingming': utils.input(request,'xingming',old.xingming),
        'nicheng': utils.input(request,'nicheng',old.nicheng),
        'xingbie': utils.input(request,'xingbie',old.xingbie),
        'shoujihao': utils.input(request,'shoujihao',old.shoujihao),
        'youxiang': utils.input(request,'youxiang',old.youxiang),
        'shenfenzheng': utils.input(request,'shenfenzheng',old.shenfenzheng),
        'dizhi': utils.input(request,'dizhi',old.dizhi),
        'aixinjifen': utils.input(request,'aixinjifen','').strip(),

    }

    if data['aixinjifen'] == '':
        data['aixinjifen'] = 0
    else:
        data['aixinjifen'] = float(data['aixinjifen'])


    model = Yonghu(**data)
    model.save(force_update = True)

    referer = utils.input(request , "referer" , request.headers.get('referer'))
    return utils.showSuccess(request , "修改成功" , referer)



