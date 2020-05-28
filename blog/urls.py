from django.urls import path, include
from . import views
from .views import *
from django.views.generic.list import ListView



urlpatterns = [

    path('', views.index_home,name='index_home'),

    path('post/<int:id>', views.post_mostrar, name='post'),

    path('teste/', testeListView.as_view()),

    path('sobre_mim/', views.sobre_mim_detail, name='sobre_mim'),

    path('index_home/', views.post_list, name='post_list'),

    path('manutencao/', views.manutencao_de_computador, name='manutencao'),

    path('index_admin/', views.index_admin, name='index_admin'),

    #path('fale_comigo/', views.FaleComigoFormulario, name='Fale_comigo'),

    path('post_list/', views.post_list, name='post_list'),



    path('list_Editar_nav_blog/', views.list_Editar_nav_blog, name='list_Editar_nav_blog'),
    path('list_FaleComigo/', views.list_FaleComigo, name='list_FaleComigo'),
    path('list_MeuBlog/', views.list_MeuBlog, name='list_MeuBlog'),
    path('list_Post/', views.list_Post, name='list_Post'),
    path('list_ServicoManutencao/', views.list_ServicoManutencao, name='list_ServicoManutencao'),
    path('list_SobreMim/', views.list_SobreMim, name='list_SobreMim'),

    path('editar/<int:id>', views.update_Editar_nav_blog, name='editar_nav'),
    path('editar_MeuBlog/<int:id>', views.UpdateMeuBlog, name='editar_MeuBlog'),
    path('editar_Post/<int:id>',views.UpdatePost,name='editar_Post'),
    path('editar_SobreMim/<int:id>',views.UpdateSobreMim,name='editar_SobreMim'),
    path('editar_ServicoManutencao/<int:id>',views.UpdateServicoManutencao,name='editar_ServicoManutencao'),

    path('criar_MeuBlog/',views.CriarMeuBlog,name='criar_MeuBlog'),
    path('criar_Post/',views.CriarPost,name='criar_Post'),
    path('criar_ServicoManitencao/',views.CriarServicoManutencao,name='criar_ServicoManutencao'),

    path('list_Post/<int:id>',views.post_delete,name='post_delete'),
    path('list_FaleComigo/<int:id>',views.FaleComigo_delete,name='FaleComigo_delete'),
    path('list_MeuBlog/<int:id>',views.MeuBlog_delete,name='MeuBlog_delete'),
    path('list_ServicoManutencao/<int:id>',views.ServicoManutencao_delete,name='ServicoManutencao_delete'),

    path('registrar/',views.Registrar,name='registrar'),

    path('editar_usuario_nome_completo/',views.editar_usuario_nome_completo,name='editar_usuario_nome_completo'),
    path('editar_usuario_username/',views.editar_usuario_username,name='editar_usuario_username'),
    path('editar_usuario_email/',views.editar_usuario_email,name='editar_usuario_email'),
    path('editar_usuario_senha/',views.editar_usuario_senha,name='editar_usuario_senha'),
    path('edit_perfil/',views.edit_perfil_list,name='edit_perfil'),
]

