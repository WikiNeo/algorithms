enum NodeColor {
  WHITE,
  GRAY,
  BLACK
}

class GraphNode<T> {
  value: T;
  // number of incoming edges
  incomeEdge: number;
  // distance from the source node
  distance: number;
  // parent node
  parent: GraphNode<T> | null;
  color: NodeColor;

  constructor(value: T) {
    this.value = value;
    this.incomeEdge = 0;
    this.distance = Infinity;
    this.parent = null;
    this.color = NodeColor.WHITE;
  }

  isWhite(): boolean{
    return this.color === NodeColor.WHITE;
  }

  setNodeWhite(){
    this.color = NodeColor.WHITE;
  }

  setNodeGray(){
    this.color = NodeColor.GRAY;
  }

  setNodeBlack(){
    this.color = NodeColor.BLACK;
  }

  setParent(parent: GraphNode<T> | null){
    this.parent = parent;
  }

  setDistance(distance: number){
    this.distance = distance;
  }

  setIncomeEdge(num: number){
    this.incomeEdge = num;
  }

  hasNoIncomeEdge(): boolean {
    return this.incomeEdge === 0;
  }

  decreaseIncomeEdge(): void {
    this.incomeEdge--;
  }

  increaseIncomeEdge(): void {
    this.incomeEdge++;
  }
}

export {NodeColor};

export default GraphNode;
