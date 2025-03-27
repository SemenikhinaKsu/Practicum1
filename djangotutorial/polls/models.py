from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
            return self.question_text
    def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
from django.db import models

class Bank(models.Model):
    bank_id = models.AutoField(primary_key=True)  # BankID
    legal_address = models.TextField(verbose_name="Юридический адрес")  # ЮридическийАдрес
    name = models.CharField(max_length=255, verbose_name="Название")  # Название

    def __str__(self):
        return self.name

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)  # TransactionID
    date = models.DateField(verbose_name="Дата")  # Дата
    amount = models.FloatField(verbose_name="Сумма")  # Сумма

    def __str__(self):
        return f"Transaction {self.transaction_id} on {self.date}"

class Client (models.Model):
    client_id = models.AutoField(primary_key=True)  # ClientID
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")  # Фамилия
    first_name = models.CharField(max_length=255, verbose_name="Имя")  # Имя
    patronymic = models.CharField(max_length=255, verbose_name="Отчество")  # Отчество
    phone_number = models.CharField(max_length=50, verbose_name="Номер")  # Номер
    deposit = models.ForeignKey('Deposit', on_delete=models.CASCADE, null=True, blank=True, related_name='clients')  # Вклад

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

class Deposit(models.Model):
    deposit_id = models.AutoField(primary_key=True)  # DepositID
    client_id1 = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='deposits')  # clientID1
    amount = models.FloatField(verbose_name="Сумма")  # Сумма
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Процентная ставка")  # процентная_ставка
    term = models.PositiveIntegerField(verbose_name="Срок")  # Срок
    opening_date = models.DateField(verbose_name="Дата открытия")  # Дата_открытия
    closing_date = models.DateField(null=True, blank=True, verbose_name="Дата закрытия")  # Дата_закрытия
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name='deposits')  # Транзакция
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE, related_name='deposits')  # Банк

    def __str__(self):
        return f"Deposit {self.deposit_id} for {self.client_id1}"