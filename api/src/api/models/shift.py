from pydantic import BaseModel, Field
from datetime import date
from .employee import Employee
from .shift_type import ShiftType

class Shift(BaseModel):
    """Shift model representing a work shift assignment."""
    start_date: date = Field(description="The date when the shift starts")
    employee: Employee = Field(description="The employee assigned to this shift")
    shift_type: ShiftType = Field(description="The type of shift being worked") 