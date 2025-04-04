from pydantic import BaseModel, Field
from datetime import time

class TimeSlot(BaseModel):
    """TimeSlot model representing a specific time period."""
    start_time: time = Field(description="The start time of the slot")
    end_time: time = Field(description="The end time of the slot")
    duration: int = Field(description="Duration of the slot in minutes") 