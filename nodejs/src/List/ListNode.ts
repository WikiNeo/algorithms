/**
 * ListNode with template support
 */
class ListNodeT<T> {
  value: T
  next: ListNodeT<T>

  constructor(value: T, next: ListNodeT<T>) {
    this.value = value
    this.next = next;
  }
}

/**
 * Simple ListNode
 */
class ListNodeS {
  value: number
  next: ListNodeS

  constructor(value: number, next: ListNodeS) {
    this.value = value
    this.next = next;
  }
}

export default ListNodeT;

export {ListNodeS}
