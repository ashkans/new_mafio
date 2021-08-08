# -*- coding: utf-8 -*-
""" Forms for the games application. """
# standard library

# django
from django import forms

# models
from .models import Game

# views
from base.forms import BaseModelForm


class GameForm(BaseModelForm):
    """
    Form Game model.
    """

    class Meta:
        model = Game
        exclude = ()
