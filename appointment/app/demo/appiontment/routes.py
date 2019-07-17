# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.chatbots import Chatbots
from .api.timeslots_id import TimeslotsId
from .api.timeslots_id_date import TimeslotsIdDate
from .api.timeslots_id_date_timeslot import TimeslotsIdDateTimeslot
from .api.timeslots_id_dates_timeslot_patient_reserve import TimeslotsIdDatesTimeslotPatientReserve
from .api.timeslots_id_dates_timeslot_patient_cancel import TimeslotsIdDatesTimeslotPatientCancel
from .api.dentists import Dentists
from .api.dentists_id import DentistsId


routes = [
    dict(resource=Chatbots, urls=['/chatbots'], endpoint='chatbots'),
    dict(resource=TimeslotsId, urls=['/timeslots/<int:id>'], endpoint='timeslots_id'),
    dict(resource=TimeslotsIdDate, urls=['/timeslots/<int:id>/<date>'], endpoint='timeslots_id_date'),
    dict(resource=TimeslotsIdDateTimeslot, urls=['/timeslots/<int:id>/<date>/<timeslot>'], endpoint='timeslots_id_date_timeslot'),
    dict(resource=TimeslotsIdDatesTimeslotPatientReserve, urls=['/timeslots/<int:id>/<dates>/<timeslot>/<patient>/reserve'], endpoint='timeslots_id_dates_timeslot_patient_reserve'),
    dict(resource=TimeslotsIdDatesTimeslotPatientCancel, urls=['/timeslots/<int:id>/<dates>/<timeslot>/<patient>/cancel'], endpoint='timeslots_id_dates_timeslot_patient_cancel'),
    dict(resource=Dentists, urls=['/dentists'], endpoint='dentists'),
    dict(resource=DentistsId, urls=['/dentists/<int:id>'], endpoint='dentists_id'),
]