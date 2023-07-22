#include <stdio.h>
#include <stdbool.h>

#define MAX_FRAMES 10

// Implementación de la cola circular
typedef struct {
    int front;
    int rear;
    int arr[MAX_FRAMES];
} Queue;

bool isQueueFull(Queue *queue) {
    return ((queue->rear + 1) % MAX_FRAMES == queue->front);
}

bool isQueueEmpty(Queue *queue) {
    return (queue->front == -1);
}

void enqueue(Queue *queue, int item) {
    if (isQueueFull(queue)) {
        return;
    }

    if (isQueueEmpty(queue)) {
        queue->front = 0;
    }

    queue->rear = (queue->rear + 1) % MAX_FRAMES;
    queue->arr[queue->rear] = item;
}

int dequeue(Queue *queue) {
    if (isQueueEmpty(queue)) {
        return -1;
    }

    int item = queue->arr[queue->front];
    if (queue->front == queue->rear) {
        queue->front = -1;
        queue->rear = -1;
    } else {
        queue->front = (queue->front + 1) % MAX_FRAMES;
    }

    return item;
}

// Function to find page faults using FIFO
int pageFaults(int incomingStream[], int n, int frames) {
    printf("Incoming \t pages\n");

    // Using an array to quickly check if a given incoming
    // stream item is in the array or not.
    bool present[MAX_FRAMES] = {false};

    // Queue created to store pages in FIFO manner
    Queue queue;
    queue.front = -1;
    queue.rear = -1;

    int page_faults = 0;
    for (int i = 0; i < n; i++) {
        // If the array has fewer items than frames
        // i.e. the array can hold more items.
        if (queue.rear < frames - 1) {
            // If the incoming item is not present, add it to the array.
            if (!present[incomingStream[i]]) {
                present[incomingStream[i]] = true;
                enqueue(&queue, incomingStream[i]);

                // Increment page fault
                page_faults++;

                // Print incoming page and the pages in the queue.
                printf("%d\t\t", incomingStream[i]);
                for (int j = queue.front; j != queue.rear; j = (j + 1) % MAX_FRAMES) {
                    printf("%d\t", queue.arr[j]);
                }
                printf("%d\t", queue.arr[queue.rear]);
                printf("\n");
            }
        } else { // If the array is full, we need to do page replacement in FIFO manner.
            // If the incoming item is not present.
            if (!present[incomingStream[i]]) {
                int val = dequeue(&queue);

                // Remove it from the array.
                present[val] = false;

                // Insert incoming page into the array.
                present[incomingStream[i]] = true;
                enqueue(&queue, incomingStream[i]);

                // Increment page faults.
                page_faults++;

                // Print incoming page and the pages in the queue.
                printf("%d\t\t", incomingStream[i]);
                for (int j = queue.front; j != queue.rear; j = (j + 1) % MAX_FRAMES) {
                    printf("%d\t", queue.arr[j]);
                }
                printf("%d\t", queue.arr[queue.rear]);
                printf("\n");
            }
        }
    }
    return page_faults;
}

int main() {
    int incomingStream[] = {7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1};
    int n = sizeof(incomingStream) / sizeof(incomingStream[0]);
    int frames = 3;

    int page_faults = pageFaults(incomingStream, n, frames);
    int hits = n - page_faults;

    printf("\nPage Faults: %d\n", page_faults);
    printf("Hit: %d\n", hits);

    return 0;
}
