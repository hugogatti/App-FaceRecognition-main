from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.core.paginator import Paginator

from medicamentos.models import Medicamento
from .models import Prescricao
from django.shortcuts import render, redirect
from .forms import PrescricaoForm
from login.models import UserProfile

@login_required
def listPrescricoes(request):
    pesquisa = request.GET.get('pesquisa')
    if (pesquisa):
        prescricoes = Prescricao.objects.filter(Nome__icontains=request.GET.get('pesquisa'))
    else:
        prescricoes = Prescricao.objects.all().order_by('Data').reverse()
        paginacao = Paginator(prescricoes, 10)
        pagina = request.GET.get('page')
        prescricoes = paginacao.get_page(pagina)
        
    contexto = {'prescricoes': prescricoes}
    return render(request, 'prescricao/listPrescricoes.html', contexto)

def detalhesPrescricao(request, id):
    prescricao = Prescricao.objects.get(id=id)
    medicamentos_prescritos = prescricao.Medicamentos.all()
    
    contexto = {'prescricao': prescricao, 'medicamentos_prescritos': medicamentos_prescritos}
    return render(request, 'prescricao/detalhePrescricao.html', contexto)

def novaPrescricao(request):
    criarPrescricao = PrescricaoForm()
    if request.method == 'POST':
        criarPrescricao = PrescricaoForm(request.POST)
        if criarPrescricao.is_valid():
            prescricao = criarPrescricao.save(commit=False)
            prescricao.Medico = UserProfile.objects.get(id=1)
            prescricao.save()
            id_prescricao = len(Prescricao.objects.all())
            
            prescricao = Prescricao.objects.get(id=id_prescricao)
            # prescricao = Prescricao.objects.get(Id=prescricao.Id)
            print(request.POST.getlist('Medicamentos'))
            
            medicamentos_selecionados = request.POST.getlist('Medicamentos')
            for item in medicamentos_selecionados:
                medicamento = Medicamento.objects.get(id=int(item))
                prescricao.Medicamentos.add(medicamento)            
            
            return redirect('listPrescricoes')
        
    contexto = {'criarPrescricao': criarPrescricao}
    return render(request, 'prescricao/novaPrescricao.html', contexto)

def editarPrescricao(request, id):
    prescricao = Prescricao.objects.get(id=id)
    editarPrescricao = PrescricaoForm(instance=prescricao)
    if request.method == 'POST':
        editarPrescricao = PrescricaoForm(request.POST, instance=prescricao)
        if editarPrescricao.is_valid():
            editarPrescricao.save()
            return redirect('listPrescricoes')
        
    contexto = {'editarPrescricao': editarPrescricao}
    return render(request, 'prescricao/editarPrescricao.html', contexto)