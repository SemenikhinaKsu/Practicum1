from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Bank, Transaction, Client, Deposit
from .forms import BankForm, TransactionForm, ClientForm, DepositForm
from rest_framework import viewsets
from .models import Question, Choice, Bank, Transaction, Client, Deposit
from .serializers import QuestionSerializer, ChoiceSerializer, BankSerializer, TransactionSerializer, ClientSerializer, DepositSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer
# Bank Views
class BankListView(View):
    def get(self, request):
        banks = Bank.objects.all()
        return render(request, 'bank_list.html', {'banks': banks})

class BankDetailView(View):
    def get(self, request, bank_id):
        bank = get_object_or_404(Bank, pk=bank_id)
        return render(request, 'bank_detail.html', {'bank': bank})

class BankCreateView(View):
    def get(self, request):
        form = BankForm()
        return render(request, 'bank_form.html', {'form': form})

    def post(self, request):
        form = BankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bank_list')
        return render(request, 'bank_form.html', {'form': form})

class BankUpdateView(View):
    def get(self, request, bank_id):
        bank = get_object_or_404(Bank, pk=bank_id)
        form = BankForm(instance=bank)
        return render(request, 'bank_form.html', {'form': form})

    def post(self, request, bank_id):
        bank = get_object_or_404(Bank, pk=bank_id)
        form = BankForm(request.POST, instance=bank)
        if form.is_valid():
            form.save()
            return redirect('bank_detail', bank_id=bank_id)
        return render(request, 'bank_form.html', {'form': form})

class BankDeleteView(View):
    def get(self, request, bank_id):
        bank = get_object_or_404(Bank, pk=bank_id)
        return render(request, 'bank_confirm_delete.html', {'bank': bank})

    def post(self, request, bank_id):
        bank = get_object_or_404(Bank, pk=bank_id)
        bank.delete()
        return redirect('bank_list')

# Similar Views for Transaction, Client, and Deposit

# Transaction views
class TransactionListView(View):
    def get(self, request):
        transactions = Transaction.objects.all()
        return render(request, 'transaction_list.html', {'transactions': transactions})

class TransactionDetailView(View):
    def get(self, request, transaction_id):
        transaction = get_object_or_404(Transaction, pk=transaction_id)
        return render(request, 'transaction_detail.html', {'transaction': transaction})

# Client views
class ClientListView(View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'client_list.html', {'clients': clients})

# Deposit views
class DepositListView(View):
    def get(self, request):
        deposits = Deposit.objects.all()
        return render(request, 'deposit_list.html', {'deposits': deposits})

# You would repeat similar patterns for creating, updating, and deleting Deposits and Clients.


