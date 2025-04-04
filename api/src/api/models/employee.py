from pydantic import BaseModel, Field

class Employee(BaseModel):
    """Employee model representing a worker in the system."""
    name: str = Field(description="The name of the employee")
    employee_number: int = Field(description="The unique identifier for the employee")
    work_load: int = Field(
        default=100,
        ge=1,
        le=100,
        description="Percentage of normal full time work (1-100)"
    ) 