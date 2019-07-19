# chatbotd dentist booking website
## description
 It's a chatbot website for booking dentists
## how to the website works

run backend:
 python3 appiontment/app/demo/\_\_init\_\_.py
![readme_pic](
http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/run_backend.png)
 run frontend:
 front/client.html
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/run_frontend.png)
### Bot Interaction
 It's a Rule based chatbot (/api/brain/rules.rive)
 The data rule based bot needed handled through the chatbot API which get needed data through dentists and timeslots API
 * basic greetings
![readme_pic]((https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/greeting.png))
 * specific dentist information
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/ask_doctors.png)
 * pick avaliable dentist
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/avialable_dentists.png)
 * get available dates
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/avaliable_dates.png)
 * get available timeslots
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/avaliable_time.png)
 * check a specific timeslot
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/check_timeslots.png)
 * book an appointment
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/book.png)
 * confirm/cancel an appointment
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/confirm:cancel.png)
## design
###data design
 /api/\_\_init\__.py generate /api/data.json
![readme_pic](http://github.com/Joannazhx/chatbot_dentist_booking_web/readme_pic/data.png)
###Restful API design
 * __Post__:appiontment /chatbots
 Bot interaction
 Response body:
{
&ensp;&ensp;"messges": "hi bro" 
}
 * __Get__: appiontment/dentists
 get all dentists' names
 Response body:
 [
&ensp;&ensp;"Yogita Khasa",
&ensp;&ensp;"Janani Ravichandran", "Nader Malik",
&ensp;&ensp;"Jelena Skovrlj"
]

 * __Get__: appointment/dentists/{id}
 get all information of a specific dentist
 Response body:
[
&ensp;{
&ensp;&ensp;&ensp;"location": "Suite 4, Level 1 / 300,Barangaroo Avenue Barangaroo,NSW 2000",
&ensp;&ensp;&ensp;"name": "Yogita Khasa",
&ensp;&ensp;&ensp;"specialization": "Cosmetic Dentistry" 
&ensp;}
]

 * __Get__: appiontment /timeslots/{id}
 Get available dates of the specific dentist
 Response body: 
 [
&ensp;&ensp;"07/04", 
&ensp;&ensp;"08/04", 
&ensp;&ensp;"09/04", 
&ensp;&ensp;"10/04", 
&ensp;&ensp;"11/04", 
&ensp;&ensp;"12/04",
&ensp;&ensp;"13/04"
]

 * __Get__: appiontment /timeslots/{id}/{date}
 Get all available timeslots of the specific doctor in specific date
 [
&ensp;&ensp;"10:00 - 11:00", 
&ensp;&ensp;"14:00 - 15:00",
&ensp;&ensp;"16:00 - 17:00" ]

 * __Get__: appiontment /timeslots/{id}/{date}/{timeslot}
 Check a specific timeslot is available or not
 Response body:
[
&ensp;&ensp;"booked",
&ensp;&ensp;"Joe" 
]
Or 
[
&ensp;&ensp;"available",
&ensp;&ensp;"None" 
]

 * __Post__:  appiontment /timeslots/{id}/{dates}/{timeslot}/{patient}/reserve
 book the appiontment
 Response body:
{
&ensp;&ensp;"07/04 15:00-16:00": 
&ensp;[
&ensp;&ensp;&ensp;"booked",
&ensp;&ensp;&ensp;"Joe" 
&ensp;]
}

 * __Delete__:appointment/timeslots/{id}/{dates}/{timeslot}/{patient}/cancel
 cancel the booked timeslot appointment
  Response body:
{
&ensp;&ensp;"07/04 15:00-16:00": 
&ensp;[
&ensp;&ensp;&ensp;"available",
&ensp;&ensp;&ensp;"None" 
&ensp;]
}


