from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User


class DateForm(forms.DateInput):
    input_type = 'date'


### FALE COMIGO FORM ####
class FaleComigoForm(forms.ModelForm):
    class Meta:
        model = FaleComigo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Informe Seu Nome'}),
            'telefone': forms.TextInput(attrs={'class':'form-control','type':'tel','placeholder':'Digite os 11 digitos do seu Celular','pattern':'[0-9]{11}'}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email','placeholder':'E-mail'}),
            'mensagem': forms.Textarea(attrs={'class':'form-control','type':'text','placeholder':'Mensagem'})
        }


######  FORM UPDATE FORM   ####

class UpdateNavForm(forms.ModelForm):
    class Meta:
        model = Editar_nav_blog
        fields ='__all__'

class UpdateMeuBlogForm(forms.ModelForm):
    class Meta:
        model = MeuBlog
        fields ='__all__'

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','descricao_curta','text','created_date','published_date','foto','tipo')
        widgets = {
            'created_date':DateForm(), 'published_date':DateForm(),
            }


class UpdateSobreMimForm(forms.ModelForm):
    class Meta:
        model = SobreMim
        fields = '__all__'


class UpdateServicoManutencaoForm(forms.ModelForm):
    class Meta:
        model = ServicoManutencao
        fields = '__all__'


###### formulário para cadastro e atualização de dados do usuário de pessoa blog ######



class CadastrarUserFormNomeCompleto(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
        ]


class CadastrarUserFormUsername(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
        ]

class CadastrarUserFormEmail(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'email',
        ]

class CadastrarUserFormPassword(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control',}),
        }

    def save(self, commit=True):
        user = super(CadastrarUserFormPassword, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CadastrarUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'email',
        ]
        widgets = {
            'password': forms.PasswordInput(attrs={'class':'form-control',}),
            'email': forms.TextInput(attrs={'class':'form-control','type':'email'})
        }

    def save(self, commit=True):
        user = super(CadastrarUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
