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
class ListNodeS {
  val: number
  next: ListNodeS | null

  constructor(val?: number, next?: ListNodeS) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null: next)
  }
}

export default ListNodeT;

export {ListNodeS}
