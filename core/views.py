from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.paginator import Paginator
from django.http import HttpResponse
from .models import Post, Category, Comment, Newsletter
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from .forms import ContactForm

# Create your views here.
def index(request):
    posts_page = Paginator(Post.objects.filter(published=True), 2)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    title = 'Blog'
    total_pages = 'x' * posts.paginator.num_pages
    msj = ''  
    data = {
        'title':title,
        'posts':posts,
        'total_pages':total_pages,
        'msj':msj
    }
    return render(request, 'core/index.html',data)

def contact(request):
    title = 'Contacto'
    contact_form = ContactForm()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        html = render_to_string('emails/contactform.html',{
            'name':name,
            'email':email,
            'message':message
        })
        #print(request.POST)
        send_mail(request.POST['subject'],request.POST['message'],request.POST['email'],['vitoko.hgd@gmail.com'],html_message=html)
    data = {
        'title':title,
        'form':contact_form
    }
    return render(request, 'core/contact.html',data)

def detail(request, post_id):
    #post = Post.objects.get(id=post_id)
    title = 'Blog'
    if request.method == 'POST':
        comment = request.POST['comment']
        name = request.POST['name']
        email = request.POST['email']

        save_data = Comment(comment=comment, name=name,email=email,post_id=post_id)
        save_data.save()
    else:
        #try:
        post = get_object_or_404(Post, id=post_id)
        comments = Comment.objects.filter(post_id=post_id)
        return render(request, 'core/detail.html',{
        'title':title,
        'post':post,
        'comments':comments
        })
        #except:
            #return render(request, 'core/404.html')

def category(request, category_id):
    title = 'Blog'
    try:
        category = get_object_or_404(Category, id=category_id)
        #posts = Post.objects.filter(category=category_id)
        
        return render(request,'core/category.html',{
        'title' : title,
        'category': category,
        #'posts':posts,
    })
    except:
        return render(request, 'core/404.html')
    
    

def author(request, author_id):
    title = 'Blog'
    try:
        author = get_object_or_404(User, id=author_id)
        return render(request,'core/author.html',{
        'title' : title,
        'author': author
    })
    except:
        return render(request, 'core/404.html')
    

def dates(request, month_id, year_id):
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre',
    }

    if month_id > 12 or month_id < 1:
        return render(request, 'core/404.html')

    title = 'Blog'
    posts = Post.objects.filter(published=True, created__month=month_id, created__year=year_id)

    return render(request,'core/dates.html',{
        'title' : title,
        'posts':posts,
        'month':meses[month_id],
        'year':year_id
    })

def register(request):
    title = 'Registro'
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = make_password(request.POST['password'])

            save_data = User(password=password, username=username)
            save_data.save()            
            return redirect('signin') 
        else:
            return render(request,'core/register.html',{
            'title':title
            })
    except:
        error = 'Usuario ya se encuentra registrado'
        return render(request,'core/register.html',{
            'title':title,
            'error':error
            })

def newsletter(request):
    title = 'Blog'
    posts_page = Paginator(Post.objects.filter(published=True), 2)
    page = request.GET.get('page')
    posts = posts_page.get_page(page)
    total_pages = 'x' * posts.paginator.num_pages  
    try:
        if request.method == 'POST':
            email = request.POST['email']
            verify = Newsletter.objects.filter(email=email)
            print(verify)
            if verify:
                msj = 'El correo ya se encuentra registrado'
                return render(request, 'core/index.html',{
                    'title':title,
                    'msj':msj,
                    'posts':posts,
                    'total_pages':total_pages
                })
            else:
                save_data = Newsletter(email=email)
                save_data.save()
                msj = 'Suscrito correctamente'

                return render(request, 'core/index.html',{
                    'title':title,
                    'msj':msj,
                    'posts':posts,
                    'total_pages':total_pages
                })
        else:
            msj = ''
            return render(request, 'core/index.html',{
                    'title':title,
                    'msj':msj,
                    'posts':posts,
                    'total_pages':total_pages
                })
    except:
        msj = 'Error inesperado'
        return render(request, 'core/index.html',{
                    'title':title,
                    'msj':msj,
                    'posts':posts,
                    'total_pages':total_pages
                })
    