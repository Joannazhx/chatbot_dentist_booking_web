# -*- coding: utf-8 -*-
from __future__ import absolute_import

import flask_restful as restful

import datetime,random,json

from ..validators import request_validate, response_filter

id_to_dentist = { 
                    "0" : "Yogita Khasa",
                    "1" : "Janani Ravichandran",
                    "2" : "Nader Malik",
                    "3" : "Jelena Skovrlj"
}
dentist_to_id = { 
                    "yogita khasa":"0",
                    "janani ravichandran":"1",
                    "nader malik":"2",
                    "jelena skovrlj":"3"
}
patient = ''
patients = ["Alice","Zoe","Hannah","Kiyo","Molly","Sophie","John","Monica","Joey","Phobe","Ross","Chandeller","Richel","Tony","Sana","Steve","Seven","Tina","Joe","Ana","Lily"]
status = ["available","booked"]
location = [
        'Suite 4, Level 1 / 300 Barangaroo Avenue Barangaroo, NSW 2000',
        'Westfield Shopping Centre Level 5, Shop 5020-5021, / 159-175 Church Street Parramatta, NSW 2150',
        'Parade Centre Suite 6 / 826 Anzac Parade Maroubra, NSW 2035',
        'Suite 4 / 166 Belmore Road Randwick, NSW 2031']
specialization =[
        'Cosmetic Dentistry',
        'Extractions',
        'Root Canal Treatment',
        'Dentures'
]

dates = []
today = datetime.date.today()
book_appointment = []
chioce_doctor_id = []

# all dates next week
for i in range (1,8) :
    date = (today + datetime.timedelta(days = i)).strftime('%d/%m')
    #print(date)
    dates.append(date)

timeslots = []
# all 1 hour timeslots in a date
for i in range (9,17) :
    j = i + 1
    timeslot = str(i)+":00 - "+str(j)+":00"
    timeslots.append(timeslot)


data = {}
for i in id_to_dentist:
    dentist_data = {}
    information = {}
    dentist = int(i)
    information["name"] = id_to_dentist[i]
    information['location'] = location[dentist]
    information['specialization'] = specialization[dentist]
    dentist_data['information'] = information
    datetime = {}
    for j in range(0,7):
        slottime = {}
        for k in range(0,8):
            statu = []
            ss = random.randint(0,1)
            statu.append(status[ss])
            if ss == 1:
                patient = patients[random.randint(0,20)]
            else:
                patient = "None"
            statu.append(patient)
            slottime[timeslots[k]] = statu
        datetime[dates[j]] = slottime
    dentist_data['appointment'] = datetime
    data[i] = dentist_data
    #print(data)

#write data json file
with open('data.json','w') as outfile:
    json.dump(data,outfile,ensure_ascii=False)
    outfile.write('\n')
        

class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]