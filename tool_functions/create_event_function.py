from utils.authenticate_calendar import authenticate_calendar
from datetime import datetime, timedelta


def create_event_function(summary: str, start_time: str, duration_minutes: int = 60) -> str:
    """Creates a Google Calendar event."""
    service = authenticate_calendar()
    start_dt = datetime.fromisoformat(start_time)
    end_dt = start_dt + timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {'dateTime': start_dt.isoformat(), 'timeZone': 'UTC'},
        'end': {'dateTime': end_dt.isoformat(), 'timeZone': 'UTC'},
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print("event_created")
    return f"Event created: {created_event.get('htmlLink')}"
