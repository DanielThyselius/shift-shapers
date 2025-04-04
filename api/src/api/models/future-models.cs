public class Employee {
    public string Name { get; set; }
    public int EmployeeNumber { get; set; }
    public int WorkLoad { get; set; } = 100; // percentage of normal full time work (1-100)
}

// AI is allowed to change the schedule
public class Schedule {
    public List<ShiftType> Shifts { get; set; }
}
public class Shift {
    public string StartDate { get; set; }
    public Employee Employee { get; set; }
    public ShiftType ShiftType { get; set; }
}

public class ShiftType {
    public string Id { get; set; }
    public List<TimeSlot> TimeSlots { get; set; }

public class Slot {
    public TimeSpan StartTime { get; set; }
    public TimeSpan EndTime { get; set; }
    public int Duration { get; set; }
}

public class Rules {
    public string Rule { get; set; }
    public string Description { get; set; }
    public string Severity { get; set; }
}

