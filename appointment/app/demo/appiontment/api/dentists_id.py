# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class DentistsId(Resource):

    def get(self, id):

        information = data[str(id)]['information']
        print(information)
        infro = []
        infro.append(information)
        return infro, 200, None