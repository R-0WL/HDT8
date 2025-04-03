// Implementación de la Cola de Prioridad basada en un Heap (ADT)
import java.util.Vector;

public class HeapPriorityQueue<E extends Comparable<E>> implements PriorityQueueADT<E> {
    private Vector<E> heap;

    public HeapPriorityQueue() {
        heap = new Vector<>();
    }

    @Override
    public void enqueue(E item) {
        heap.add(item); // Añadir al final
        upHeap(heap.size() - 1); // Ajustar el heap
    }

    @Override
    public E dequeue() {
        if (heap.isEmpty()) return null;

        E result = heap.get(0);
        E lastItem = heap.remove(heap.size() - 1);

        if (!heap.isEmpty()) {
            heap.set(0, lastItem); // Reemplazar la raíz
            downHeap(0); // Ajustar el heap
        }

        return result;
    }

    @Override
    public boolean isEmpty() {
        return heap.isEmpty();
    }

    private void upHeap(int index) {
        E item = heap.get(index);
        while (index > 0) {
            int parent = (index - 1) / 2;
            E parentItem = heap.get(parent);
            if (item.compareTo(parentItem) >= 0) break;
            heap.set(index, parentItem);
            index = parent;
        }
        heap.set(index, item);
    }

    private void downHeap(int index) {
        int child;
        E item = heap.get(index);
        int size = heap.size();

        while (index < size / 2) {
            child = 2 * index + 1;
            int rightChild = child + 1;
            if (rightChild < size && heap.get(child).compareTo(heap.get(rightChild)) > 0) {
                child = rightChild;
            }
            if (item.compareTo(heap.get(child)) <= 0) break;
            heap.set(index, heap.get(child));
            index = child;
        }
        heap.set(index, item);
    }
}