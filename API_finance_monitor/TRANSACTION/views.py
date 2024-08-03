from django.shortcuts import render
from django.views.generic import View,ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import OperacionesForm,Gasto_DiarioForm
import datetime
from .models import *

# Create your views here.

class Inicio(View):
    def get(self, request):
        return render(request,'inicio.html', {})

class Ingresos(View):
    
     def get(self, request):
        categories = Category.objects.all()
        subcategories = Subcategory.objects.all()
        return render(request, 'ingresos.html', {'categories': categories,'subcategories': subcategories})
        
# class OperacionesListView(ListView):
#      model = Operaciones
#      form_class = OperacionesForm
#      context_object_name = 'operations'
#      template_name ='TRANSACTION/operaciones_list.html'    

#      def get_queryset(self):
#          queryset = super().get_queryset().select_related('category', 'subcategory')
#          for operacion in queryset:
#              operacion.multiplicador = operacion.subcategory.multiplicador
#          return queryset

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
      
      def get_queryset(self):
         queryset = super().get_queryset()
         month_filter = self.request.GET.get('month_filter')

         if month_filter:
             year, month = month_filter.split('-')
             queryset = queryset.filter(fecha_creacion__year=year, fecha_creacion__month=month)
         
         return queryset
      
      def get_context_data(self, **kwargs):
          context = super().get_context_data(**kwargs)
          current_year = datetime.datetime.now().year
          context['selected_month'] = self.request.GET.get('month_filter', '')
          context['min_date'] = '2014-09'
          context['max_date'] = f'{current_year}-12'
          return context
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
    template_name = 'TRANSACTION/gastodiario_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        month_filter = self.request.GET.get('month_filter')

        if month_filter:
            year, month = month_filter.split('-')
            queryset = queryset.filter(fecha_creacion__year=year, fecha_creacion__month=month)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = datetime.datetime.now().year
        context['selected_month'] = self.request.GET.get('month_filter', '')
        context['min_date'] = '2014-09'
        context['max_date'] = f'{current_year}-12'
        return context    

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