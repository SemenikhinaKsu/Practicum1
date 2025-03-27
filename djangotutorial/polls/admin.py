from django.contrib import admin

from .models import Question, Deposit, Client, Transaction, Bank

admin.site.register(Question)
admin.site.register(Deposit)
admin.site.register(Client)
admin.site.register(Transaction)
admin.site.register(Bank)