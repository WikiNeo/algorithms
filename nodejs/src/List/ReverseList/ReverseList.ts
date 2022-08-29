import {ListNode} from "../ListNode";

class ReverseList {
  head: ListNode

  constructor(head: ListNode) {
    this.head = head;
  }

  exec(): ListNode | null {
    // special check for empty or single node list
    if(this.head === null || this.head.next === null) return this.head;

    // for list problem, we usually have a dummy head
    let left: ListNode | null = null, right: ListNode | null = this.head;

    while(right !== null){
      const temp: ListNode | null = right.next;
      right.next = left;
      left = right;
      right = temp
    }

    return left;
  }
}

export default ReverseList;
