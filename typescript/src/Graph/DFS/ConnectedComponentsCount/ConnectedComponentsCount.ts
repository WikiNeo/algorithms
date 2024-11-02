interface Graph {
  [key: string]: number[]
}

// --------------------- DFS Recursion ----------------------
const connectedComponentsCount = (graph: Graph) => {
  const visited = new Set<number>();
  let count = 0

  // the in command will get key of the hash
  for (let node in graph) {
    // let's be explicit here
    if (explore(graph, node, visited) === true) {
      count += 1
    }
  }

  return count;
};

// explore function return true when it has finished exploring the graph
const explore = (graph: Graph, current: string, visited: Set<number>) => {
  // return if has visiited the node to avoid cycle
  if (visited.has(parseInt(current))) return false;

  // update visited Set
  visited.add(parseInt(current))

  // explore current neighbor
  for (let neighbor of graph[current]) {
    explore(graph, String(neighbor), visited)
  }

  return true
}

// --------------------------- DFS Stack -----------------------------
const connectedComponentsCountDFS = (graph: Graph) => {
  const visited = new Set<number>();
  let count = 0

  // the in command will get key of the hash
  for (let node in graph) {
    // let's be explicit here
    if (exploreDFS(graph, node, visited) === true) {
      count += 1
    }
  }

  return count;
};

// explore function return true when it has finished exploring the graph
const exploreDFS = (graph: Graph, src: string, visited: Set<number>) => {
  if (visited.has(parseInt(src))) return false;

  const stack = [src]

  while (stack.length > 0) {
    const current = stack.pop()
    // update visited Set
    if (current !== undefined) {
      visited.add(parseInt(current))
      // explore current neighbor
      for (let neighbor of graph[current]) {
        // return if has visited the node to avoid cycle
        if (visited.has(neighbor)) continue;

        stack.push(String(neighbor))
      }
    }

  }

  return true
}

console.log('-------------DFS----------------------')
console.log(connectedComponentsCount({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) === 2); // -> 2

console.log(connectedComponentsCount({
  1: [2],
  2: [1, 8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) === 1); // -> 1

console.log(connectedComponentsCount({})); // -> 0

console.log('-------------DFS Stack----------------------')
console.log(connectedComponentsCountDFS({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) === 2); // -> 2

console.log(connectedComponentsCountDFS({
  1: [2],
  2: [1, 8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) === 1); // -> 1

console.log(connectedComponentsCountDFS({})); // -> 0
