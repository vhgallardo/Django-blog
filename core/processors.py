from .models import About, Link, Category, Post, Tag

#ABOUT
def ctx_dic_about(request):
    ctx_about = {}
    ctx_about['ABOUT'] = About.objects.latest('created')

    return ctx_about
    # en el front se llama {{ ABOUT }}

#CATEGORIAS
def ctx_dic_category(request):
    ctx_category = {}
    ctx_category['categories'] = Category.objects.filter(active=True)

    return ctx_category

#TAGS
def ctx_dic_tag(request):
    ctx_tags = {}
    ctx_tags['tag'] = Tag.objects.filter(active=True)

    return ctx_tags

#ARCHIVOS
#RSS
def ctx_dic_link(request):
    ctx_link = {}
    links = Link.objects.all()

    for link in links:
        ctx_link[link.key] = {'url':link.url,'icon':link.icon}
    
    return ctx_link

def ctx_dic_history(request):
    ctx_history = {}
    ctx_history['dates'] = Post.objects.dates('created', 'month', order='DESC').distinct()
    return ctx_history
