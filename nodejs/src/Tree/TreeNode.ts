/**
 * TreeNode with template support
 */
class TreeNodeT<T> {
  val: T | undefined;
  left: TreeNodeT<T> | null;
  right: TreeNodeT<T> | null;

  leftAddedNull: boolean

  constructor(value?: T, left?: TreeNodeT<T> | null, right?: TreeNodeT<T> | null) {
    this.val = value;
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
    this.leftAddedNull = false;
  }

  setLeftAddedNull() {
    this.leftAddedNull = true;
  }
}

/**
 * Simple TreeNode
 */
class TreeNodeS {
  val: number
  left: TreeNodeS | null
  right: TreeNodeS | null

  constructor(val?: number, left?: TreeNodeS | null, right?: TreeNodeS | null) {
    this.val = (val===undefined ? 0 : val)
    this.left = (left===undefined ? null : left)
    this.right = (right===undefined ? null : right)
  }
}

export default TreeNodeT;

export {
  TreeNodeS
}

