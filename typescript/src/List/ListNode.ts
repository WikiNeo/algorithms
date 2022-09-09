/**
 * ListNode with template support
 */
class ListNodeT<T> {
  value: T
  next: ListNodeT<T> | null

  constructor(value: T, next: ListNodeT<T>) {
    this.value = value
    this.next = next;
  }
}

/**
 * Simple ListNode
 */
class ListNode {
  val: number
  next: ListNode | null
  random: ListNode | null

  constructor(val?: number, next?: ListNode, random?: ListNode) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null: next)
    this.random = (random === undefined ? null: random)
  }
}

export default ListNodeT;

export {ListNode}
