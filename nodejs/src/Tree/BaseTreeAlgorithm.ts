import TreeT, {Tree} from "./Tree";

class BaseTreeAlgorithmT<T> {
  tree: TreeT<T>

  result: T[][]

  constructor(tree: TreeT<T>) {
    this.tree = tree
    this.result = []
  }

  flatResult(): T[]{
    return this.result.flat()
  }
}

class BaseTreeAlgorithm {
  tree: Tree

  constructor(tree: Tree) {
    this.tree = tree;
  }
}

export default BaseTreeAlgorithmT;

export {BaseTreeAlgorithm}
