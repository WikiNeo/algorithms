import TreeT, {Tree} from "./Tree";

class BaseTreeAlgorithm {
  tree: Tree

  constructor(tree: Tree) {
    this.tree = tree;
  }
}

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


export default BaseTreeAlgorithmT;

export {BaseTreeAlgorithm}
