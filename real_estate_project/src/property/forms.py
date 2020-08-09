from django import forms
from .models import Reserve , Property


class ReserveForm(forms.ModelForm):
    class Meta : 
        model = Reserve
        fields = '__all__'

class PropertyForm(forms.ModelForm):
    class Meta : 
        model = Property
        fields = '__all__'
