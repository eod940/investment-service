from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None
    korean_name = models.CharField(
        verbose_name="korean name",
        max_length=150,
        blank=True
    )

    def __str__(self):
        return f'{self.korean_name}'


class Account(models.Model):
    accounts_number = models.CharField(verbose_name="계좌번호", max_length=14)
    accounts_name = models.CharField(verbose_name="계좌명", max_length=30)
    accounts_brokerage = models.CharField(verbose_name="증권사", max_length=50)
    accounts_total = models.DecimalField(
        verbose_name="계좌 총 자산",
        max_digits=16,
        decimal_places=2,
        default=0
    )
    accounts_user = models.ForeignKey(
        "User",
        verbose_name="계좌 소유자",
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "계좌"
        db_table = "accounts"

    def __str__(self):
        return f'{self.accounts_user}, {self.accounts_name}'


class Stock(models.Model):
    name = models.CharField(
        verbose_name="종목명",
        max_length=50,
        unique=True,
        blank=False
    )
    isin = models.CharField(
        verbose_name="ISIN",
        max_length=20,
        unique=True,
        blank=False
    )
    asset_group = models.CharField(verbose_name="자산그룹", max_length=50)

    class Meta:
        verbose_name = "종목"
        db_table = "stocks"

    def __str__(self):
        return f'{self.stocks_name}'


class Holdings(models.Model):
    holdings_share = models.IntegerField(verbose_name="보유 종목 수량", default=1)
    holdings_current_price = models.DecimalField(
        verbose_name="보유 종목 현재가",
        max_digits=10,
        decimal_places=2,
        default=0
    )
    holdings_stock = models.ForeignKey(
        "Stock",
        verbose_name="보유 종목",
        on_delete=models.CASCADE
    )
    investment_principal = models.DecimalField(
        verbose_name="투자 원금",
        max_digits=16,
        decimal_places=2,
        default=0
    )
    user = models.ForeignKey(
        "User",
        on_delete=models.CASCADE,
        related_name="user"
    )

    class Meta:
        verbose_name = "보유 종목"
        db_table = "investments"

    def __str__(self):
        return f'{self.user}'


class Transfer(models.Model):
    transfer_account_number = models.CharField(verbose_name="계좌번호", max_length=14)
    user_name = models.CharField(
        verbose_name="주문 유저 이름",
        max_length=150,
        blank=True,
    )
    transfer_amount = models.DecimalField(
        verbose_name="거래 금액",
        max_digits=16,
        decimal_places=2,
        default=0,
    )
    order_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "주문"
        ordering = ['-order_date', ]
