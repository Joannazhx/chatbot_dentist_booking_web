# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class TimeslotsIdDate(Resource):

    def get(self, id, date):

        #print(date)
        date = date[:2]+'/'+date[2:4]
        #print(date)
        available_timeslots = []
        for i in data[str(id)]["appointment"][date]:
            if data[str(id)]["appointment"][date][i][0] == 'available':
                    available_timeslots.append(i)
        #print(available_timeslots)
        return available_timeslots, 200, None