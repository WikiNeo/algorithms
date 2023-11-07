import {describe, it} from 'mocha'
import {expect} from 'chai'
import BFS from "../../../src/Graph/BFS/BFS";
import Graph from "../../../src/Graph/Graph";
import GraphNode from "../../../src/Graph/GraphNode";

describe('bfs', () => {
  describe('exec', () => {
    it('should return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]', () => {
      const graph: Graph<number> = new Graph<number>()

      const node1: GraphNode<number> = new GraphNode(1);
      const node2: GraphNode<number> = new GraphNode(2);
      const node3: GraphNode<number> = new GraphNode(3);
      const node4: GraphNode<number> = new GraphNode(4);
      const node5: GraphNode<number> = new GraphNode(5);
      const node6: GraphNode<number> = new GraphNode(6);
      const node7: GraphNode<number> = new GraphNode(7);
      const node8: GraphNode<number> = new GraphNode(8);
      const node9: GraphNode<number> = new GraphNode(9);
      const node10: GraphNode<number> = new GraphNode(10);

      graph.setAdjacencyList(node1, [node2, node3, node4]);
      graph.setAdjacencyList(node2, [node5])
      graph.setAdjacencyList(node3, [node6, node7])
      graph.setAdjacencyList(node4, [node8, node9, node10])
      graph.setAdjacencyList(node5, [node6])
      graph.setAdjacencyList(node6, [])
      graph.setAdjacencyList(node7, [])
      graph.setAdjacencyList(node8, [])
      graph.setAdjacencyList(node9, [])
      graph.setAdjacencyList(node10, [])

      const bfs = new BFS<number>(graph, node1);
      bfs.exec();

      expect(bfs.resultT).deep.equal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    })
  })
})
