from django import forms
from .models import Operaciones, Subcategory

class OperacionesForm(forms.ModelForm):
    class Meta:
        model = Operaciones
        fields = ('name','fecha_creacion','category','subcategory','fecha_pago','monto')
        widgets = {
             'fecha_creacion': forms.DateInput(attrs={'type': 'date'}),
             'fecha_pago': forms.DateInput(attrs={'type': 'date'}),
             'monto': forms.NumberInput(attrs={'class': 'currency-input', 'step': '0.01'})                     
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass # invalid input from the client; ignore and fallback to empty City queryset
        
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategory_set.order_by('name') 