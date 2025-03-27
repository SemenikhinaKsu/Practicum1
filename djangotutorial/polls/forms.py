from django import forms
from .models import Bank, Client, Deposit, Transaction

class BankForm(forms.ModelForm):
    class Meta:
        model = Bank
        fields = ['legal_address', 'name']
        labels = {
            'legal_address': 'Юридический адрес',
            'name': 'Название'
        }
        widgets = {
            'legal_address': forms.Textarea(attrs={'placeholder': 'Введите юридический адрес'}),
            'name': forms.TextInput(attrs={'placeholder': 'Введите название банка'}),
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['last_name', 'first_name', 'patronymic', 'phone_number', 'deposit']
        labels = {
            'last_name': 'Фамилия',
            'first_name': 'Имя',
            'patronymic': 'Отчество',
            'phone_number': 'Номер',
            'deposit': 'Вклад'
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'placeholder': 'Введите фамилию'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Введите имя'}),
            'patronymic': forms.TextInput(attrs={'placeholder': 'Введите отчество'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}),
            'deposit': forms.Select(attrs={'placeholder': 'Выберите вклад'}),
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['date', 'amount']
        labels = {
            'date': 'Дата',
            'amount': 'Сумма'
        }
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Введите сумму'}),
        }

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['client_id1', 'amount', 'interest_rate', 'term', 'opening_date', 'closing_date', 'transaction', 'bank']
        labels = {
            'client_id1': 'Клиент',
            'amount': 'Сумма',
            'interest_rate': 'Процентная ставка',
            'term': 'Срок',
            'opening_date': 'Дата открытия',
            'closing_date': 'Дата закрытия',
            'transaction': 'Транзакция',
            'bank': 'Банк'
        }
        widgets = {
            'client_id1': forms.Select(attrs={'placeholder': 'Выберите клиента'}),
            'amount': forms.NumberInput(attrs={'placeholder': 'Введите сумму'}),
            'interest_rate': forms.NumberInput(attrs={'placeholder': 'Введите процентную ставку'}),
            'term': forms.NumberInput(attrs={'placeholder': 'Введите срок'}),
            'opening_date': forms.TextInput(attrs={'type': 'date'}),
            'closing_date': forms.TextInput(attrs={'type': 'date'}),
            'transaction': forms.Select(attrs={'placeholder': 'Выберите транзакцию'}),
            'bank': forms.Select(attrs={'placeholder': 'Выберите банк'}),
        }
        