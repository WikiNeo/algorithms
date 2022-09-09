import {ListNode} from "../ListNode";

class ReorderList {
  head: ListNode

  constructor(head: ListNode) {
    this.head = head
  }

  exec(): void {
    let slow: ListNode | null = this.head, fast: ListNode | null = this.head;

    // move slow to the mid
    while(fast && fast.next){
      // @ts-ignore
      slow = slow.next
      fast = fast.next.next
    }
    if(fast !== null) { // @ts-ignore
      slow = slow.next;
    }

    // reverse second half
    let left: ListNode | null = null, right: ListNode | null = slow;
    while(right){
      const temp: ListNode | null = right.next;
      right.next = left;
      left = right
      right = temp;
    }

    // merge two lists
    let first: ListNode | null = this.head, second = left;
    while(second){
      // @ts-ignore
      const temp1: ListNode | null = first.next;
      // @ts-ignore
      first.next = second;
      first = temp1;

      const temp2: ListNode | null = second.next;
      second.next = first;
      second = temp2;
    }
    // @ts-ignore
    first.next = null
  }

}

export default ReorderList
