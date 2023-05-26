from django.shortcuts import render, HttpResponse, redirect
from app import models


#http://127.0.0.1:8000/login/ get
#http://127.0.0.1:8000/login/ post
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        #后台验收用户名密码以及合法性

    if username == 'root' and password == '123':
        #验证通过 跳转后台页面
        return redirect('/department/')
    else:
        #验证不通过
        return render(request, 'login.html', {"error": "用户名或密码错误"})


def department(request):
    #数据库获取数据
    #查询 Department 表所有
    # queryset=models.Department.objects.all()
    # queryset=models.Department.objects.all().order_by('id')
    queryset = models.Department.objects.all().order_by('-id')  #desc
    #数据渲染
    return render(request, 'department.html', {'queryset_lis': queryset})


def add_department(request):
    if request.method == 'GET':
        return render(request, 'add_department.html')
    else:
        title = request.POST.get('title')
        count = request.POST.get('count')
        models.Department.objects.create(title=title, count=count)
        return redirect('/department/')


def delete_department(request):
    depid = request.GET.get('id')
    models.Department.objects.filter(id=depid).delete()
    return redirect('/department/')
