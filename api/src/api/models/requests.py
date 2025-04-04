from pydantic import BaseModel, Field
from typing import Any

class MessageResponse(BaseModel):
    message: str

class EmployeeCreateRequest(BaseModel):
    name: str
    employee_number: str
    known_absences: list[str] = Field(default_factory=list)  # ISO format dates
    metadata: dict[str, Any] = Field(default_factory=dict)

class ScheduleCreateRequest(BaseModel):
    date: str  # ISO format date
    first_line_support: str  # Employee number

class RulesUpdateRequest(BaseModel):
    max_days_per_week: int | None = None
    preferred_balance: float | None = None 