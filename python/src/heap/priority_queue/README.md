# Priority Queue

## Priority Queue Implementation Notes (Python)

A priority queue is common use for a heap, and it presents several implementation
challenges:

- Sort stability: how do you get two tasks with equal priorities to be returned in the order they were originally added?
- Tuple comparison breaks for (priority, task) pairs if the priorities are equal and the tasks do not have a default comparison order.
- If the priority of a task changes, how do you move it to a new position in the heap?
- Or if a pending task needs to be deleted, how do you find it and remove it from the queue?

A solution to the first two challenges is to store entries as 3-element list including
the priority, an entry count, and the task. The entry count serves as a tie-breaker so
that two tasks with the same priority are returned in the order they were added. And
since no two entry counts are the same, the tuple comparison will never attempt to
directly compare two tasks.

The remaining challenges revolve around finding a pending task and making changes to its
priority or removing it entirely. Finding a task can be done with a dictionary pointing
to an entry in the queue.

Removing the entry or changing its priority is more difficult because it would break the
heap structure invariants. So, a possible solution is to mark the entry as removed and
add a new entry with the revised priority

## Wikipedia

In computer science, a priority queue is an abstract data-type similar to a regular queue or stack data structure.
Each element in a priority queue has an associated priority. In a priority queue, elements with high priority are
served before elements with low priority. In some implementations, if two elements have the same priority, they are
served in the same order in which they were enqueued.

## References

- [https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes](https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes)
- [https://en.wikipedia.org/wiki/Priority_queue](https://en.wikipedia.org/wiki/Priority_queue)
