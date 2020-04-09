from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User



class FaleComigoForm(forms.ModelForm):
    class Meta:
        model = FaleComigo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control','type':'text','placeholder':'Nome'}),
            'telefone': forms.TextInput(attrs={'class':'form-control','type':'tel','placeholder':'Telefone'}),
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
        fields = '__all__'

class UpdateSobreMimForm(forms.ModelForm):
    class Meta:
        model = SobreMim
        fields = '__all__'


class UpdateServicoManutencaoForm(forms.ModelForm):
    class Meta:
        model = ServicoManutencao
        fields = '__all__'


###### formulário para cadastro de pessoa blog ######
'''
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
    def save(self,**kwargs):
        userPessoa=super().save(commit=False)
        user = User.objects.create(
            username=self.cleaned_data['username'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email']
        )
        user.set_password(self.cleaned_data['password'])
        userPessoa.user = user
        userPessoa.user.save()
        return userPessoa

'''
