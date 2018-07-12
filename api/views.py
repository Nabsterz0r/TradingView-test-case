from rest_framework import viewsets

from .models import Symbol
from .filters import SymbolsNameFilterBackend, SymbolsPageFilterBackend, SymbolsBatchFilterBackend
from api.serializers import SymbolsSerializer

# Create your views here.
class SymbolsList(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolsSerializer
    filter_backends = (SymbolsPageFilterBackend,
                       SymbolsBatchFilterBackend)

class SymbolsData(viewsets.ModelViewSet):
    queryset = Symbol.objects.all()
    serializer_class = SymbolsSerializer
    filter_backends = (SymbolsNameFilterBackend,)