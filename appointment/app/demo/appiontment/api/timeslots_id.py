# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class TimeslotsId(Resource):

    def get(self, id):
        available_dates = []
        for i in data[str(id)]["appointment"]:
            for j in data[str(id)]["appointment"][i]:
                if data[str(id)]["appointment"][i][j][0] == 'available':
                    date = str(i)
                    available_dates.append(date)
                    break
        #print(available_dates)
        return available_dates, 200, None