from rest_framework import filters

class SymbolsPageFilterBackend(filters.BaseFilterBackend):
    page_size = 5
    filter_parameter = 'page'

    def filter_queryset(self, request, queryset, view):
        parameter = request.query_params.get(self.filter_parameter)
        if parameter:
            parameter = int(parameter)
            return queryset[self.page_size * (parameter - 1) : self.page_size * parameter]
        else:
            return queryset


class SymbolsBatchFilterBackend(filters.BaseFilterBackend):
    filter_parameter = 'batch'

    def filter_queryset(self, request, queryset, view):
        parameter = request.query_params.get(self.filter_parameter)
        if parameter:
            return queryset[:int(parameter)]
        else:
            return queryset


class SymbolsNameFilterBackend(filters.BaseFilterBackend):
    filter_parameter = 'name'

    def filter_queryset(self, request, queryset, view):
        parameter = request.query_params.get(self.filter_parameter)
        if parameter:
            return queryset.filter(name=request.query_params.get(self.filter_parameter))

