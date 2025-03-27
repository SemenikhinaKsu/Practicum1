
## Question

- **question_text**: `CharField` (max_length=200)
- **pub_date**: `DateTimeField` ("date published")

## Choice

- **question**: `ForeignKey` (ссылка на `Question`, on_delete=models.CASCADE)
- **choice_text**: `CharField` (max_length=200)
- **votes**: `IntegerField` (default=0)

## Bank

- **bank_id**: `AutoField` (primary_key=True)  # BankID
- **legal_address**: `TextField` (verbose_name="Юридический адрес")  # ЮридическийАдрес
- **name**: `CharField` (max_length=255, verbose_name="Название")  # Название

## Transaction

- **transaction_id**: `AutoField` (primary_key=True)  # TransactionID
- **date**: `DateField` (verbose_name="Дата")  # Дата
- **amount**: `FloatField` (verbose_name="Сумма")  # Сумма

## Client

- **client_id**: `AutoField` (primary_key=True)  # ClientID
- **last_name**: `CharField` (max_length=255, verbose_name="Фамилия")  # Фамилия
- **first_name**: `CharField` (max_length=255, verbose_name="Имя")  # Имя
- **patronymic**: `CharField` (max_length=255, verbose_name="Отчество")  # Отчество
- **phone_number**: `CharField` (max_length=50, verbose_name="Номер")  # Номер
- **deposit**: `ForeignKey` (ссылка на `Deposit`, on_delete=models.CASCADE, null=True, blank=True, related_name='clients')  # Вклад

## Deposit

- **deposit_id**: `AutoField` (primary_key=True)  # DepositID
- **client_id1**: `ForeignKey` (ссылка на `Client`, on_delete=models.CASCADE, related_name='deposits')  # clientID1
- **amount**: `FloatField` (verbose_name="Сумма")  # Сумма
- **interest_rate**: `DecimalField` (max_digits=5, decimal_places=2, verbose_name="Процентная ставка")  # процентная_ставка
- **term**: `PositiveIntegerField` (verbose_name="Срок")  # Срок
- **opening_date**: `DateField` (verbose_name="Дата открытия")  # Дата_открытия
- **closing_date**: `DateField` (null=True, blank=True, verbose_name="Дата закрытия")  # Дата_закрытия
- **transaction**: `ForeignKey` (ссылка на `Transaction`, on_delete=models.CASCADE, related_name='deposits')  # Транзакция
- **bank**: `ForeignKey` (ссылка на `Bank`, on_delete=models.CASCADE, related_name='deposits')  # Банк
