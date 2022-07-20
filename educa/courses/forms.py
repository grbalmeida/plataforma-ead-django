from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

# *fields = os campos que serão incluídos em cada formulário do formset.
# *extra = permite definir o número de formulários extras vazios para exibir no formset.
# *can_delete = se for definido como True, Django incluirá um campo booleano para cada
# formulário que será renderizado, na forma de uma caixa de seleção. Ela permite que
# você marque os objetos que quiser remover.
ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)