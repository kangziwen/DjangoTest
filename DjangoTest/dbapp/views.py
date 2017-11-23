from django.shortcuts import render,redirect

from dbapp import models
# Create your views here.


def user_info(request):
    if request.method == 'GET':
        user_list = models.UserInfo.objects.all()

        group_list = models.UserGroup.objects.all()

        return render(request,'user_info.html',{'user_list':user_list,'group_list':group_list})
    elif request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')

        models.UserInfo.objects.create(username=u,password=p)
        return redirect('dbapp/user_info/')

    else:
        pass

def user_detail(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    return render(request,'user_detail.html',{'obj':obj})

def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/dbapp/user_info/')

def user_edit(request,nid):
    print("user_edit :",request.method)
    if request.method == "GET":
        obj = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj})
    elif request.method == 'POST':
        nid = request.POST.get('id')
        u = request.POST.get('username')
        p = request.POST.get('password')
        # models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        obj = models.UserInfo.objects.filter(id=nid).first()
        obj.username = u
        obj.password = p
        obj.save()

        print("path_info : ",request.path_info)
        # 跳转错误，跳转到 dbapp/useredit-3/dbapp/login/ 连接
        return redirect('dbapp/login/')
        # return render(request,'user_info.html')
def orm(request):

    models.UserInfo.objects.create(username='root',password='123')

    dic = {'username':'eric','password':'666'}
    models.UserInfo.objects.create(**dic)

    obj = models.UserInfo(username='hehe',password='321')
    obj.save()

    # 查
    r = models.UserInfo.objects.all()
    r= models.UserInfo.objects.filter(username='root',password='1234')

    for row in r:
        print(row.id,row.username)

    # 删
    models.UserInfo.objects.filter(username='hehe').delete()
    # 更新
    models.UserInfo.objects.filter(id=2).update()

    models.UserInfo.objects.create(
        username='r1',
        password='456',
        email='123@qq.com',
        test='abcd',
        user_group = models.UserInfo.objects.filter(id=1).first()
    )

    models.UserInfo.objects.create(
        username='r2',
        password='654',
        email='456@163.com',
        test='dcba',
        user_group_id=1

    )


def index(request):
    return render(request,"dbindex.html")

def login(request):
    if request.method == 'POST':
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        # 先查询，有就登录没有直接注册
        obj = models.UserInfo.objects.filter(username=u).first()
        # print("obj :",obj.password)
        t = 0
        if obj:
            if obj.password == p:
                # 登录成功
                t = 1
            else:
                # 密码错误
                t=3
        else:
            # 插入数据
            o = models.UserInfo.objects.create(username=u,password=p)
            # # 方法二
            # dic = {"username":u,"password":p}
            # o = models.UserInfo.objects.create(**dic)
            # # 方法三
            # obj = models.UserInfo(username=u,password=p)
            # obj.save()
            if o :
                t=2


        return  render(request,'dblogin.html',{"name":u,"state":t})
    elif request.method == 'GET':
        return  render(request,'dblogin.html')

    else:
        return redirect('/db/login')


   # return render(request,'dblogin.html')