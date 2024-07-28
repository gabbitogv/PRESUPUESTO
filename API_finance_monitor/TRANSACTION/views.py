from django.shortcuts import render
from django.views.generic import View,ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import OperacionesForm,Gasto_DiarioForm
from .models import *

# from django.shortcuts import redirect
# from django.utils.text import slugify
# from django.http import HttpResponse
# import json
# from django.http import HttpResponseBadRequest
# from django.http import JsonResponse
# from django.template.loader import render_to_string

# Create your views here.

class Inicio(View):
    def get(self, request):
        return render(request,'inicio.html', {})

class Ingresos(View):
    
     def get(self, request):
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        return render(request, 'ingresos.html', {'categories': categories,'subcategories': subcategories})
        
class OperacionesListView(ListView):
    model = Operaciones
    form_class = OperacionesForm
    context_object_name = 'operations'
    template_name ='TRANSACTION/operaciones_list.html'    

    def get_queryset(self):
        queryset = super().get_queryset().select_related('category', 'subcategory')
        for operacion in queryset:
            operacion.multiplicador = operacion.subcategory.multiplicador
        return queryset

class OperacionesCreateView(CreateView):
    model = Operaciones
    form_class = OperacionesForm
    success_url = reverse_lazy('operation_changelist')
    template_name ='TRANSACTION/operaciones_form.html'   

class OperacionesUpdateView(UpdateView):
    model = Operaciones
    form_class = OperacionesForm
    success_url = reverse_lazy('operation_changelist')
    template_name ='TRANSACTION/operationes_modify.html'

def load_subcategories(request):
    category_id = request.GET.get('category')
    subcategorys = Subcategory.objects.filter(category_id=category_id).order_by('name')
    return render(request,'API_finance_monitor/branch_dropdown_list_options.html',{'subcategorys': subcategorys})


class GastoDiarioListView(ListView):
    model = Gasto_Diario
    form_class = Gasto_DiarioForm
    context_object_name = 'gds'
    template_name ='TRANSACTION/gastodiario_list.html'

class GastoDiarioCreateView(CreateView):
    model = Gasto_Diario
    form_class = Gasto_DiarioForm
    success_url = reverse_lazy('gastodiario_changelist')
    template_name ='TRANSACTION/gastodiario_form.html'

class GastoDiarioUpdateView(UpdateView):
    model = Gasto_Diario
    form_class = Gasto_DiarioForm
    success_url = reverse_lazy('gastodiario_changelist')
    template_name ='TRANSACTION/gastodiario_modify.html'