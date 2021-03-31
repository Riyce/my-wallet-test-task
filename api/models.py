from django.db import models


class Wallet(models.Model):
    name = models.CharField(verbose_name='Wallet`s name', max_length=100,)
    balance = models.DecimalField(verbose_name='Balance',
                                  max_digits=12, decimal_places=2, default=0)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class Type(models.TextChoices):
        ADDING = 'adding'
        DEBITING = 'debiting'

    date = models.DateTimeField(verbose_name='Date of transaction',
                                auto_now_add=True)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE,
                               related_name='transactions',
                               verbose_name='Wallet`s name',
                               null=True, blank=True)
    comment = models.CharField(verbose_name='Comment', max_length=255)
    summ = models.DecimalField(verbose_name='Transaction`s name',
                               max_digits=12, decimal_places=2)
    type = models.TextField(verbose_name='Transaction`s type',
                            choices=Type.choices, default='debiting')

    class Meta:
        ordering = ['-date']

    def save(self, *args, **kwargs):
        super(Transaction, self).save(*args, **kwargs)
        if self.type == 'debiting':
            self.wallet.balance -= self.summ
            self.wallet.save()
        else:
            self.wallet.balance += self.summ
            self.wallet.save()
