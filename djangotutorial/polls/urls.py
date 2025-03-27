from django.urls import path

from . import views
urlpatterns = [
    
    path("", views.index, name="index"),
    #path('bank/new/', views.BankCreateView.as_view(), name='bank-create'),  # Создание нового банка
    #path('client/new/', views.ClientCreateView.as_view(), name='client-create'),  # Создание нового клиента
    #path('transaction/new/', views.TransactionCreateView.as_view(), name='transaction-create'),  # Создание новой транзакции
    #path('deposit/new/', views.DepositCreateView.as_view(), name='deposit-create'),  # Создание нового вклада
]
