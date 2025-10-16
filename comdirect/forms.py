from django import forms
from django.contrib.auth.forms import UserChangeForm # Importar o formulário base do Admin
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

# Formulário para atualização do Usuário (FRONT-END)
class UsuarioUpdateForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de Usuário'}),
        }

# =================================================================
# CORREÇÃO PARA O ERRO NO DJANGO ADMIN: object of type 'NoneType' has no len()
# Este formulário deve ser referenciado no seu admin.py para o modelo Usuario.
# =================================================================
class UsuarioAdminChangeForm(UserChangeForm):
    """
    Formulário personalizado para o Django Admin que corrige o TypeError:
    object of type 'NoneType' has no len() no campo 'username'.
    """
    class Meta(UserChangeForm.Meta):
        model = Usuario
        # Você provavelmente está a usar '__all__' ou listando campos no admin.py,
        # mas aqui listamos explicitamente para garantir o campo 'username' está lá.
        fields = '__all__' # ou list_your_admin_fields

    def clean_username(self):
        """
        Limpeza personalizada para garantir que 'username' não seja None, 
        evitando assim o TypeError.
        """
        username = self.cleaned_data.get('username')
        
        # Se for None, retorna uma string vazia ("") que tem um comprimento (len = 0).
        if username is None:
            return ""
            
        return username

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
        