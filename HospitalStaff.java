public class HospitalStaff {
    protected String name;
    protected double costPerHour;
    protected double averageTaskTime;
    protected int workingHours;

    public HospitalStaff(String name, double costPerHour, double averageTaskTime, int workingHours) {
        this.name = name;
        this.costPerHour = costPerHour;
        this.averageTaskTime = averageTaskTime;
        this.workingHours = workingHours;
    }

    public double calculateDailyCost() {
        return costPerHour * workingHours;
    }

    public String getRole() {
        return "General Staff";
    }
}

class Receptionist extends HospitalStaff {
    public Receptionist(String name, double costPerHour, double averageTaskTime, int workingHours) {
        super(name, costPerHour, averageTaskTime, workingHours);
    }

    @Override
    public String getRole() {
        return "Receptionist";
    }
}

class GeneralDoctor extends HospitalStaff {
    public GeneralDoctor(String name, double costPerHour, double averageTaskTime, int workingHours) {
        super(name, costPerHour, averageTaskTime, workingHours);
    }

    @Override
    public String getRole() {
        return "General Doctor";
    }
}

class Surgeon extends HospitalStaff {
    public Surgeon(String name, double costPerHour, double averageTaskTime, int workingHours) {
        super(name, costPerHour, averageTaskTime, workingHours);
    }

    @Override
    public String getRole() {
        return "Surgeon";
    }
}

class Specialist extends HospitalStaff {
    public Specialist(String name, double costPerHour, double averageTaskTime, int workingHours) {
        super(name, costPerHour, averageTaskTime, workingHours);
    }

    @Override
    public String getRole() {
        return "Specialist";
    }
}
