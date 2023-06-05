from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class AgentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'username',
            'email',
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
        
        help_texts = {
            'username': _('Логин должен состоять только из букв, цифр и символов @/./+/-/_<br>Обратите внимание, что исполнители задают пароль с помощью функции восстановления пароля при входе в систему.')
        }
