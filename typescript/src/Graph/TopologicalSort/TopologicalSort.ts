import Graph from "../Graph";
import GraphNode from "../GraphNode";

class TopologicalSort<T> {
  graph: Graph<T>;

  resultT: T[];

  constructor(graph: Graph<T>) {
    this.graph = graph;
    this.resultT = []
  }

  /*
  L ← Empty list that will contain the sorted elements
  S ← Set of all nodes with no incoming edge

  while S is not empty do
      remove a node n from S
      add n to L
      for each node m with an edge e from n to m do
          remove edge e from the graph
          if m has no other incoming edges then
              insert m into S

  if graph has edges then
      return error   (graph has at least one cycle)
  else
      return L   (a topologically sorted order)
   */
  execKahnBFS(){
    // node queue that has no incoming edge
    const queue: GraphNode<T>[] = []
    for(const node of this.graph.getNodeKeys()){
      if(node.hasNoIncomeEdge()){
        queue.push(node)
      }
    }

    while(queue.length > 0){
      // @ts-ignore
      const frontNode: GraphNode<T> = queue.shift();
      this.resultT.push(frontNode.value)

      for(const neighbourNode of this.graph.getNeighbours(frontNode)){
        neighbourNode.decreaseIncomeEdge();
        if(neighbourNode.hasNoIncomeEdge()){
          queue.push(neighbourNode);
        }
      }
    }
  }

  /*
  L ← Empty list that will contain the sorted nodes
  while exists nodes without a permanent mark do
      select an unmarked node n
      visit(n)

  function visit(node n)
      if n has a permanent mark then
          return
      if n has a temporary mark then
          stop   (not a DAG)

      mark n with a temporary mark

      for each node m with an edge from n to m do
          visit(m)

      remove temporary mark from n
      mark n with a permanent mark
      add n to head of L
   */
  execDFS(){
    const visiting: Set<GraphNode<T>> = new Set<GraphNode<T>>();
    const visited: Set<GraphNode<T>> = new Set<GraphNode<T>>();

    const dfs = (node: GraphNode<T>): boolean => {
      // has cycle
      if(visiting.has(node)) return false;
      // done dfs for node
      if(visited.has(node)) return true;

      visiting.add(node)

      for(let neighbour of this.graph.getNeighbours(node)){
        if(!visited.has(neighbour)){
          if(!dfs(neighbour)) return false;
        }
      }
      visiting.delete(node)
      visited.add(node)

      this.resultT.unshift(node.value)

      return true;
    }

    for(const node of this.graph.getNodeKeys()){
      if(!dfs(node)) {
        return this.resultT = []
      }
    }

  }
}

export default TopologicalSort;
