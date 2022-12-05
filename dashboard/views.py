from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from core.models import Tag, Category, Link


# Create your views here. 

def home(request):
    return render(request, 'dashboard/home.html')

@login_required
def users(request):
    try:
        users = User.objects.all()
        data = {
            'users':users
        }
        return render(request, 'dashboard/users.html',data)
    except:
        print('An exception occurred')

@login_required
def add_user(request): 
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        pass1 = request.POST['password']
        pass2 = request.POST['password_confirmation']

        if pass1 != pass2:
            msj = 'La contraseña tiene que ser igual'
            users = User.objects.all()
            data = {
                'users':users,
                'msj':msj
            }
            return render(request,'dashboard/users.html',data)
        else:
            save_data = User(username=username, email=email,first_name=first_name,last_name=last_name)
            save_data.save()
            messages.success(request,'usuario creado correctamente')
            users = User.objects.all()
            data = {
                'users':users
            }
            return render(request,'dashboard/users.html',data)   

@login_required
def posts(request):
    return render(request, 'dashboard/posts.html')

@login_required
def categories(request):
    try:
        categories = Category.objects.all()
        data = {
            'categories':categories
        }
        return render(request, 'dashboard/categories.html',data)
    except:
        print('An exception occurred')
    
    categories = Category.objects.all()
    data = {
        'categories':categories
    }
    return render(request, 'dashboard/categories.html',data)

@login_required
def add_category(request):
    if request.method == 'POST':
        name = request.POST['name']
        try:
            save_data = Category(name=name)
            save_data.save()
            messages.success(request,'Categoría creada correctamente')
            categories = Category.objects.all()
            data = {
                'categories':categories
            }
            return render(request,'dashboard/categories.html',data)
        except:
            messages.error(request,'La categoría ya se encuentra creada')
            categories = Category.objects.all()
            data = {
                'categories':categories
            }
            return render(request,'dashboard/categories.html',data)
    else:
        try:
            categories = Category.objects.all()
            data = {
                'categories':categories
            }
            return render(request,'dashboard/categories.html',data)
        except:
            messages.error(request,'Error al cargar las categorías')
            categories = Category.objects.all()
            data = {
                'categories':categories
            }
            return render(request,'dashboard/categories.html',data) 

@login_required
def tags(request):
    tags = Tag.objects.all()
    data = {
        'tags':tags
    }
    return render(request,'dashboard/tags.html',data)

@login_required
def add_tag(request):
    if request.method == 'POST':
        name = request.POST['name']

        try:
            save_data = Tag(name=name)
            save_data.save()

            tags = Tag.objects.all()
            data = {
                'tags':tags
            }
            return render(request,'dashboard/tags.html',data)
        except:
            tags = Tag.objects.all()
            data = {
                'tags':tags
            }
            return render(request,'dashboard/tags.html',data)
    else:
            
        try:
            tags = Tag.objects.all()
            data = {
                'tags':tags
            }
            return render(request,'dashboard/tags.html',data)
        except:        
            tags = Tag.objects.all()
            data = {
                'tags':tags
            }
            return render(request,'dashboard/tags.html',data)

@login_required
def rss(request):
    link = Link.objects.all()
    data = {
        'link':link
    }
    return render(request,'dashboard/rss.html',data)

@login_required
def add_rss(request):
    if request.method == 'POST':
        name = request.POST['name']
        key = request.POST['key']
        url = request.POST['url']
        icon = request.POST['icon']

        try:
            save_data = Link(name=name,key=key,url=url,icon=icon)
            save_data.save()

            link = Link.objects.all()
            data = {
                'link':link
            }
            return render(request,'dashboard/rss.html',data)
        except:
            link = Link.objects.all()
            data = {
                'link':link
            }
            return render(request,'dashboard/rss.html',data)
    else:
            
        try:
            link = Link.objects.all()
            data = {
                'link':link
            }
            return render(request,'dashboard/rss.html',data)
        except:        
            link = Link.objects.all()
            data = {
                'link':link
            }
            return render(request,'dashboard/rss.html',data)

@login_required
def user_profile(request):
    return render(request, 'dashboard/user_profile.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username,password=password)
        
        if user is None:
            data = {
                'msj': 'Usuario o contraseña incorrecta'
            }
            return render(request, 'dashboard/login.html',data)
        else:
            login(request, user)
            return redirect('user_profile')
    else:
        data = {
                'msj': ''
            }
        return render(request, 'dashboard/login.html',data)

def lockScreen(request,user_id):
    if request.method == 'POST':
        password = request.POST['password']
        passw = User.objects.values('password').filter(id=user_id)
        if passw is None:
            return redirect('signin')
        else:
            if make_password(password) == passw:
                return redirect('user_profile')
            else:
                data = {
                'msj':'Contraseña incorrecta'
                }
                return render(request, 'dashboard/lock_screen.html',data)    

    else:
        data = {
                'msj':''
            }
        return render(request, 'dashboard/lock_screen.html',data)

def signout(request):
    logout(request)
    return redirect('index')