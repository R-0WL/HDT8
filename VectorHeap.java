import java.util.Vector;

public class VectorHeap<E extends Comparable<E>> implements PriorityQueue<E> {
    private Vector<E> heap;

    public VectorHeap() {
        heap = new Vector<>();
    }

    @Override
    public void add(E item) {
        heap.add(item); // Agrega el elemento al final
        upHeap(heap.size() - 1); // Reajusta la estructura del heap
    }

    @Override
    public E remove() {
        if (heap.isEmpty()) return null;
        
        E result = heap.get(0); // El primer elemento es el de mayor prioridad
        E lastItem = heap.remove(heap.size() - 1); // El último elemento

        if (!heap.isEmpty()) {
            heap.set(0, lastItem); // Coloca el último elemento en la raíz
            downHeap(0); // Reajusta la estructura del heap
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
        
        while (index < size / 2) { // Si tiene hijos
            child = 2 * index + 1; // Hijo izquierdo
            int rightChild = child + 1;
            if (rightChild < size && heap.get(child).compareTo(heap.get(rightChild)) > 0) {
                child = rightChild; // Si el hijo derecho es más pequeño, lo elegimos
            }
            if (item.compareTo(heap.get(child)) <= 0) break;
            heap.set(index, heap.get(child));
            index = child;
        }
        heap.set(index, item);
    }
}