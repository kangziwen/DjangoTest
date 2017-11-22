from django.shortcuts import render,redirect

from dbapp import models
# Create your views here.


def login(request):
    if request.method =='POST':
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