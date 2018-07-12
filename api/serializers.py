from rest_framework import serializers

from .models import Symbol


class SymbolsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Symbol
        fields = ('id', 'name', 'type', 'market', 'price', 'close', 'precent', 'delta')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        try:
            fields = self.context['request'].GET.get('fields', False)
            if fields:
                fields = fields.split(',')
                allowed = set(fields)
                existing = set(self.fields.keys())
                for field_name in existing - allowed:
                    self.fields.pop(field_name)
        except:
            pass