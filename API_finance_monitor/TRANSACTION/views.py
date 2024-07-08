from django.shortcuts import render
from django.views.generic import View,ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import OperacionesForm
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