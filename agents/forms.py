from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import ClearableFileInput
User = get_user_model()

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'custom/custom_clearable_file_input.html'

class AgentModelForm(forms.ModelForm):  
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'username',
            'profile_picture',
        )
        
        labels = {
            'email': 'Электронная почта',
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'profile_picture': 'Фото',
        }
        
        widgets = {
            'profile_picture': CustomClearableFileInput(),
        }
        
        help_texts = {
            'username': _('Логин должен состоять только из букв, цифр и символов @/./+/-/_<br>Обратите внимание, что исполнители задают пароль с помощью функции восстановления пароля при входе в систему.')
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profile_picture'].widget.clear_checkbox_label = 'Удалить'
        self.fields['profile_picture'].widget.initial_text = "Сейчас"
        self.fields['profile_picture'].widget.input_text = "Изменить"