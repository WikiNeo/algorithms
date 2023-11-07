import {describe, it} from "mocha";
import Graph from "../../../src/Graph/Graph";
import GraphNode from "../../../src/Graph/GraphNode";
import {expect} from "chai";
import TopologicalSort from "../../../src/Graph/TopologicalSort/TopologicalSort";

describe('topological sort', () => {
  describe('Kahn BFS', () => {
    it('should return correct order', () => {
      const graph: Graph<number> = new Graph<number>();

      const node2: GraphNode<number> = new GraphNode(2);
      const node3: GraphNode<number> = new GraphNode(3);
      const node5: GraphNode<number> = new GraphNode(5);
      const node7: GraphNode<number> = new GraphNode(7);
      const node8: GraphNode<number> = new GraphNode(8);
      const node9: GraphNode<number> = new GraphNode(9);
      const node10: GraphNode<number> = new GraphNode(10);
      const node11: GraphNode<number> = new GraphNode(11);

      graph.setAdjacencyList(node2, [])
      graph.setAdjacencyList(node3, [node8, node10])
      graph.setAdjacencyList(node5, [node11])
      graph.setAdjacencyList(node7, [node8, node11])
      graph.setAdjacencyList(node8, [node9])
      graph.setAdjacencyList(node9, [])
      graph.setAdjacencyList(node10, [])
      graph.setAdjacencyList(node11, [node2, node9, node10])

      const topologicalSort = new TopologicalSort<number>(graph);
      topologicalSort.execKahnBFS()

      expect(topologicalSort.resultT).deep.equal( [3, 5, 7, 8, 11, 2, 9, 10])
    })
  })

  describe('DFS', () => {
    it('should return correct order', () => {
      const graph: Graph<number> = new Graph<number>();

      const node2: GraphNode<number> = new GraphNode(2);
      const node3: GraphNode<number> = new GraphNode(3);
      const node5: GraphNode<number> = new GraphNode(5);
      const node7: GraphNode<number> = new GraphNode(7);
      const node8: GraphNode<number> = new GraphNode(8);
      const node9: GraphNode<number> = new GraphNode(9);
      const node10: GraphNode<number> = new GraphNode(10);
      const node11: GraphNode<number> = new GraphNode(11);

      graph.setAdjacencyList(node2, [])
      graph.setAdjacencyList(node3, [node8, node10])
      graph.setAdjacencyList(node5, [node11])
      graph.setAdjacencyList(node7, [node8, node11])
      graph.setAdjacencyList(node8, [node9])
      graph.setAdjacencyList(node9, [])
      graph.setAdjacencyList(node10, [])
      graph.setAdjacencyList(node11, [node2, node9, node10])

      const topologicalSort = new TopologicalSort<number>(graph);
      topologicalSort.execDFS()

      expect(topologicalSort.resultT).deep.equal( [7, 5, 11, 3, 10, 8, 9, 2])
    })
  })

  describe('DFS with cycle', () => {
    it('should find cycle and returns emtpy array', () => {
      const graph: Graph<number> = new Graph<number>();

      const node2: GraphNode<number> = new GraphNode(2);
      const node3: GraphNode<number> = new GraphNode(3);
      const node5: GraphNode<number> = new GraphNode(5);
      const node7: GraphNode<number> = new GraphNode(7);
      const node8: GraphNode<number> = new GraphNode(8);
      const node9: GraphNode<number> = new GraphNode(9);
      const node10: GraphNode<number> = new GraphNode(10);
      const node11: GraphNode<number> = new GraphNode(11);

      graph.setAdjacencyList(node2, [node11])
      graph.setAdjacencyList(node3, [node8, node10])
      graph.setAdjacencyList(node5, [node11])
      graph.setAdjacencyList(node7, [node8, node11])
      graph.setAdjacencyList(node8, [node9])
      graph.setAdjacencyList(node9, [])
      graph.setAdjacencyList(node10, [])
      graph.setAdjacencyList(node11, [node2, node9, node10])

      const topologicalSort = new TopologicalSort<number>(graph);
      topologicalSort.execDFS()

      expect(topologicalSort.resultT).deep.equal( [])
    })
  })
})
