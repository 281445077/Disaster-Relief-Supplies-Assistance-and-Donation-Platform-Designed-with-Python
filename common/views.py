import os
import uuid

from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime
import random
import json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from . import utils,models as commonModels
from urllib.parse import urljoin






def index(request):

    return render(request , 'index.html' , locals())


def sh(request):
    tablename = utils.input(request , "tablename" , "")
    yuan = utils.input(request , "yuan" , "")
    id = int(utils.input(request , "id" , 0))

    if yuan == "否" or yuan == "":
        sql = "UPDATE %s SET issh='是' WHERE id='%s' " %(tablename,id,)
    else:
        sql = "UPDATE %s SET issh='否' WHERE id='%s' " %(tablename,id,)

    commonModels.execute(sql)

    return utils.showSuccess(request , "审核成功" if yuan == '否' or not yuan else '已取消审核')

# 系统登录
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        cx       = request.POST.get('cx')

        if "a" in request.GET:
            pagerandom = request.POST.get('pagerandom')
            captcha = request.session["captchaCode"]
            if not pagerandom:
                return utils.showError(request, "请填写验证码")
            if pagerandom != captcha:
                return utils.showError(request , "验证码错误")

        if not username:
            return utils.showError(request, "请填写账号")
        if not password:
            return utils.showError(request, "请填写密码")
        if not cx:
            return utils.showError(request, "请选择相应角色")
        qs = None
        if cx == '管理员':
            from admins.models import Admins
            
            qs = Admins.objects.filter(username=username , pwd=password)
        if cx == '用户':
            from yonghu.models import Yonghu
            
            qs = Yonghu.objects.filter(yonghuming=username , mima=password)

        if qs is None:
            return utils.showError(request,'没有找到相关角色')

        list = qs.values()

        if not list:
            return utils.showError(request,"账号或密码错误")

        user = list[0]
        request.session['cx'] = cx
        request.session['login'] = cx
        request.session['username'] = username

        for key,value in user.items():
            request.session[key] = str(value)

        if 'referer' in request.POST:
            referer = request.POST.get('referer')
        else:
            referer = '/main'

        return utils.showSuccess(request,"登录成功" , referer)
    else:
        # 访问页面
        return render(request,'login.html' , locals())

# 生成验证码
# https://www.cnblogs.com/3one/p/8461306.html  参考这个网站做得一个函数
def captcha(request):
    img , strs=utils.create_validate_code(size=(120 , 30))
    request.session["captchaCode"] = strs
    from io import BytesIO
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    print("验证码值：%s" % (strs,))

    return HttpResponse(data, content_type='image/png')



# 退出登录
def logout(request):
    request.session.flush()
    return redirect('/')

# 管理后台主页面
def main(request):
    return render(request,'main.html')




def adminsy(request):

    return render(request , 'sy.html' , locals())





def createUUID():
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS , str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))))
    return ''.join(uid.split('-'))

# Create your views here.
def get_path_format_vars():
    return {
        "year": datetime.datetime.now().strftime("%Y"),
        "month": datetime.datetime.now().strftime("%m"),
        "day": datetime.datetime.now().strftime("%d"),
        "date": datetime.datetime.now().strftime("%Y%m%d"),
        "time": datetime.datetime.now().strftime("%H%M%S"),
        "datetime": datetime.datetime.now().strftime("%Y%m%d%H%M%S"),
        "uuid":createUUID(),
        "rnd": random.randrange(1000, 9999)
    }


def upload(request):
    """获取ueditor的后端URL地址"""
    return render(request , 'upload/upload.html' , )


def get_output_path(request, path_format_var):
    # 取得输出文件的路径
    OutputPathFormat = ("%(uuid)s%(rnd)s.%(extname)s" % path_format_var).replace("\\", "/")
    # 分解OutputPathFormat
    OutputPath, OutputFile = os.path.split(OutputPathFormat)
    OutputPath = os.path.join(settings.MEDIA_ROOT, OutputPath)
    # 如果OutputFile为空说明传入的OutputPathFormat没有包含文件名，因此需要用默认的文件名

    if not os.path.exists(OutputPath):
        os.makedirs(OutputPath)
    return (OutputPathFormat, OutputPath, OutputFile)



def UploadFile(request):
    """上传文件"""
    if not request.method == "POST":
        return HttpResponse(json.dumps({'state':'ERROR'}), content_type="application/javascript")

    state = "SUCCESS"
    # 上传文件

    UploadFieldName = 'upfile'

    # 取得上传的文件
    file = request.FILES.get(UploadFieldName, None)
    if file is None:
        return HttpResponse(json.dumps({'state':'ERROR'}), content_type="application/javascript")
    upload_file_name = file.name
    upload_file_size = file.size

    # 取得上传的文件的原始名称
    upload_original_name, upload_original_ext = os.path.splitext(
        upload_file_name)

    # 大小检验
    # max_size = 1024 * 1024 * 1024 * 1024 * 10
    #
    # if upload_file_size > max_size:
    #     state = u"上传文件大小不允许超过%s。" % max_size

    path_format_var = get_path_format_vars()
    path_format_var.update({
        "basename": upload_original_name,
        "extname": upload_original_ext[1:],
        "filename": upload_file_name,
    })
    # 取得输出文件的路径
    OutputPathFormat, OutputPath, OutputFile = get_output_path(request,  path_format_var)

    # 所有检测完成后写入文件
    if state == "SUCCESS":
        state = save_upload_file(
            file, os.path.join(OutputPath, OutputFile))

    # 返回数据
    return_info = {
        # 保存后的文件名称
        'url': urljoin(settings.MEDIA_URL, OutputPathFormat),
        'original': upload_file_name,  # 原始文件名
        'type': upload_original_ext,
        'state': state,  # 上传状态，成功时返回SUCCESS,其他任何值将原样返回至图片上传框中
        'size': upload_file_size
    }
    return HttpResponse(json.dumps(return_info, ensure_ascii=False), content_type="application/javascript")


def save_upload_file(PostFile, FilePath):
    try:
        f = open(FilePath, 'wb')
        for chunk in PostFile.chunks():
            f.write(chunk)
    except Exception as E:
        f.close()
        return u"写入文件错误: {}".format(E.message)
    f.close()
    return u"SUCCESS"




# 检测数据库中表得数据是否存在
def checkno(request):
    table = utils.input(request,'table')
    col = utils.input(request,"col")
    checktype = utils.input(request,"checktype")
    value = utils.input(request,col)

    sql = "SELECT COUNT(*) count,'1' as id FROM %s WHERE %s='%s' " % ( table , col , value , )

    if checktype == "update":
        id = utils.input(request,"id")
        sql += " AND id!=%s " % ( id ,  )

    d = commonModels.find(sql)

    count = d['count']

    if count:
        return HttpResponse('false')
    else:
        return HttpResponse('true')


def mod(request):
    if request.method == 'POST':
        oldPwd = request.POST.get("oldPwd" , "")
        newPwd = request.POST.get("newPwd" , "")
        newPwd2 = request.POST.get("newPwd2" , "")

        if not all([oldPwd,newPwd2,newPwd]):
            return utils.showError(request , "请填写原密码或新密码或确认密码")

        if newPwd != newPwd2:
            return utils.showError(request , "两次输入密码错误")
        cx  = request.session["login"]
        username = request.session["username"]
        qs = None
        mimafield = ''

        if cx == '管理员':
            from admins.models import Admins
                        
            qs = Admins.objects.filter(username=username , pwd=oldPwd)
            mimafield = 'pwd'
        if cx == '用户':
            from yonghu.models import Yonghu
                        
            qs = Yonghu.objects.filter(yonghuming=username , mima=oldPwd)
            mimafield = 'mima'


        if qs is None:
            return utils.showError(request , "没有该用户")

        values = qs.all()
        if not len(values):
            return utils.showError(request , "原密码错误")

        user = values[0]
        setattr(user , mimafield , newPwd)
        user.save()
        return utils.showSuccess(request,"密码修改成功" , "/common/mod/")
    else:
        return render(request , 'mod.html')





def selectUpdateSearch(request):
    import json
    where = json.loads(request.POST.get('where'))
    table = request.POST.get('table')
    className = utils.parseName(table)
    fromName = table+'.models'
    model = utils.imports(fromName , className)
    if model is None:
        return HttpResponse('Error' , status=500)

    qs = model.objects
    pagesize = 50

    for key,value in where.items():
        if key == 'limit':
            pagesize = int(value)
        else:
            if isinstance(value , str):
                filters = {}
                filters[key] = value
                qs = qs.filter(**filters)
            else:
                exp = value[0]
                val = value[1]
                if exp == '>':
                    exp = 'gt'
                elif exp == '>=':
                    exp = 'gte'
                elif exp == '<':
                    exp = 'lt'
                elif exp == '<=':
                    exp ='lte'
                elif exp == 'like':
                    exp = 'icontains'
                else:
                    exp = ''

                if exp == '':
                    zd = {}
                    zd[key] = val
                    qs = qs.filter(**zd)
                else:
                    field = key + '__' + exp
                    zd = {}
                    zd[field] = val
                    qs = qs.filter(**zd)
    pass
    lists = list(qs.values()[0:pagesize])

    print(lists)
    return HttpResponse(json.dumps(lists,cls=utils.DecimalEncoder))

