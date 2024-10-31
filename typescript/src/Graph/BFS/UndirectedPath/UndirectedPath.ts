// --------------------BFS queue--------------------
const undirectedPathBFS = (edges: any, nodeA: any, nodeB: any) => {
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

  const graph = buildGraph(edges);
  return hasPathBFS(graph, nodeA, nodeB)
};

const hasPathBFS = (graph: any, src: any, dst: any) => {
  // we have visited src
  const visited = new Set()
  visited.add(src)

  // for DFS, we use stack to store the data
  // initialize the stack with src
  const queue = [src]

  // while it is not empty
  while (queue.length > 0) {
    // get top
    const current = queue.shift()
    // return true if we have found the node
    if (current === dst) return true;

    for (let neighbor of graph[current]) {
      // skip if we have visited the node
      if (visited.has(neighbor)) continue;

      // add the unvisited node to Set & Stack
      visited.add(neighbor)
      queue.push(neighbor)
    }
  }

  return false;
}

// TODO: add to UT
const edges = [
  ['i', 'j'],
  ['k', 'i'],
  ['m', 'k'],
  ['k', 'l'],
  ['o', 'n']
];


console.log('-----BFS Queue---------')
console.log(undirectedPathBFS(edges, 'j', 'm')); // -> true
console.log(undirectedPathBFS(edges, 'm', 'j')); // -> true
console.log(undirectedPathBFS(edges, 'l', 'j')); // -> true
console.log(undirectedPathBFS(edges, 'k', 'o')); // -> false
console.log(undirectedPathBFS(edges, 'i', 'o')); // -> false
