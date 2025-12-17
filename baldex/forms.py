from django import forms
# Importa o UserChangeForm do Django para ser a base do formulário Admin
from django.contrib.auth.forms import UserChangeForm 
from .models import Deposito, Saque, Usuario, ClientBankDetails

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Deposito
        fields = ['valor', 'comprovativo_imagem'] 
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
            'comprovativo_imagem': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SaqueForm(forms.ModelForm):
    class Meta:
        model = Saque
        fields = ['valor']
        widgets = {
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Valor'}),
        }

# Formulário para atualização do Usuário
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
        }

# Formulário para Detalhes Bancários do Cliente
class ClientBankDetailsForm(forms.ModelForm):
    class Meta:
        model = ClientBankDetails
        fields = ['nome_banco', 'nome_titular_conta', 'iban']
        widgets = {
            'nome_banco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Banco'}),
            'nome_titular_conta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Titular da Conta'}),
            'iban': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'IBAN'}),
        }


# =================================================================
# CORREÇÃO PARA O ERRO NO DJANGO ADMIN: object of type 'NoneType' has no len()
# Esta classe é NECESSÁRIA para ser usada no admin.py do seu modelo Usuario.
# =================================================================
class UsuarioAdminChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
        model = Usuario
        # Garante que todos os campos do UserAdmin (incluindo senha e permissões) são usados.
        fields = '__all__'

    def clean_username(self):
        """
        Limpeza personalizada para garantir que 'username' não seja None 
        durante o processamento do formulário no Admin.
        """
        username = self.cleaned_data.get('username')
        
        # A correção principal: Se o valor for None, força a ser uma string vazia ("").
        if username is None:
            return ""
            
        return username
        