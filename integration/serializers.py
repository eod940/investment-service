from rest_framework import serializers

from integration.models import Transfer, Stock, Holdings


class TransferSerializer(serializers.ModelSerializer):
    transfer_id = serializers.IntegerField(source="id", write_only=True)

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


class HoldingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Holdings
