import random
import openai
import datetime
from google_files import quickstart as addEvnt
import calc_time
import findDateIntxt



def handle_response(message) -> str:
    p_message = message.lower()
    if p_message != '' and p_message != None and p_message[:1] == "/":
        #type your logic here 

















        # if "create" in p_message and "event" in p_message:
        #     # =====store last event 
        #     with open('last_event', 'w') as file:
        #         file.write('Create Event')
        #     # ======get approval
        #     return "Sure please provide - EventTitle,Date*,time*,duration*,Location (use prefix - /inp )"
        
        
        # findDate = findDateIntxt.getDate(p_message)
        # if findDate !='' and findDate != None:
        #     # =====store last event 
        #     with open('last_event', 'w') as file:
        #         file.write('nextmonth')
        #     # ======get approval
        #     return "New event on "+findDate+"?  (use prefix - '/')"


        # if p_message[:4] == "/inp":
        #     with open('last_event') as f:
        #         l_event = f.readlines()
        #     if l_event[0] == 'Create Event':
        #         inp = p_message[4:].split(",")

        #         e_name = inp[0]
        #         st_date = 

        #         # add event function will create event based on given parameter (add more if want)
        #         event_id, event_link =  addEvnt.addEvent(st_date,end_date,"test event")
        #         return "Event scheduled....... ID: "+ event_id +" Link: "+ event_link
        #         # return st_date
            
        # print(p_message[:2] == "/")

# if __name__ == "__main__":
#     print(handle_response("/yes"))
