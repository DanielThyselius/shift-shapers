from datetime import date, time
from typing import List
from ..models import (
    Employee, TimeSlot, ShiftType, Shift, Schedule, Rules
)

# Create sample employees
employees = [
    Employee(
        name="Åsa Jansson",
        employee_number=1060,
        work_load=100
    ),
    Employee(
        name="Olle Gustavsson",
        employee_number=1040,
        work_load=80
    ),
    Employee(
        name="Anders Karlsson",
        employee_number=1050,
        work_load=100
    )
]

# Create shift types based on the XML data
shift_types = [
    ShiftType(
        id="D",
        time_slots=[
            TimeSlot(
                start_time=time(8, 45),
                end_time=time(16, 30),
                duration=465  # 7.75 hours in minutes
            )
        ]
    ),
    ShiftType(
        id="N",
        time_slots=[
            TimeSlot(
                start_time=time(21, 0),
                end_time=time(9, 15),
                duration=735  # 12.25 hours in minutes
            )
        ]
    ),
    ShiftType(
        id="E1",
        time_slots=[
            TimeSlot(
                start_time=time(14, 30),
                end_time=time(21, 30),
                duration=420  # 7 hours in minutes
            )
        ]
    )
]

# Create sample shifts for the first week
shifts = [
    # Åsa Jansson's shifts
    Shift(
        start_date=date(2025, 1, 6),  # Monday
        employee=employees[0],
        shift_type=shift_types[0]  # D shift
    ),
    Shift(
        start_date=date(2025, 1, 7),  # Tuesday
        employee=employees[0],
        shift_type=shift_types[0]  # D shift
    ),
    Shift(
        start_date=date(2025, 1, 8),  # Wednesday
        employee=employees[0],
        shift_type=shift_types[0]  # D shift
    ),
    Shift(
        start_date=date(2025, 1, 9),  # Thursday
        employee=employees[0],
        shift_type=shift_types[0]  # D shift
    ),
    Shift(
        start_date=date(2025, 1, 10),  # Friday
        employee=employees[0],
        shift_type=shift_types[1]  # N shift
    ),

    # Olle Gustavsson's shifts
    Shift(
        start_date=date(2025, 1, 6),  # Monday
        employee=employees[1],
        shift_type=shift_types[2]  # E1 shift
    ),
    Shift(
        start_date=date(2025, 1, 7),  # Tuesday
        employee=employees[1],
        shift_type=shift_types[2]  # E1 shift
    ),
    Shift(
        start_date=date(2025, 1, 8),  # Wednesday
        employee=employees[1],
        shift_type=shift_types[1]  # N shift
    ),

    # Anders Karlsson's shifts
    Shift(
        start_date=date(2025, 1, 6),  # Monday
        employee=employees[2],
        shift_type=shift_types[1]  # N shift
    ),
    Shift(
        start_date=date(2025, 1, 7),  # Tuesday
        employee=employees[2],
        shift_type=shift_types[1]  # N shift
    ),
    Shift(
        start_date=date(2025, 1, 8),  # Wednesday
        employee=employees[2],
        shift_type=shift_types[2]  # E1 shift
    )
]

# Create a schedule
schedule = Schedule(
    shifts=shift_types
)

# Create some rules
rules = Rules(
    rule="11_hour_rest",
    description="Employees must have at least 11 hours of rest between shifts",
    severity="high"
)

# Export the data
sample_data = {
    "employees": employees,
    "shift_types": shift_types,
    "shifts": shifts,
    "schedule": schedule,
    "rules": rules
} 