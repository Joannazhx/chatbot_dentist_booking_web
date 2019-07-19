# chatbotd dentist booking website
## description
 It's a chatbot website for booking dentists
## design
### Restful API design
 * __Post__:appiontment /chatbots <br>
 Bot interaction <br>
 Response body: <br>
{ <br>
&ensp;&ensp;"messges": "hi bro"  <br>
} <br>
 * __Get__: appiontment/dentists <br>
 get all dentists' names <br>
 Response body: <br>
 [ <br>
&ensp;&ensp;"Yogita Khasa", <br>
&ensp;&ensp;"Janani Ravichandran", "Nader Malik", <br>
&ensp;&ensp;"Jelena Skovrlj" <br>
] <br>

 * __Get__: appointment/dentists/{id} <br>
 get all information of a specific dentist <br>
 Response body: <br>
[ <br>
&ensp;{ <br>
&ensp;&ensp;&ensp;"location": "Suite 4, Level 1 / 300,Barangaroo Avenue Barangaroo,NSW 2000", <br>
&ensp;&ensp;&ensp;"name": "Yogita Khasa", <br>
&ensp;&ensp;&ensp;"specialization": "Cosmetic Dentistry" <br>
&ensp;} <br>
] <br>

 * __Get__: appiontment /timeslots/{id} <br>
 Get available dates of the specific dentist <br>
 Response body: <br>
 [ <br>
&ensp;&ensp;"07/04", <br>
&ensp;&ensp;"08/04", <br>
&ensp;&ensp;"09/04", <br>
&ensp;&ensp;"10/04", <br>
&ensp;&ensp;"11/04", <br>
&ensp;&ensp;"12/04",<br>
&ensp;&ensp;"13/04"<br>
] <br>

 * __Get__: appiontment /timeslots/{id}/{date} <br>
 Get all available timeslots of the specific doctor in specific date <br>
 [ <br>
&ensp;&ensp;"10:00 - 11:00", <br>
&ensp;&ensp;"14:00 - 15:00", <br>
&ensp;&ensp;"16:00 - 17:00" ] <br>

 * __Get__: appiontment /timeslots/{id}/{date}/{timeslot} <br>
 Check a specific timeslot is available or not <br>
 Response body: <br>
[ <br>
&ensp;&ensp;"booked", <br>
&ensp;&ensp;"Joe"  <br>
] <br>
Or  <br>
[ <br>
&ensp;&ensp;"available", <br>
&ensp;&ensp;"None" <br>
] <br>

 * __Post__:  appiontment /timeslots/{id}/{dates}/{timeslot}/{patient}/reserve <br>
 book the appiontment <br>
 Response body: <br>
{ <br>
&ensp;&ensp;"07/04 15:00-16:00":  <br>
&ensp;[ <br>
&ensp;&ensp;&ensp;"booked", <br>
&ensp;&ensp;&ensp;"Joe"  <br>
&ensp;] <br>
} <br>

 * __Delete__:appointment/timeslots/{id}/{dates}/{timeslot}/{patient}/cancel <br>
 cancel the booked timeslot appointment <br>
  Response body: <br>
{ <br>
&ensp;&ensp;"07/04 15:00-16:00": <br>
&ensp;[ <br>
&ensp;&ensp;&ensp; "available", <br>
&ensp;&ensp;&ensp; "None"  <br>
&ensp;] <br>
} <br>

### data design
 /api/\_\_init\__.py generate /api/data.json
 <img src="https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/data.png" width="50%" height="50%">

## how to the website works
run backend:
 python3 appiontment/app/demo/\_\_init\_\_.py
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/run_backend.png)
 run frontend:
 front/client.html
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/run_frontend.png)
### Bot Interaction
 It's a Rule based chatbot (/api/brain/rules.rive)
 The data rule based bot needed handled through the chatbot API which get needed data through dentists and timeslots API
 
 * basic greetings
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/greeting.png)
 * specific dentist information
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/ask_doctors.png)

 * pick avaliable dentist
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/avialable_dentists.png)

 * get available dates
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/avaliable_dates.png)

 * get available timeslots
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/avaliable_time.png)

 * check a specific timeslot
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/check_timeslots.png)

 * book an appointment
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/book.png)

 * confirm/cancel an appointment
![image](https://github.com/Joannazhx/chatbot_dentist_booking_web/blob/master/readme_pic/confirm:cancel.png)




