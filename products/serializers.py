from rest_framework import serializers

from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "title",
            "price",
            "stock",
            "thumbnail",
            "description",
            "created_at",
            "updated_at"
        )
