from django.shortcuts import get_object_or_404
from rest_framework.mixins import (CreateModelMixin, DestroyModelMixin,
                                   ListModelMixin, RetrieveModelMixin)
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Transaction, Wallet
from .serializers import (TransactionCreateSerializer,
                          TransactionListSerializer, WalletCreateSerializer,
                          WalletSerializer)


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return WalletCreateSerializer
        return WalletSerializer


class AllTransactionViewSet(ListModelMixin, GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionListSerializer


class TransactionViewSet(CreateModelMixin, DestroyModelMixin,
                         ListModelMixin, RetrieveModelMixin, GenericViewSet):
    def get_queryset(self):
        wallet = get_object_or_404(Wallet, id=self.kwargs.get('wallet_id'))
        return wallet.transactions.all()

    def perform_create(self, serializer):
        wallet = get_object_or_404(Wallet, id=self.kwargs.get('wallet_id'))
        serializer.save(wallet=wallet)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TransactionListSerializer
        return TransactionCreateSerializer
