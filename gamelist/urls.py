from django.conf.urls import patterns, url

from .views import CreateConnection, CreateGame, GameList

urlpatterns = patterns('',
    url(r'^$', GameList.as_view(), name='list'),
    url(r'^game/create/$', CreateGame.as_view(), name='create_game'),
    url(r'^game/(?P<game_id>\d+)/connection/create/', CreateConnection.as_view(), name='create_connection'),
)