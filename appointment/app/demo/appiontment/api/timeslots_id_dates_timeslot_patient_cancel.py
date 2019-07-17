# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g

from . import Resource,data
from .. import schemas


class TimeslotsIdDatesTimeslotPatientCancel(Resource):

    def delete(self, id, dates, timeslot, patient):
        date = dates[:2]+'/'+dates[2:4]
        endtime = int(timeslot) + 1
        timeslot = timeslot+':00 - ' + str(endtime) + ':00'
        if data[str(id)]["appointment"][date][timeslot][0] == "booked":
            print(patient)
            if data[str(id)]["appointment"][date][timeslot][1] == patient:
                data[str(id)]["appointment"][date][timeslot][0] = "available"
                data[str(id)]["appointment"][date][timeslot][1] = "None"
            else:
                return None, 400, None
        else:
            return None, 400, None
        appointment_ca = {}
        keys = date + " "+timeslot
        appointment_ca[keys] = data[str(id)]["appointment"][date][timeslot]
        return appointment_ca,200,None

            