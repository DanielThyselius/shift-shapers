from pydantic import BaseModel, Field
from typing import Any
from .schedule import Schedule

class ScheduleChangeAnalysis(BaseModel):
    thoughts: str = Field(description="The AI's thought process while analyzing the request")
    original_query: str = Field(description="The original query text that was analyzed")
    suggested_schedule: Schedule = Field(description="The new schedule after the changes have been applied")
    reason: str | None = Field(description="The extracted reason for the changes")
    recommendation: str = Field(
        description="Whether the change should be approved, denied, or needs discussion",
        enum=["approve", "deny", "discuss"]
    )
    reasoning: str = Field(description="Detailed explanation for the recommendation")

class ScheduleChangeRequest(BaseModel):
    request_text: str
    schedule: Schedule
    

class ScheduleChangeResponse(BaseModel):
    request: str
    analysis: ScheduleChangeAnalysis 