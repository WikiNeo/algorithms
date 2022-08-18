import TreeT, {TreeS} from "./Tree";

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

class BaseTreeAlgorithmS {
  tree: TreeS

  constructor(tree: TreeS) {
    this.tree = tree;
  }
}

export default BaseTreeAlgorithmT;

export {BaseTreeAlgorithmS}
