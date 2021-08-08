from django.urls import path

from . import views


urlpatterns = [
    path(
        '',
        views.GameListView.as_view(),
        name='game_list'
    ),
    path(
        'create/',
        views.GameCreateView.as_view(),
        name='game_create'
    ),
    path(
        '<int:pk>/',
        views.GameDetailView.as_view(),
        name='game_detail'
    ),
    path(
        '<int:pk>/update/',
        views.GameUpdateView.as_view(),
        name='game_update'
    ),
    path(
        '<int:pk>/delete/',
        views.GameDeleteView.as_view(),
        name='game_delete',
    ),
]
