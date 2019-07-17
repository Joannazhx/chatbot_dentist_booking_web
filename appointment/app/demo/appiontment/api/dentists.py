# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class Dentists(Resource):

    def get(self):

        dentists = []
        for i in range(4):
            dentists.append(data[str(i)]['information']['name'])

        return dentists, 200, None