# -*- coding: utf-8 -*-
""" Administration classes for the games application. """
# standard library

# django
from django.contrib import admin

# models
from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
