interface Graph {
  [key: string]: number[]
}


// --------------------------- BFS Queue -----------------------------
const connectedComponentsCountBFS = (graph: Graph) => {
  const visited = new Set<number>();
  let count = 0

  // the in command will get key of the hash
  for (let node in graph) {
    // let's be explicit here
    if (exploreBFS(graph, node, visited) === true) {
      count += 1
    }
  }

  return count;
};

// explore function return true when it has finished exploring the graph
const exploreBFS = (graph: Graph, src: string, visited: Set<number>) => {
  if (visited.has(parseInt(src))) return false;

  const queue = [src]

  while (queue.length > 0) {
    const current = queue.shift()
    if (current !== undefined) {
      // update visited Set
      visited.add(parseInt(current))

      // explore current neighbor
      for (let neighbor of graph[current]) {
        // continue if has visited the node to avoid cycle
        if (visited.has(neighbor)) continue;
        queue.push(String(neighbor))
      }
    }
  }

  return true
}

console.log('-------------BFS Stack----------------------')
console.log(connectedComponentsCountBFS({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) === 2); // -> 2

console.log(connectedComponentsCountBFS({
  1: [2],
  2: [1, 8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) === 1); // -> 1

console.log(connectedComponentsCountBFS({}) === 0); // -> 0

export { }
