from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Paciente
from django.shortcuts import render, redirect
from .forms import PacienteForm

def listPacientes(request):
    pesquisa = request.GET.get('pesquisa')
    if (pesquisa):
        pacientes = Paciente.objects.filter(Nome__icontains=request.GET.get('pesquisa'))
    else:
        pacientes = Paciente.objects.all().order_by('Nome')
        paginacao = Paginator(pacientes, 10)
        pagina = request.GET.get('page')
        pacientes = paginacao.get_page(pagina)
        
    contexto = {'pacientes': pacientes}
    return render(request, 'paciente/listPacientes.html', contexto)

def detalhesPaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    
    contexto = {'paciente': paciente}
    return render(request, 'paciente/detalhesPaciente.html', contexto)

def novoPaciente(request):
    criarPaciante = PacienteForm()
    if request.method == 'POST':
        criarPaciante = PacienteForm(request.POST)
        if criarPaciante.is_valid():
            criarPaciante.save()
            return redirect('listPacientes')
        
    contexto = {'criarPaciante': criarPaciante}
    return render(request, 'paciente/novoPaciente.html', contexto)

def editarPaciente(request, id):
    paciente = Paciente.objects.get(Id=id)
    editarPaciente = PacienteForm(instance=paciente)
    if request.method == 'POST':
        editarPaciente = PacienteForm(request.POST, instance=paciente)
        if editarPaciente.is_valid():
            editarPaciente.save()
            return redirect('listPacientes')
        
    contexto = {'editarPaciente': editarPaciente}
    return render(request, 'paciente/editarPaciente.html', contexto)