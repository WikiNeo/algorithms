const buildGraph = (edges: any) => {
  const graph: any = {}

  for (let edge of edges) {
    const [a, b] = edge;

    if (!(a in graph)) graph[a] = []
    if (!(b in graph)) graph[b] = []

    graph[a].push(b)
    graph[b].push(a)
  }

  return graph;
}

// ------------------------ DFS recursive ---------------------
const undirectedPath = (edges: any, nodeA: any, nodeB: any) => {
  const graph = buildGraph(edges);
  return hasPath(graph, nodeA, nodeB, new Set())
};

const hasPath = (graph: any, src: any, dst: any, visited: any) => {
  // if we find the path, return true
  if (src === dst) return true;
  // if we have already visited the node, return false.
  if (visited.has(src)) return false;

  // add the node to the visited
  visited.add(src)

  // then we visit the neighbors
  for (let neighbor of graph[src]) {
    if (hasPath(graph, neighbor, dst, visited) === true) {
      return true
    }
  }

  return false
}

// -------------------- DFS stack ----------------------------
const undirectedPathDFS = (edges: any, nodeA: any, nodeB: any) => {
  const graph = buildGraph(edges);
  return hasPathDFS(graph, nodeA, nodeB)
};

const hasPathDFS = (graph: any, src: any, dst: any) => {
  // we have visited src
  const visited = new Set()
  visited.add(src)

  // for DFS, we use stack to store the data
  // initialize the stack with src
  const stack = [src]

  // while it is not empty
  while (stack.length > 0) {
    // get top
    const current = stack.pop()
    // return true if we have found the node
    if (current === dst) return true;

    for (let neighbor of graph[current]) {
      // skip if we have visited the node
      if (visited.has(neighbor)) continue;

      // add the unvisited node to Set & Stack
      visited.add(neighbor)
      stack.push(neighbor)
    }
  }

  return false;
}

// TODO: add the following to UT
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];

console.log('-----DFS Recursion---------')
console.log(undirectedPath(edges, 'j', 'm')); // -> true
console.log(undirectedPath(edges, 'm', 'j')); // -> true
console.log(undirectedPath(edges, 'l', 'j')); // -> true
console.log(undirectedPath(edges, 'k', 'o')); // -> false
console.log(undirectedPath(edges, 'i', 'o')); // -> false

console.log('-----DFS Stack---------')
console.log(undirectedPathDFS(edges, 'j', 'm')); // -> true
console.log(undirectedPathDFS(edges, 'm', 'j')); // -> true
console.log(undirectedPathDFS(edges, 'l', 'j')); // -> true
console.log(undirectedPathDFS(edges, 'k', 'o')); // -> false
console.log(undirectedPathDFS(edges, 'i', 'o')); // -> false
