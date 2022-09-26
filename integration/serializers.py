from rest_framework import serializers

from integration.models import Transfer


class TransferSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transfer
        fields = (
            "transfer_account_number",
            "user_name",
            "transfer_amount"
        )