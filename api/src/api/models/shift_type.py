from pydantic import BaseModel, Field
from typing import List
from .time_slot import TimeSlot

class ShiftType(BaseModel):
    """ShiftType model representing a type of work shift."""
    id: str = Field(description="Unique identifier for the shift type")
    time_slots: List[TimeSlot] = Field(description="List of time slots for this shift type") 