from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=300)
    subject = forms.CharField(max_length=100)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea , required=True)




class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  
        super(BaseForm, self).__init__(*args, **kwargs)

forms.Form = BaseForm