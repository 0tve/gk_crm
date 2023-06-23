from typing import Any, Dict
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm, SetPasswordForm
from .models import Lead, Agent, Category, FollowUp
from agents.forms import CustomClearableFileInput
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class LeadModelForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'first_name',
            'last_name',
            'middle_name',
            'age',
            'agent',
            'address',
            'order',
            'phone_number',
            'email',
            'profile_picture',
        )
        
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'age': 'Возраст',
            'agent': 'Ответственный исполнитель',
            'address': 'Адрес',
            'order': 'Заказ',
            'phone_number': 'Телефон',
            'email': 'Электронная почта',
            'profile_picture': 'Фото',
        }
        
        widgets = {
            'profile_picture': CustomClearableFileInput(),
        }
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['agent'].queryset = Agent.objects.filter(organisation=self.request.user.userprofile)
        self.fields['profile_picture'].widget.clear_checkbox_label = 'Удалить'
        self.fields['profile_picture'].widget.initial_text = "Сейчас"
        self.fields['profile_picture'].widget.input_text = "Изменить"


class CustomPasswordResetConfirmForm(SetPasswordForm): 
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomPasswordResetConfirmForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = 'Новый пароль'
        self.fields['new_password1'].help_text = """Пароль должен состоять минимум из 8 символов.<br>
                                               Пароль не может состоять только из цифр.<br>
                                               Пароль не должен быть узнаваемым."""
        self.fields['new_password2'].label = 'Повторите новый пароль'
        self.error_messages['password_mismatch'] = 'Введеные пароли не совпадают'        


class CustomLoginForm(AuthenticationForm):
    def __init__(self, request: Any = ..., *args: Any, **kwargs: Any) -> None:
        super(CustomLoginForm, self).__init__(request, *args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'

        self.error_messages['invalid_login'] = 'Неверные данные. Обратите внимание, что поля чувствительны к регистру.'
        self.error_messages['inactive'] = 'Данный аккаунт деактивирован.'


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Повторите пароль'
        self.fields['username'].help_text = 'Логин должен состоять только из букв, цифр и символов @/./+/-/_'
        self.fields['password1'].help_text = """Пароль должен состоять минимум из 8 символов.<br>
                                               Пароль не может состоять только из цифр.<br>
                                               Пароль не должен быть узнаваемым."""
        self.fields['password2'].help_text = 'Введите пароль еще раз.'


class AssignAgentForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=Agent.objects.none(), label='Исполнитель')

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")
        agents = Agent.objects.filter(organisation=request.user.userprofile)
        super(AssignAgentForm, self).__init__(*args, **kwargs)
        self.fields["agent"].queryset = agents


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            'category',
        )
        
        labels = {
            'category': 'Категория'
        }


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = (
            'name',
        )
        labels = {
            'name': _('Название')
        }
        error_messages = {
            'name':
                {'required': 'Данное поле обязательно для заполнения'}
        }
        

class FollowUpModelForm(forms.ModelForm):
    class Meta:
        model = FollowUp
        fields = (
            'notes',
            'file',
        )
        
        labels = {
            'notes': 'Описание',
            'file': 'Файл',
        }
        
        widgets = {
            'file': CustomClearableFileInput(),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].widget.clear_checkbox_label = 'Удалить'
        self.fields['file'].widget.initial_text = "Сейчас"
        self.fields['file'].widget.input_text = "Изменить"
