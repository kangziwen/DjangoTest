from django.shortcuts import render
import os

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

# 1
# def login(request):
#     return HttpResponse("hello world !")

# #2 HttpResponse 读取文件
# def login(request):
#     f = open('templates/login.html','r',encoding='utf-8')
#     data = f.read()
#     f.close()
#     return HttpResponse(data)

# 3
def login(request):
    print("request.method :",request.method)#POST
    error_msg = ""
    user = request.POST.get('username')
    pwd = request.POST.get('password')
    print(" ---",user,pwd)
    if user == 'root' and pwd =='123':
        # 去跳转到
        return redirect('/login')
    else:
        if request.method == 'POST':
            error_msg = "用户名或密码错误"

    return render(request,'login.html',{'error_msg':error_msg})

USER_LIST = [
    {'id': 1, 'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'id': 2, 'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {"id": 3, 'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]
def home(request):
    print(request.method,request.GET.get('nid'))
    if request.method == 'POST':
        u = request.POST.get('username')
        e = request.POST.get('email')
        g = request.POST.get('gender')
        zid=USER_LIST[len(USER_LIST)-1]["id"]+1
        print("u:%s e:%s g:%s"%(u,e,g))
        print("zid :",zid)
        temp = {'username':u,'email':e,'gender':g,"id":zid}
        USER_LIST.append(temp)

    return render(request, 'test/home.html', {'user_list':USER_LIST})

def kdelete(request):
    nid = request.GET.get('nid')

    for dic in USER_LIST:
        # print("dic :" ,dic ,nid)
        print("dic[id] ",dic['id'],nid)
        if int(dic['id']) == int(nid) :
            USER_LIST.remove(dic)
            print("nid ",nid)
            break
    print("USER_LIST ",USER_LIST)
    return redirect('/home')

# 上传文件
def upload(request):

    print("request.method : ",request.method)
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == "POST":
        g = request.POST.get("gender")
        print("g : ",g)
        f = request.POST.getlist('favor')
        print("f ",f)
        city = request.POST.getlist('city')
        print("city : ",city)
        # 上传文件的处理
        obj = request.FILES.get("fasong")
        print(obj,type(obj),obj.name)
        file_path = os.path.join('upload',obj.name)

        print("file_path : ",file_path)

        f = open(file_path,mode='wb')
        for i in obj.chunks():
            f.write(i)
        f.close()


        return render(request,'upload.html')

    else:
        return redirect('/login')

from django.views import View
class Home(View):
    def post(self,request):
        print(request.method)
        print(request.POST.get('can'))

        return render(request,"leihome.html")
    def get(self,request):
        print(request.method)
        print(request.GET.get('nid'))
        return render(request,"leihome.html")
    def dispatch(self, request, *args, **kwargs):
        print('before...')
        result = super(Home,self).dispatch(request,*args,**kwargs)
        print("after...")
        return result


# 模板迭代测试
# 1 迭代列表
ITER_LIST = [
    {'name':"kzw","age":18},
    {'name':'zhangsan','age':26},
    {'name':'lisi','age':20}
]

ITER_DIC={
    "key1":"value1",
    "key2": "value2",
    "key3": "value3",
    "key4": "value4",

}
ITER_DICTODIC = {
    "1": {'name':'kzw','age':15,'email':'123@qq.com'},
    "2": {'name': 'lisi', 'age': 16, 'email': '123@sina.com'},
    "3": {'name': 'wangwu', 'age': 32, 'email': '123@163.com'},
    "4": {'name': 'zhangsan', 'age': 24, 'email': '456@qq.com'}

}

def iter(request):
    return render(request,"iter.html",
                  {"iter_list":ITER_LIST,"iter_dic":ITER_DIC,"dictodic":ITER_DICTODIC})

# 正则,参数有顺序
def detail(request,nid,uid):
    print("detail : ",nid,uid)
    # from django.urls import reverse
    # v = reverse('detail',args=(90,80))
    # print("v : ",v)
    return render(request,"detail.html",{"d1":nid})

# nid,uid参数的顺序可以改变
def detailn(request,uid,nid):
    print("uid:%s nid : %s"%(uid,nid))
    return render(request,'detail.html',{"d2" : nid})

def othername(request,nid,uid):
    print(request.path_info)
    from django.urls import reverse
    # 拼接
    v = reverse("onamex",args=(90,80))
    v2 = reverse("onamex",kwargs={'nid':11,'uid':33})
    print("v : ",v)
    print("v2 : ",v2)
    return render(request,'iter.html')

