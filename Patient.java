import java.util.ArrayList;

public class Patient implements Comparable<Patient> {
    private int patientCode;
    private String fullName;
    private String apellidos;
    private String names;
    private int edad;
    private String direccion;
    private String telefono;
    private String email;
    private String fechaNacimiento;
    private String fechaIngreso;
    private String fechaSalida;
    private String horaIngreso;
    private String horaSalida;
    private String sintomaPrincipal;
    private ArrayList<String> sintomasGenerales;
    private char codigoEmergencia; // A, B, C, D, E
    private byte estado; // 0: No atendido, 1: En espera, 2: Atendido

    public Patient(int patientCode, String fullName, String apellidos, String names, int edad, String direccion,
                   String telefono, String email, String fechaNacimiento, String fechaIngreso, String fechaSalida,
                   String horaIngreso, String horaSalida, String sintomaPrincipal, ArrayList<String> sintomasGenerales,
                   char codigoEmergencia, byte estado) {
        this.patientCode = patientCode;
        this.fullName = fullName;
        this.apellidos = apellidos;
        this.names = names;
        this.edad = edad;
        this.direccion = direccion;
        this.telefono = telefono;
        this.email = email;
        this.fechaNacimiento = fechaNacimiento;
        this.fechaIngreso = fechaIngreso;
        this.fechaSalida = fechaSalida;
        this.horaIngreso = horaIngreso;
        this.horaSalida = horaSalida;
        this.sintomaPrincipal = sintomaPrincipal;
        this.sintomasGenerales = sintomasGenerales;
        this.codigoEmergencia = codigoEmergencia;
        this.estado = estado;
    }

    public int getPatientCode() {
        return patientCode;
    }

    public char getCodigoEmergencia() {
        return codigoEmergencia;
    }

    @Override
    public int compareTo(Patient other) {
        return Character.compare(this.codigoEmergencia, other.codigoEmergencia);
    }

    @Override
    public String toString() {
        return patientCode + "," + fullName + "," + apellidos + "," + names + "," + edad + "," + direccion + ","
                + telefono + "," + email + "," + fechaNacimiento + "," + fechaIngreso + "," + fechaSalida + ","
                + horaIngreso + "," + horaSalida + "," + sintomaPrincipal + "," + String.join(";", sintomasGenerales) + ","
                + codigoEmergencia + "," + estado;
    }
}
