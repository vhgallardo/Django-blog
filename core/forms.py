from django import forms

class ContactForm(forms.Form):
    message = forms.CharField(
        widget=forms.Textarea(attrs={
        'class':'form-control w-100',
        'placeholder':'Mensaje',
        'name':'message',
        'id':'message',
        'cols':'30',
        'rows':'9',
        'onfocus':"this.placeholder = ''",
        'onblur':"this.placeholder = 'Mensaje'"
        }),
        error_messages ={
        'required':"Ingresa un mensaje"
        }
    )
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control valid',
        'placeholder':'Ingresa tu nombre',
        'name':'name',
        'id':'name',
        'onfocus':"this.placeholder = ''",
        'onblur':"this.placeholder = 'Ingresa tu nombre'"
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class':'form-control valid',
        'placeholder':'Correo',
        'name':'email',
        'id':'email',
        'onfocus':"this.placeholder = ''",
        'onblur':"this.placeholder = 'Correo'"
    }))
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control valid',
        'placeholder':'Asunto',
        'name':'subject',
        'id':'subject',
        'onfocus':"this.placeholder = ''",
        'onblur':"this.placeholder = 'Asunto'"
    }))