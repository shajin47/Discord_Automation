import random
import openai
import datetime
from google_files import quickstart as addEvnt
import calc_time
import findDateIntxt



def handle_response(message) -> str:
    p_message = message.lower()
    if p_message != '' and p_message != None and p_message[0] == '/' :

        if p_message[:3] == "/ce":
                inp = p_message[4:].split(",")

                e_name = inp[0]
                st_date = inp[1].replace("-","/").removeprefix(" ")
                st_date = datetime.strptime(st_date, '%d/%m/%y %H:%M:%S')
                end_date = (st_date + timedelta(hours=int(inp[2]))).strftime("%Y-%m-%dT%H:%M:%S-07:00")
                st_date = st_date.strftime("%Y-%m-%dT%H:%M:%S-07:00")
                # add event function will create event based on given parameter (add more if want)
                event_id, event_link =  addEvnt.addEvent(st_date,end_date,e_name)
                return "Event scheduled....... ID: "+ event_id +" Link: "+ event_link
                # return st_date,end_date,e_name
        
        elif "create" in p_message and "event" in p_message:

            # =====store last event 
            with open('last_event', 'w') as file:
                file.write('Create Event')
            # ======get approval
            return "Sure please provide - EventTitle,Datetime(d/m/y hh:mm:ss)*,duration(in hours)*,Location (use prefix - /CE )"

















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
