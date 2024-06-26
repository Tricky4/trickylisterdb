from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class TaskListPagination(PageNumberPagination):
    page_size = 10
    # page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    # last_page_strings = 'end'
    
class TaskListLOPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'start'
    
class TaskListCPagination(CursorPagination):
    page_size = 5
    ordering = 'created'
    cursor_query_param = 'record'