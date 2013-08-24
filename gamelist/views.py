from django.views.generic import ListView
from django.views.generic.edit import CreateView

from .forms import ConnectionForm
from .models import Connection, Game


class CreateConnection(CreateView):
    model = Connection
    form_class = ConnectionForm
    template_name = 'gamelist/create_connection.html'

    def get_context_data(self, **kwargs):
        context = super(CreateConnection, self).get_context_data(**kwargs)
        context['game'] = Game.objects.get(pk=self.kwargs['game_id'])
        return context

    def get_initial(self):
        return {'game': Game.objects.get(pk=self.kwargs['game_id'])}


class CreateGame(CreateView):
    model = Game
    fields = ['name']
    template_name = 'gamelist/create_game.html'


class GameList(ListView):
    model = Game
    template_name = 'gamelist/list.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.all().order_by('name')