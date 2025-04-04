from pydantic import BaseModel, Field
from typing import List
from .shift_type import ShiftType

class Schedule(BaseModel):
    """Schedule model representing a collection of shifts."""
    shifts: List[ShiftType] = Field(description="List of shift types in the schedule") 