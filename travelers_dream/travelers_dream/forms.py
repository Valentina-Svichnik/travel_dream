from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Agreement, Contract, Employee, Client, AuthUser
from django.forms import ModelForm, forms, CharField, PasswordInput, TextInput


class EmployeeCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = ["initials", "fio", "dob", "photo", "organization", "position", "user"]


class ClientCreateForm(ModelForm):
    class Meta:
        model = Client
        fields = ['fio', 'gender', 'dob', 'place', 'passport_series',
                  'passport_number', 'date_issue', 'date_end', 'issued_by', 'status', 'birth_certificate']

class AgreementCreateForm(ModelForm):
    class Meta:
        model = Agreement
        fields = ['date', 'organization','agent', 'client', 'country',  'number_participants', 'date_start', 'date_end', 'cities']


class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class UserCreateForm(ModelForm):
    class Meta:
        model = AuthUser
        fields = ['password', 'last_login', 'username', 'date_joined']


class ContractCreateForm(ModelForm):
    class Meta:
        model = Contract
        fields = ['date_start', 'date_end', 'participants']



