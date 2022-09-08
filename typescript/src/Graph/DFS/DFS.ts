import Graph from "../Graph";
import GraphNode from "../GraphNode";

class DFS<T>{
  graph: Graph<T>;
  startNode: GraphNode<T>

  visited: Set<GraphNode<T>>

  resultT: T[];

  constructor(graph: Graph<T>, startNode: GraphNode<T>) {
    this.graph = graph;
    this.startNode = startNode;
    this.visited = new Set<GraphNode<T>>();
    this.resultT = []
  }

  /*
  procedure DFS(G, v) is
    label v as discovered
    for all directed edges from v to w that are in G.adjacentEdges(v) do
        if vertex w is not labeled as discovered then
            recursively call DFS(G, w)
   */
  execRecursive(node: GraphNode<T>){
    this.visited.add(node)
    this.resultT.push(node.value)

    for(let neighbourNode of this.graph.getNeighbours(node)){
      if(!this.visited.has(neighbourNode)){
        this.execRecursive(neighbourNode)
      }
    }
  }

  /*
  procedure DFS_iterative(G, v) is
    let S be a stack
    S.push(v)
    while S is not empty do
        v = S.pop()
        if v is not labeled as discovered then
            label v as discovered
            for all edges from v to w in G.adjacentEdges(v) do
                S.push(w)
   */
  execIterative(){
    const stack: GraphNode<T>[] = []
    stack.push(this.startNode)

    while(stack.length > 0){
      // @ts-ignore
      const topNode: GraphNode<T> = stack.pop()

      if(!this.visited.has(topNode)){
        this.resultT.push(topNode.value)
        this.visited.add(topNode)
        for(let neighbourNode of this.graph.getNeighbours(topNode)){
          stack.push(neighbourNode)
        }
      }
    }
  }
}

export default DFS;
