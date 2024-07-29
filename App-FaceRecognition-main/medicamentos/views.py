from django.shortcuts import redirect, render
from medicamentos.forms import MedicamentoForm
from .models import Medicamento
from django.core.paginator import Paginator

# Create your views here.
def listMedicamentos(request):
    pesquisa = request.GET.get('pesquisa')
    
    if pesquisa:
        medicamentos = Medicamento.objects.filter(Nome__icontains=pesquisa)
    else:
        medicamentos = Medicamento.objects.all().order_by('Nome')
        paginacao = Paginator(medicamentos, 10)
        pagina = request.GET.get('page')
        medicamentos = paginacao.get_page(pagina)
    
    contexto = {'medicamentos': medicamentos}
    return render(request, 'medicamento/listMedicamentos.html', contexto)

def createMedicamento(request):
    criarMedicamento = MedicamentoForm()
    if request.method == 'POST':
        criarMedicamento = MedicamentoForm(request.POST)
        if criarMedicamento.is_valid():
            criarMedicamento.save()
            return redirect('listMedicamentos')
        
    contexto = {'criarMedicamento': criarMedicamento}
    return render(request, 'medicamento/createMedicamento.html', contexto)