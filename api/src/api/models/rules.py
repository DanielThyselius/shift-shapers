from pydantic import BaseModel, Field

class Rules(BaseModel):
    """Rules model representing scheduling rules and constraints."""
    rule: str = Field(description="The rule identifier or name")
    description: str = Field(description="Detailed description of the rule")
    severity: str = Field(description="Severity level of the rule (e.g., high, medium, low)") 