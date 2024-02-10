from rest_framework import pagination


class LimitPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = "limit"
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        if request.method != 'GET':
            return None

        return super().paginate_queryset(queryset, request, view)
