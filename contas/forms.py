from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['data', 'descriacao', 'valor', 'observacoes', 'categoria']

        widgets = {
            'data': forms.DateInput(attrs={'class':'form-control','display':'block' }),
            'descriacao': forms.TextInput(attrs={'class':'form-control', }),
            'valor': forms.NumberInput(attrs={'class':'form-control', }),
            'observacoes': forms.Textarea(attrs={'class':'form-control', }),
            'categoria': forms.Select(attrs={'class':'form-control', }),
        }