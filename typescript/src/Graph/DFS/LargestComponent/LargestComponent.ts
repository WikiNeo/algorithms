interface Graph {
  [key: string]: number[]
}

// ------------------ DFS Recursion -----------------------------------------
const largestComponent = (graph: Graph) => {
  const visited = new Set<number>()
  let largestSize = 0;

  for (let node in graph) {
    const size = countComponentSize(graph, node, visited)
    if (size > largestSize) {
      largestSize = size;
    }
  }

  return largestSize;
};

const countComponentSize = (graph: Graph, src: string, visited: Set<number>) => {
  // the base case should also return the size
  if (visited.has(parseInt(src))) return 0;

  // update visited & size here
  visited.add(parseInt(src))
  let size = 1;

  for (let neighbor of graph[src]) {
    size += countComponentSize(graph, String(neighbor), visited)
  }

  return size;
}

// ------------------ DFS Stack ---------------------------------------
const largestComponentDFS = (graph: Graph) => {
  const visited = new Set<number>()
  let largestSize = 0;

  for (let node in graph) {
    const size = countComponentSizeDFS(graph, node, visited)
    if (size > largestSize) {
      largestSize = size;
    }
  }

  return largestSize;
};

const countComponentSizeDFS = (graph: Graph, src: string, visited: Set<number>) => {
  // the base case should also return the size
  if (visited.has(parseInt(src))) return 0;

  let size = 0;
  // add src to stack & visited.
  const stack = [src]
  visited.add(parseInt(src))

  while (stack.length > 0) {
    const current = stack.pop();
    if (current === undefined) continue;
    size += 1;

    for (let neighbor of graph[current]) {
      if (visited.has(neighbor)) continue;
      // if not visited, add it
      visited.add(neighbor)
      stack.push(String(neighbor))
    }

  }

  return size;
}

console.log("------------DFS Stack-------")
console.log(largestComponent({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) === 4);

console.log(largestComponent({
  1: [2],
  2: [1, 8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) === 6);

console.log(largestComponent({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) === 5);

console.log(largestComponent({}) === 0)

console.log(largestComponent({
  0: [4, 7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) === 3);


console.log("------------DFS Stack-------")
console.log(largestComponentDFS({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) === 4);

console.log(largestComponentDFS({
  1: [2],
  2: [1, 8],
  6: [7],
  9: [8],
  7: [6, 8],
  8: [9, 7, 2]
}) === 6);

console.log(largestComponentDFS({
  3: [],
  4: [6],
  6: [4, 5, 7, 8],
  8: [6],
  7: [6],
  5: [6],
  1: [2],
  2: [1]
}) === 5);

console.log(largestComponentDFS({}) === 0)

console.log(largestComponentDFS({
  0: [4, 7],
  1: [],
  2: [],
  3: [6],
  4: [0],
  6: [3],
  7: [0],
  8: []
}) === 3);
