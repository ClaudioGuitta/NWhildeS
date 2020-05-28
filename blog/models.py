from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model


TIPO_CHOICE = [
    ('HTML/CSS', 'HTML/CSS'),
    ('Js', 'JavaScript'),
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Bootstrap', 'Bootstrap'),
    ('Conteúdo Região', 'Conteudo Região'),
]


class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField('Título',max_length=200)
    descricao_curta = models.CharField('Descrição Curta',max_length=100, null=True,blank=True)
    text = RichTextField('Texto',null=True, blank=True)
    created_date = models.DateTimeField('Data de Criação',
            default=timezone.now)
    published_date = models.DateTimeField('Data de Publicação',
            blank=True, null=True)
    foto = models.ImageField('Foto',upload_to="media/posts/%Y/%m/%D", null=True,blank=True)
    tipo = models.CharField('Tipo de Postagem', max_length=15, choices=TIPO_CHOICE, null=True,
            blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Editar_nav_blog(models.Model):
    logo = models.CharField(max_length=20,null=True)
    imagem_de_fundo = models.ImageField(upload_to="media/%Y/%m/%D", null=True)



class SobreMim(models.Model):
    primeiro_nome = models.CharField(max_length=50, null=True, blank=True)
    segundo_nome = models.CharField(max_length=50, null=True, blank=True)
    descricao_curta = models.CharField(max_length=300, null=True, blank=True)
    sobre = models.TextField(null=True, blank=True)
    experiencia = models.TextField(null=True, blank=True)
    educacao = models.TextField(null=True, blank=True)
    habilidades = models.TextField(null=True, blank=True)
    interesse = models.TextField(null=True, blank=True)
    imagem_sobre = models.ImageField(upload_to="media/%Y/%m/%D", null=True,blank=True)
    email = models.EmailField(null=True, blank=True)



class FaleComigo(models.Model):
    nome = models.CharField(max_length=40)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    mensagem = models.TextField()
    def __str__(self):
        return self.nome
    data = models.DateTimeField(default=timezone.now, null=True,blank=True)


class MeuBlog(models.Model):
    descricao_curta = models.CharField(max_length=255,null=True,blank=True)
    fotos = models.ImageField(upload_to="media/%Y/%m/%D")

    def __str__(self):
        return self.descricao_curta


class teste(models.Model):
    teste = models.CharField(max_length=10)
    teste2 = models.IntegerField()

class ServicoManutencao(models.Model):
    servico = models.CharField(max_length=255)
    descricao = models.CharField(max_length=255)
    valor = models.FloatField()

    def __str__(self):
        return self.servico


############# modelo cadastro de para cadastro de pessoa blog ###########
'''
class UserPessoa(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cpf = models.CharField(primary_key=True,max_length=11,blank=True)

'''



'''
SEXO_CHOICES = (
    ('M', 'Maculino'),
    ('F', 'Feminino')
)

sexo = models.CharField(max_length=2,blank=True,choices=SEXO_CHOICES)
'''
