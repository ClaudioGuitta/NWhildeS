from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *
import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.contrib import messages
from django.core.paginator import Paginator

from .forms import *


####################  Views   #########################



def post_list(request):                    ## modelo em função
    editar_nav = Editar_nav_blog.objects.get(pk=1)
    sobre_mim = SobreMim.objects.get(pk=1)

    search = request.GET.get('search')
    filter = request.GET.get('filter')

    ultimas_postagens = Post.objects.all().order_by('-created_date')

    if search:
        posts_list = Post.objects.filter(title__icontains=search)
        paginator = Paginator(posts_list, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        ultimas = Post.objects.all().order_by('-created_date')
        paginator2 = Paginator(ultimas,3)
        page2 = request.GET.get('page')
        ultimas_postagens = paginator2.get_page(page2)


    elif filter:
        posts_list = Post.objects.filter(tipo=filter).order_by('-created_date')
        paginator = Paginator(posts_list, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        ultimas = Post.objects.all().order_by('-created_date')
        paginator2 = Paginator(ultimas,3)
        page2 = request.GET.get('page')
        ultimas_postagens = paginator2.get_page(page2)

    else:

        posts_list = Post.objects.all().order_by('-created_date')
        paginator = Paginator(posts_list, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        ultimas = Post.objects.all().order_by('-created_date')
        paginator2 = Paginator(ultimas,3)
        page2 = request.GET.get('page')
        ultimas_postagens = paginator2.get_page(page2)


    return render(request, 'blog/post_list.html', {'posts': posts, 'editar_nav': editar_nav, 'sobre_mim': sobre_mim, 'ultimas_postagens':ultimas_postagens})



def sobre_mim_detail(request):
    sobre_detail = SobreMim.objects.get(pk=1)
    editar_nav = Editar_nav_blog.objects.get(pk=1)
    return render(request, 'blog/sobre_mim.html', {'sobre_detail':sobre_detail,'editar_nav': editar_nav})





def post_mostrar(request, id):

    editar_nav = Editar_nav_blog.objects.get(pk=1)
    sobre_mim = SobreMim.objects.get(pk=1)

    search = request.GET.get('search')
    if search:
        posts = Post.objects.filter(title__icontains=search)

        ultimas = Post.objects.all().order_by('-created_date')
        paginator2 = Paginator(ultimas,3)
        page2 = request.GET.get('page')
        ultimas_postagens = paginator2.get_page(page2)

        return render(request, 'blog/post_list.html', {'editar_nav': editar_nav,'sobre_mim': sobre_mim,'posts': posts})
    else:

        ultimas = Post.objects.all().order_by('-created_date')
        paginator2 = Paginator(ultimas,3)
        page2 = request.GET.get('page')
        ultimas_postagens = paginator2.get_page(page2)

        mostrar = Post.objects.get(pk=id)

        form = FaleComigoForm(request.POST)

        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('post_list')
            else:
                form = FaleComigoForm()

        return render(request, 'blog/post.html', {'mostrar': mostrar, 'editar_nav': editar_nav,'sobre_mim': sobre_mim,'form': form,'ultimas_postagens':ultimas_postagens})


class testeListView(ListView):
    model = teste
    model = Post
    template_name = 'blog/teste.html'
    context_object_name = 'Tnome', 'posts'


'''
@login_required
def FaleComigoFormulario(request):
    form = FaleComigoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_admin')
    else:
        form = FaleComigoForm()
    return render(request, 'blog/user_pergunta.html',{'form':form})
'''

def index_home(request):
    editar_nav = Editar_nav_blog.objects.get(pk=1)
    sobre_mim = SobreMim.objects.get(pk=1)
    s_imagens = MeuBlog.objects.all()

    form = FaleComigoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index_home')
        else:
            form = FaleComigoForm()
    return render(request, 'blog/home.html', {'editar_nav':editar_nav, 'sobre_mim':sobre_mim, 'form':form,'s_imagens':s_imagens})

def manutencao_de_computador(request):
    mostrar_servico = ServicoManutencao.objects.all().order_by('valor')
    editar_nav = Editar_nav_blog.objects.get(pk=1)
    sobre_mim = SobreMim.objects.get(pk=1)
    return render(request, 'blog/manutencao.html', {'mostrar_servico':mostrar_servico, 'editar_nav':editar_nav,'sobre_mim':sobre_mim})




###########################   Administração do Site  ######################
@login_required()
def index_admin(request):

    return render(request, 'blog/admin/index_admin.html')


##########  VIEWS LISTAR   #############

@login_required()
def list_Editar_nav_blog(request):
    listar_editar_nav_blog = Editar_nav_blog.objects.all()
    return render(request, 'blog/admin/list_Editar_nav_blog.html',{'listar_editar_nav_blog':listar_editar_nav_blog,})


@login_required()
def list_FaleComigo(request):
    listar_FaleComigo = FaleComigo.objects.all()
    return render(request, 'blog/admin/list_FaleComigo.html',{'listar_FaleComigo':listar_FaleComigo})

@login_required()
def list_MeuBlog(request):
    listar_MeuBlog = MeuBlog.objects.all()
    return render(request, 'blog/admin/list_MeuBlog.html',{'listar_MeuBlog':listar_MeuBlog})

@login_required()
def list_Post(request):
    listar_post = Post.objects.all().order_by('-created_date').filter(autor=request.user)
    return render(request, 'blog/admin/list_Post.html',{'listar_post':listar_post})


@login_required()
def list_SobreMim(request):
    listar_SobreMim = SobreMim.objects.all()
    return render(request, 'blog/admin/list_SobreMim.html',{'listar_SobreMim':listar_SobreMim})


@login_required()
def list_ServicoManutencao(request):
    listar_ServicoManutencao = ServicoManutencao.objects.all().order_by('valor')
    return render(request, 'blog/admin/list_ServicoManutencao.html',{'listar_ServicoManutencao':listar_ServicoManutencao})




# VIEWS UPDATE

@login_required()
def update_Editar_nav_blog(request,id):
    update_nav = get_object_or_404(Editar_nav_blog,pk=id)
    form = UpdateNavForm(request.POST or None,request.FILES or None, instance=update_nav)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('list_Editar_nav_blog')
            messages.success(request, "You successfully updated the post")
        else:
            form = UpdateNavForm(request.POST or None,request.FILES or None, instance=update_nav)

    return render(request, 'blog/admin/update_nav.html',{'form':form})

@login_required()
def UpdateMeuBlog(request,id):
    update_MeuBlog = get_object_or_404(MeuBlog,pk=id)
    form = UpdateMeuBlogForm(request.POST or None, request.FILES or None, instance=update_MeuBlog)

    if form.is_valid():
        form.save()
        return redirect('list_MeuBlog')
    else:
        form = UpdateMeuBlogForm(request.POST or None, request.FILES or None, instance=update_MeuBlog)
    return render(request, 'blog/admin/update_MeuBlog.html', {'form':form})


@login_required()
def UpdatePost(request,id):
    update_Post = get_object_or_404(Post,pk=id)
    form = UpdatePostForm(request.POST or None, request.FILES or None, instance=update_Post)

    if form.is_valid():
        post = form.save(commit=False)
        post.autor = request.user
        post.save()
        return redirect('list_Post')
    else:
        form = UpdatePostForm(request.POST or None, request.FILES or None, instance=update_Post)
    return render(request, 'blog/admin/update_post.html', {'form':form})


@login_required()
def UpdateSobreMim(request,id):
    update_SobreMim = get_object_or_404(SobreMim,pk=id)
    form = UpdateSobreMimForm(request.POST or None, request.FILES or None, instance=update_SobreMim)

    if form.is_valid():
        form.save()
        return redirect('list_SobreMim')
    else:
        form = UpdateSobreMimForm(request.POST or None, request.FILES or None, instance=update_SobreMim)
    return render(request, 'blog/admin/update_SobreMim.html', {'form':form})

@login_required()
def UpdateServicoManutencao(request,id):
    update_ServicoManutencao = get_object_or_404(ServicoManutencao,pk=id)
    form = UpdateServicoManutencaoForm(request.POST or None,instance=update_ServicoManutencao)

    if form.is_valid():
        form.save()
        return redirect('list_ServicoManutencao')
    else:
        form = UpdateServicoManutencaoForm(request.POST or None, instance=update_ServicoManutencao)
    return render(request, 'blog/admin/update_ServicoManutencao.html', {'form':form})




#### CREATE ######

@login_required()
def CriarMeuBlog(request):
    form = UpdateMeuBlogForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('list_MeuBlog')
    else:
        form = UpdateMeuBlogForm(request.POST or None, request.FILES or None)
    return render(request, 'blog/admin/criar_Meublog.html', {'form':form})


@login_required()
def CriarPost(request):
    form = UpdatePostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.autor = request.user
        post.save()
        return redirect('list_Post')
    else:
        form = UpdatePostForm(request.POST or None, request.FILES or None)
    return render(request, 'blog/admin/criar_Post.html',{'form':form})


@login_required()
def CriarServicoManutencao(request):
    form = UpdateServicoManutencaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_ServicoManutencao')
    else:
        form = UpdateServicoManutencaoForm(request.POST or None)
    return render(request, 'blog/admin/criar_ServicoManutencao.html', {'form':form})



@login_required()
def post_delete(request,id):
    obj = get_object_or_404(Post,pk=id)
    obj.delete()
    return redirect('list_Post')

@login_required()
def FaleComigo_delete(request,id):
    obj = get_object_or_404(FaleComigo, pk=id)
    obj.delete()
    return redirect('list_FaleComigo')


@login_required()
def MeuBlog_delete(request,id):
    obj = get_object_or_404(MeuBlog,pk=id)
    obj.delete()
    return redirect('list_MeuBlog')

@login_required()
def ServicoManutencao_delete(request,id):
    obj = get_object_or_404(ServicoManutencao,pk=id)
    obj.delete()
    return redirect('list_ServicoManutencao')





############### view para cadastro de pessoa blog  ##################

def Registrar(request):
    user_form = CadastrarUserForm(request.POST or None)

    if user_form.is_valid():
        user_form.save()
        return redirect('login')

    return render(request, 'registration/register.html',{'user_form':user_form})



def edit_perfil_list(request):

    return render(request, 'blog/admin/usuario/edit_user.html',{})


def editar_usuario_nome_completo(request):
    user_form = CadastrarUserFormNomeCompleto(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('edit_perfil')

    return render(request, 'blog/admin/usuario/edit_user_nomecompleto.html',{'user_form':user_form})


def editar_usuario_username(request):
    user_form = CadastrarUserFormUsername(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('edit_perfil')

    return render(request, 'blog/admin/usuario/edit_user_username.html',{'user_form':user_form})


def editar_usuario_email(request):
    user_form = CadastrarUserFormEmail(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('edit_perfil')

    return render(request, 'blog/admin/usuario/edit_user_email.html',{'user_form':user_form})


def editar_usuario_senha(request):
    user_form = CadastrarUserFormPassword(request.POST, instance=request.user)
    if request.method == 'POST':
        if user_form.is_valid():
            user_form.save()
            return redirect('edit_perfil')

    return render(request, 'blog/admin/usuario/edit_user_senha.html',{'user_form':user_form})









