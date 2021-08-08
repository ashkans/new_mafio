# -*- coding: utf-8 -*-
""" Views for the games application. """
# standard library

# django

# models
from .models import Game

# views
from base.views import BaseCreateView
from base.views import BaseDeleteView
from base.views import BaseDetailView
from base.views import BaseListView
from base.views import BaseUpdateView

# forms
from .forms import GameForm


class GameListView(BaseListView):
    """
    View for displaying a list of games.
    """
    model = Game
    template_name = 'games/game_list.pug'
    permission_required = 'games.view_game'


class GameCreateView(BaseCreateView):
    """
    A view for creating a single game
    """
    model = Game
    form_class = GameForm
    template_name = 'games/game_create.pug'
    permission_required = 'games.add_game'


class GameDetailView(BaseDetailView):
    """
    A view for displaying a single game
    """
    model = Game
    template_name = 'games/game_detail.pug'
    permission_required = 'games.view_game'


class GameUpdateView(BaseUpdateView):
    """
    A view for editing a single game
    """
    model = Game
    form_class = GameForm
    template_name = 'games/game_update.pug'
    permission_required = 'games.change_game'


class GameDeleteView(BaseDeleteView):
    """
    A view for deleting a single game
    """
    model = Game
    permission_required = 'games.delete_game'
    template_name = 'games/game_delete.pug'
