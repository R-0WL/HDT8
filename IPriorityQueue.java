// Interfaz general para una Cola de Prioridad
public interface IPriorityQueue<E extends Comparable<E>> {
    void enqueue(E item); // Agregar un elemento a la cola
    E dequeue();          // Extraer el elemento de mayor prioridad
    boolean isEmpty();    // Verificar si la cola está vacía
}