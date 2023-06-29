from datetime import datetime, timedelta


def calcTime(l_event):
    if l_event == "tomorrow":
        st_date = (datetime.now() + timedelta(hours=24)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        end_date = (datetime.now() + timedelta(hours=26)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        return st_date,end_date
    elif l_event == "nextweek":
        st_date = (datetime.now() + timedelta(weeks=1)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        end_date = (datetime.now() + timedelta(weeks=1)+ timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        return st_date,end_date 
    elif l_event == "nextmonth":
        st_date = (datetime.now() + timedelta(weeks=4)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        end_date = (datetime.now() + timedelta(weeks=4)+ timedelta(hours=1)).strftime("%Y-%m-%dT%H:%M:%S-07:00")
        return st_date,end_date 
    
# if __name__ == "__main__":
#     print(calcTime("tomorrow"))