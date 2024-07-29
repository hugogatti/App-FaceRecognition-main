from django import forms
from .models import Prescricao, Medicamento, Paciente

class PrescricaoForm(forms.ModelForm):
    class Meta:
        model = Prescricao
        fields = ['Paciente', 'Medicamentos']
        widgets = {
            'Paciente': forms.RadioSelect(),
            'Medicamentos': forms.CheckboxSelectMultiple()
        }
        
    def __init__(self, *args, **kwargs):
        super(PrescricaoForm, self).__init__(*args, **kwargs)
        self.fields['Paciente'].label = 'Paciente'
        self.fields['Medicamentos'].label = 'Medicamentos'
        
        # Carregar o queryset de medicamentos para o campo 'Medicamentos'
        self.fields['Medicamentos'].queryset = Medicamento.objects.all()
        
    def clean(self):
        cleaned_data = super().clean()
        paciente = cleaned_data.get('Paciente')
        medicamentos = cleaned_data.get('Medicamentos')
        
        if not paciente:
            raise forms.ValidationError('Informe o paciente')
        if not medicamentos:
            raise forms.ValidationError('Informe ao menos um medicamento')
        
        return cleaned_data
