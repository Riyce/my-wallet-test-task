from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Transaction, Wallet


class TransactionCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        wallet = get_object_or_404(
            Wallet,
            id=self.context['request'].parser_context['kwargs']['wallet_id']
        )
        if data['summ'] > wallet.balance and data['type'] == 'debiting':
            raise serializers.ValidationError(
                'Not enough money on the balance!'
            )
        return data

    class Meta:
        exclude = ('id', 'wallet')
        model = Transaction


class TransactionListSerializer(serializers.ModelSerializer):
    wallet = serializers.SlugRelatedField(
        queryset=Wallet.objects.all(),
        slug_field='name',
    )

    class Meta:
        fields = '__all__'
        model = Transaction


class WalletSerializer(serializers.ModelSerializer):
    transactions = TransactionListSerializer(many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Wallet
        read_only_fields = ['balance', 'transactions']


class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'balance')
        model = Wallet
