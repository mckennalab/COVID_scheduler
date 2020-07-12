from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from datetime import datetime, timezone, tzinfo
import pytz as tz

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']


def create_event(bench,person,month,day,is_morning):
    if is_morning:
        time_for_slot_begin = tz.timezone('America/New_York').localize(datetime(2020, month, day, 8, 0, 0)).isoformat()
        time_for_slot_end = tz.timezone('America/New_York').localize(datetime(2020, month, day, 13, 0, 0)).isoformat()
    else:
        time_for_slot_begin = tz.timezone('America/New_York').localize(datetime(2020, month, day, 13, 0, 0)).isoformat()
        time_for_slot_end = tz.timezone('America/New_York').localize(datetime(2020, month, day, 18, 0, 0)).isoformat()
    event = {
        'summary': bench + ' ' + person,
        'location': '6 floor williamson, bays 67-70',
        'description': 'Automated reservation for lab time during phase 2',
        'start': {
            'dateTime': time_for_slot_begin,
            'timeZone': 'America/New_York',
        },
        'end': {
            'dateTime': time_for_slot_end,
            'timeZone': 'America/New_York',
        }
    }
    return(event)


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # now go in and add the events
    month = 7
    day_start = 20
    day_end = 24
    calendarAPI='eeni8d2kk99e81ds28h6mm95ps@group.calendar.google.com'
    for day in range(day_start,day_end+1):
        if day % 3 == 0:
            event = create_event("BAY2","MF",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY2","MF",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","FE",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","RS",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
        if day % 3 == 1:
            event = create_event("BAY2","MF",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY2","RS",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","FE",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","FE",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
        if day % 3 == 2:
            event = create_event("BAY2","RS",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY2","MF",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","FE",month,day,True)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            event = create_event("BAY1","RS",month,day,False)
            created_event = service.events().insert(calendarId=calendarAPI, body=event).execute()
            

    
if __name__ == '__main__':
    main()
