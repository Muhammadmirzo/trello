from django.urls import path

from boardsApp.views import (
    BoardFormView,
    BoardCreateView, BoardListView,
)

app_name = 'boardsApp'
urlpatterns = [
    # path("", BoardFormView.as_view(), name='home_page'),
    path('', BoardListView.as_view(), name='board_list'),
    path('new/', BoardCreateView.as_view(), name='new_board'),
]
