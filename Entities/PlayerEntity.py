# Copyright (c) 2017 David J Moore

from . import Entity

from pyarena.Config import Conf

class PlayerEntity(Entity.Entity):

    def __init__(self):
        super(PlayerEntity,self).__init__()
        self.Glyph = Conf['Entities']['PlayerEntity']['Glyph']

