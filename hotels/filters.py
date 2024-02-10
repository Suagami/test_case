from rest_framework import filters


class QueryParamOrderFilterBackend(filters.BaseFilterBackend):
    """
    Filter that only allows users to see their own objects.
    """
    ordering_fields = ['city_id']

    def filter_queryset(self, request, queryset, view):
        if request.method != 'GET':
            return queryset
        from_id = request.query_params.get('from_id')
        if from_id:
            queryset = queryset.filter(id__gt=from_id)
        for field in self.ordering_fields:
            if request.query_params.get(field, None) is not None:
                queryset = queryset.order_by(field)

        return queryset
