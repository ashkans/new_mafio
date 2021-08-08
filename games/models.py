# -*- coding: utf-8 -*-
""" Models for the games application. """
# standard library

# django
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

# models
from base.models import BaseModel
from users.models import User
from .managers import GameQuerySet


class Game(BaseModel):
    """
    TODO: Fill this description
    The games system is used to store game.
    """
    # foreign keys
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('user'),
    )
    # required fields
    name = models.CharField(
        _('name'),
        max_length=30,
        unique=True,
    )
    # optional fields

    # Manager
    objects = GameQuerySet.as_manager()

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')

    def __str__(self):
        # TODO this is an example str return, change it
        return self.name

    def get_absolute_url(self):
        """ Returns the canonical URL for the Game object """
        # TODO this is an example, change it
        return reverse('game_detail', args=(self.pk,))
