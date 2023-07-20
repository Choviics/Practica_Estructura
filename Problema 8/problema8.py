# Python3 implementation of FIFO page
from queue import Queue


# Function to find page faults using FIFO
def pageFaults(incomingStream, n, frames):
    print("Incoming \t pages")
    # Using Hashset to quickly check if a given
    # incoming stream item in set or not
    s = set()

    # Queue created to store pages in FIFO manner
    # since set will not store order or entry
    # we will use queue to note order of entry of incoming page
    queue = Queue()

    page_faults = 0
    for i in range(n):

        # if set has lesser item than frames
        # i.e. set can hold more items
        if len(s) < frames:

            # If incoming item is not present, add to set
            if incomingStream[i] not in s:
                s.add(incomingStream[i])

                # increment page fault 
                page_faults += 1

                # Push the incoming page into the queue
                queue.put(incomingStream[i])

        # If the set is full then we need to do page replacement
        # in FIFO manner that is remove first item from both
        # set and queue then insert incoming page
        else:

            # If incoming item is not present
            if incomingStream[i] not in s:
                # remove the first page from the queue
                val = queue.queue[0]

                queue.get()

                # Remove from set
                s.remove(val)

                # insert incoming page to set
                s.add(incomingStream[i])

                # push incoming page to queue
                queue.put(incomingStream[i])

                # Increment page faults 
                page_faults += 1

        print(incomingStream[i], end="\t\t")
        for q_item in queue.queue:
            print(q_item, end="\t")

        print()
    return page_faults


# Driver code
incomingStream = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
n = len(incomingStream)
frames = 3
page_faults = pageFaults(incomingStream, n, frames)
hits = n - page_faults

print("\nPage Faults: " + str(page_faults))
print("Hit: " + str(hits))