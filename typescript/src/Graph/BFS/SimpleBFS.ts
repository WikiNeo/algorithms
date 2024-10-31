/*
 * For breadth first traversal, we use a queue to store our data.
 *  1. Similar to the DFS, we start with source in the queue.
 *  2. While the queue is not empty, we dequeue/shift the value from front, then enqueue/push the neighbors to the //#endregion
 *  3. repeat step 2
 */
const breadthFirstTraversal = (graph: any, source: any) => {
  // start with source in queue
  const queue = [source]
  const visited = new Set();
  visited.add(source)

  // as long as the queue is not empty
  while (queue.length > 0) {
    // we dequeue the data
    const current = queue.shift()
    visited.add(current)
    console.log(current)

    // enqueue the neighbours of the data
    for (let neighbour of graph[current]) {
      if (!visited.has(neighbour)) {
        queue.push(neighbour)
      }
    }
  }
}
