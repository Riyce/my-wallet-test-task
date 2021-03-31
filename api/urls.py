from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AllTransactionViewSet, TransactionViewSet, WalletViewSet

router = DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='Wallets')
router.register(
    r'wallets/(?P<wallet_id>\d+)/transactions',
    TransactionViewSet,
    basename='Transactions'
)
router.register(
    r'transactions',
    AllTransactionViewSet,
    basename='AllTransactions'
)

urlpatterns = [
    path('', include(router.urls)),
]
