from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Bank, Transaction, Client, Deposit
from .forms import BankForm, TransactionForm, ClientForm, DepositForm  # Предполагается наличие соответствующих форм


