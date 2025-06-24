from langchain_core.tools import StructuredTool
from pydantic import BaseModel,Field
from tool_functions.create_event_function import create_event_function


class CalendarInput(BaseModel):
    summary: str = Field(..., description="Title of the calendar event.")
    start_time: str = Field(..., description="Start time in ISO format (e.g., 2025-06-25T14:00:00)")
    duration_minutes: int = Field(60, description="Duration of the event in minutes")

calendar_tool = StructuredTool.from_function(
    name = "calendar_tool",
    description= (
        "Use this tool to create an event in Google Calendar. "
        "Provide a title (summary), start time in ISO format, and optionally duration in minutes."
    ),
    func=create_event_function,
    args_schema=CalendarInput
)