from rest_framework import serializers

from integration.models import Transfer, Stock


class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = (
            "transfer_account_number",
            "user_name",
            "transfer_amount"
        )


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = (
            "name",
            "isin",
            "asset_group"
        )
