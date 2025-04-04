import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

RANDOM_SEED = 10  # Semilla para generación de números aleatorios
random.seed(RANDOM_SEED)

# Parámetros de simulación
INTERVALOS = [10, 5, 1]  # Intervalos de llegada de pacientes
PACIENTES_DIAS = [25, 50, 100, 150, 200]  # Cantidad de pacientes
ENFERMERAS_CANT = [1, 2, 3]  # Número de enfermeras disponibles
DOCTORES_CANT = [1, 2, 3]  # Número de doctores disponibles
LABORATORIOS_CANT = [1, 2]  # Equipos de laboratorio
RAYOSX_CANT = [1, 2]  # Equipos de rayos X

# Tiempos de atención en cada etapa
TRIAGE_TIEMPO = 10
CONSULTA_TIEMPO = 15
LABORATORIO_TIEMPO = 20
RAYOSX_TIEMPO = 25

def paciente(env, nombre, enfermeras, doctores, laboratorio, rayosX, resultados):
    llegada = env.now

    # TRIAGE: Evaluación por enfermera
    with enfermeras.request() as req:
        yield req
        yield env.timeout(TRIAGE_TIEMPO)
        severidad = random.randint(1, 5)  # Prioridad 1 (crítico) a 5 (leve)
    
    # CONSULTA MÉDICA: Atendido por un doctor según prioridad
    with doctores.request(priority=severidad) as req:
        yield req
        yield env.timeout(CONSULTA_TIEMPO)

    # DECISIÓN: Necesita laboratorio o rayos X?
    if random.random() < 0.5:  # 50% de probabilidad de necesitar laboratorio
        with laboratorio.request(priority=severidad) as req:
            yield req
            yield env.timeout(LABORATORIO_TIEMPO)
    
    if random.random() < 0.3:  # 30% de probabilidad de necesitar rayos X
        with rayosX.request(priority=severidad) as req:
            yield req
            yield env.timeout(RAYOSX_TIEMPO)

    # PACIENTE ATENDIDO
    resultados.append(env.now - llegada)

def generar_pacientes(env, intervalo, num_pacientes, enfermeras, doctores, laboratorio, rayosX, resultados):
    for i in range(num_pacientes):
        env.process(paciente(env, f'Paciente-{i}', enfermeras, doctores, laboratorio, rayosX, resultados))
        yield env.timeout(random.expovariate(1.0 / intervalo))

def correr_simulacion(intervalo, num_pacientes, enfermeras_cant, doctores_cant, laboratorios_cant, rayosx_cant):
    env = simpy.Environment()
    
    enfermeras = simpy.Resource(env, capacity=enfermeras_cant)
    doctores = simpy.PriorityResource(env, capacity=doctores_cant)
    laboratorio = simpy.PriorityResource(env, capacity=laboratorios_cant)
    rayosX = simpy.PriorityResource(env, capacity=rayosx_cant)

    resultados = []
    
    env.process(generar_pacientes(env, intervalo, num_pacientes, enfermeras, doctores, laboratorio, rayosX, resultados))
    env.run()

    return np.mean(resultados), np.std(resultados)

def main():
    for enfermeras in ENFERMERAS_CANT:
        for doctores in DOCTORES_CANT:
            for laboratorios in LABORATORIOS_CANT:
                for rayosX in RAYOSX_CANT:
                    plt.figure()

                    for intervalo in INTERVALOS:
                        tiempos = []
                        
                        for pacientes in PACIENTES_DIAS:
                            promedio, _ = correr_simulacion(intervalo, pacientes, enfermeras, doctores, laboratorios, rayosX)
                            tiempos.append(promedio)
                        
                        plt.plot(PACIENTES_DIAS, tiempos, marker='o', label=f'Intervalo {intervalo}')
                    
                    plt.xlabel('Número de pacientes')
                    plt.ylabel('Tiempo promedio en el sistema')
                    plt.title(f'Enfermeras: {enfermeras}, Doctores: {doctores}, Lab: {laboratorios}, RayosX: {rayosX}')
                    plt.legend()
                    plt.show()

if __name__ == '__main__':
    main()
