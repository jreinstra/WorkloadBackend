from rest_framework import serializers

from main.models import Block


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id', 'start_timestamp', 'end_timestamp', 'subject', 'user')
        extra_kwargs = {'user': {'write_only': True}}