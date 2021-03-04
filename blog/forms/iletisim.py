
from django  import forms

class IletisimForm(forms.Form):
      email = forms.EmailField(label='Email',max_length=200)
      isim_soyisim = forms.CharField(label='İsim-soyisim',max_length=50)
      mesaj = forms.CharField(widget=forms.Textarea(attrs={
            'class' : 'form-control'
      }))