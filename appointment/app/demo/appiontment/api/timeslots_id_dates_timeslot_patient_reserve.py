# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class TimeslotsIdDatesTimeslotPatientReserve(Resource):

    def post(self, id, dates, timeslot, patient):

        date = dates[:2]+'/'+dates[2:4]
        endtime = int(timeslot) + 1
        timeslot = timeslot+':00 - ' + str(endtime) + ':00'
        print(timeslot)
        print(data[str(id)]["appointment"][date][timeslot])
        if data[str(id)]["appointment"][date][timeslot][0] == "available":
            data[str(id)]["appointment"][date][timeslot][0] = "booked"
            data[str(id)]["appointment"][date][timeslot][1] = patient
            appointment = {}
            appointment[date] = data[str(id)]["appointment"][date][timeslot]
        else:
            appointment = {}
            keys = ""
            keys = keys +  date + " "+timeslot
            dd = data[str(id)]["appointment"][date][timeslot]
            dd.append(timeslot)
            print(dd)
            appointment[date] = data[str(id)]["appointment"][date][timeslot]
            return appointment, 400, None
        
        return appointment, 200, None