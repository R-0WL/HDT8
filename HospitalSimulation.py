import simpy
import random

class HospitalSimulation:
    def __init__(self, numReceptionist, numDoctors, numSurgeons, numSpecialists, patientsFile):
        self.numReceptionist = numReceptionist
        self.numDoctors = numDoctors
        self.numSurgeons = numSurgeons
        self.numSpecialists = numSpecialists
        self.patientsFile = patientsFile
        self.env = simpy.Environment()

        self.receptionists = simpy.Resource(self.env, self.numReceptionist)
        self.doctors = simpy.Resource(self.env, self.numDoctors)
        self.surgeons = simpy.Resource(self.env, self.numSurgeons)
        self.specialists = simpy.Resource(self.env, self.numSpecialists)

    def load_patients_from_txt(self): # Cargar pacientes desde un archivo de texto
        # El archivo debe tener el siguiente formato:
        patients = []
        with open(self.patientsFile, 'r') as file:
            for line in file:
                fields = line.strip().split(',')
                patient_code = int(fields[0])
                full_name = fields[1]
                symptoms = fields[2]  # Sintoma principal
                priority = fields[3]  # Prioridad A, B, C, D, E
                patients.append((patient_code, full_name, symptoms, priority))
        return patients

    def patient_arrival(self, patient_id, priority):
        arrival_time = random.randint(1, 10)  # Tiempo aleatorio de llegada
        yield self.env.timeout(arrival_time)
        print(f"Paciente {patient_id} con prioridad {priority} llegó al hospital en {self.env.now} minutos")

    def receptionist_task(self, patient_id):
        with self.receptionists.request() as request:
            yield request
            process_time = random.uniform(5, 10)  # Tiempo aleatorio de atención
            yield self.env.timeout(process_time)
            print(f"Recepcionista atendió al paciente {patient_id} en {self.env.now} minutos")

    def doctor_task(self, patient_id):
        with self.doctors.request() as request:
            yield request
            process_time = random.uniform(10, 20)
            yield self.env.timeout(process_time)
            print(f"Doctor atendió al paciente {patient_id} en {self.env.now} minutos")

    def surgeon_task(self, patient_id):
        with self.surgeons.request() as request:
            yield request
            process_time = random.uniform(30, 60)  # Cirugía más larga
            yield self.env.timeout(process_time)
            print(f"Cirujano atendió al paciente {patient_id} en {self.env.now} minutos")

    def specialist_task(self, patient_id):
        with self.specialists.request() as request:
            yield request
            process_time = random.uniform(20, 40)
            yield self.env.timeout(process_time)
            print(f"Especialista atendió al paciente {patient_id} en {self.env.now} minutos")

    def run_simulation(self, patients):
        for patient_id, full_name, symptoms, priority in patients:
            self.env.process(self.patient_arrival(patient_id, priority))

            # Atender pacientes según su prioridad
            if priority == 'A':
                self.env.process(self.receptionist_task(patient_id))
                self.env.process(self.doctor_task(patient_id))
                self.env.process(self.surgeon_task(patient_id))  # Cirugía de emergencia
            elif priority == 'B':
                self.env.process(self.receptionist_task(patient_id))
                self.env.process(self.doctor_task(patient_id))
            elif priority == 'C':
                self.env.process(self.receptionist_task(patient_id))
                self.env.process(self.doctor_task(patient_id))
                self.env.process(self.specialist_task(patient_id))
            else:
                self.env.process(self.receptionist_task(patient_id))

        self.env.run()


# Cargar la lista de pacientes para la simulación
#sim = HospitalSimulation(numReceptionist=2, numDoctors=3, numSurgeons=1, numSpecialists=2, patientsFile='patients_for_simulation.txt')
sim = HospitalSimulation(numReceptionist=2, numDoctors=3, numSurgeons=1, numSpecialists=2, patientsFile='./patientSimulation.txt')
patients = sim.load_patients_from_txt()
sim.run_simulation(patients)
