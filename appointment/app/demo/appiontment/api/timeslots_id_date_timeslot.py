# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class TimeslotsIdDateTimeslot(Resource):

    def get(self, id, date, timeslot):

        #print(timeslot)
        date = date[:2]+'/'+date[2:4]
        endtime = int(timeslot) + 1
        timeslot = timeslot+':00 - ' + str(endtime) + ':00'
        #print(timeslot)
        return data[str(id)]["appointment"][date][timeslot], 200, None