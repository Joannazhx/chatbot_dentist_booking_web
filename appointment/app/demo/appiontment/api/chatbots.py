# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

from flask import request, g
import requests

from . import Resource,patient,dentist_to_id,dates,id_to_dentist,book_appointment,chioce_doctor_id
from .. import schemas

import os
from rivescript import RiveScript 

currentDIr = os.path.dirname(os.path.realpath(__file__))
rs = RiveScript()
rs.load_directory(currentDIr + "/brain")
rs.sort_replies()




class Chatbots(Resource):

    def post(self):

        clientmessage = request.values['messges']
        print(clientmessage)

        rulebot = rs.reply("localuser",clientmessage)
        mess = dict()
        mess['messges'] = rulebot
        print(mess)

        # Get all dentists name
        if "dentists=" in rulebot:
            url = "http://127.0.0.1:5000/appiontment/dentists"
            apiresponse = requests.get(url) 
            jsondata = apiresponse.json()
            string = ""
            for i in range(len(jsondata)):
                string = string + jsondata[i] + "\n"
            rulebot = rulebot.replace("dentists=",string)
            mess['messges'] = rulebot

        #get dentist information
        elif "dentistinfro=" in rulebot:
            idcontain = rulebot.split("\n",1)
            name = idcontain[0]
            name = name.replace("dentistinfro=","")
            id = dentist_to_id[name]
            #print(id)
            id = int(id)
            url = "http://127.0.0.1:5000/appiontment/dentists/{}".format(id)
            apiresponse = requests.get(url) 
            jsondata = apiresponse.json()
            #print(jsondata)
            string = ""
            dicts = jsondata[0]
            name = dicts["name"]
            for i in dicts:
                if i != "name":
                    string+= "the "+ i + " of the dentist " + name +" is " + dicts[i] + "\n"
            string += "\n"
            string += idcontain[1]
            mess['messges'] = string
            #print(string)

        elif "doctorchoice=" in rulebot:
            idcontain = rulebot.split("\n",1)
            print(idcontain)
            name = idcontain[0]
            name = name.replace("doctorchoice=","")
            print(name)
            chioce_doctor_id.append(dentist_to_id[name])
            string = ""
            string += idcontain[1]
            mess['messges'] = string
        
        #check a timeslot available or not
        elif "checktime=" in rulebot:
            spdata = rulebot.split("\n",1)
            datatimecon = spdata[0]
            datetimesp = datatimecon.split(",",1)
            time = datetimesp[0]
            time = time.replace("checktime=","")
            time = time.replace("00","")
            date = datetimesp[1]
            date = date.replace("checkdate=","")
            date = date.replace("/","")
            id = chioce_doctor_id[0]
            url = "http://127.0.0.1:5000/appiontment/timeslots/{}/{}/{}".format(id,date,time)
            apiresponse = requests.get(url) 
            jsondata = apiresponse.json()
            string = ""
            if jsondata[0] == "booked":
                string +=  time + ":00 of " + date + " is booked by " + jsondata[1] + "\n"
                string += "you can check another timeslot or\nYou can ask me:\navailable dates\navailable time of [date]\n"
            else:
                string +=  time + ":00 of " + date + " is available\n"
                string += "you can book this timeslot by saying\n[yourname] book [time] of [date]\n"

            mess['messges'] = string
        
        #get all available dates
        elif "availabledates=" in rulebot:
            spdata = rulebot.split("\n",1)
            id = chioce_doctor_id[0]
            url = "http://127.0.0.1:5000/appiontment/timeslots/{}".format(id)
            apiresponse = requests.get(url) 
            jsondata = apiresponse.json()
            print(jsondata)
            string = ""
            for i in range(len(jsondata)):
                string += jsondata[i] + "\n"
            rulebot = rulebot.replace("availabledates=",string)
            mess['messges'] = rulebot
        
        #get available timeslots in a date
        elif "availabledate=" in rulebot:
            spdata = rulebot.split("\n",1)
            dateco = spdata[0]
            date = dateco.replace("availabledate=","")
            id = chioce_doctor_id[0]
            url = "http://127.0.0.1:5000/appiontment/timeslots/{}/{}".format(id,date)
            apiresponse = requests.get(url) 
            jsondata = apiresponse.json()
            string = ""
            for i in range(len(jsondata)):
                string += jsondata[i] + "\n"
            string += "\n"
            string += spdata[1]
            mess['messges'] = string
        
        #patient book an appointment
        elif "bookpatient=" in rulebot:
            spdata = rulebot.split("\n",1)
            dataco = spdata[0]
            datasp = dataco.split(",")
            patientname = datasp[0]
            patientname = patientname.replace("bookpatient=","")
            date = datasp[1]
            date = date.replace("bookdate=","")
            timeslot = datasp[2]
            timeslot = timeslot.replace("booktime=","")
            timeslot = timeslot.replace("00","")
            id = chioce_doctor_id[0]
            url = "http://127.0.0.1:5000/appiontment/timeslots/{}/{}/{}/{}/reserve".format(id,date,timeslot,patientname)
            apiresponse = requests.post(url) 
            jsondata = apiresponse.json()
            string = ""
            print(jsondata)
            if jsondata == None:
                string += "timeslot be booked by other patient or date/time choice wrong\n"
                string += spdata[1]
            else:
                end = int(timeslot) + 1
                timed = timeslot + ":00 - " + str(end) + ":00"
                string += patientname + " booked with doctor " + id_to_dentist[str(chioce_doctor_id[0])] + " at " + timed + " of " + date +"\n"
                string += "You can ask me:\nconfirm\ncancel\n"
                book_appointment.append(patientname)
                book_appointment.append(id)
                book_appointment.append(date)
                book_appointment.append(timeslot)
            mess['messges'] = string
        
        # check if the patient want to confirm cancel
        elif "trycancel=" in rulebot:
            patientname = book_appointment[0]
            id = book_appointment[1]
            date = book_appointment[2]
            timeslot = book_appointment[3]
            string = ""
            id = str(id)
            string += "Do you want to cancel" + " booking with doctor " + id_to_dentist[id] + " at " + timeslot + " of " + date +"\n"
            string += "You can cancel by answer:Yes or no"
            mess['messges'] = string 

        #cancel booked appiontment
        elif "cancel=" in rulebot:
            patientname = book_appointment[0]
            id = book_appointment[1]
            date = book_appointment[2]
            timeslot = book_appointment[3]
            url = "http://127.0.0.1:5000/appiontment/timeslots/{}/{}/{}/{}/cancel".format(id,date,timeslot,patientname)
            apiresponse = requests.delete(url) 
            jsondata = apiresponse.json()
            string = ""
            id = str(id)
            string += patientname + " cancelled booking with doctor " + id_to_dentist[id] + " at " + timeslot + " of " + date +"\n"
            string += "You can book another appionment\n"
            mess['messges'] = string 
            
        #confrim booking
        elif "confirm=" in rulebot:
            patientname = book_appointment[0]
            id = book_appointment[1]
            date = book_appointment[2]
            timeslot = book_appointment[3]
            id = str(id)
            string = ""
            string += patientname + " booked with doctor " + id_to_dentist[id] + " at " + timeslot+ " of " + date +"\n"
            mess['messges'] = string 

        #book an appointment
        

        print(mess)

         
        return mess, 200, None