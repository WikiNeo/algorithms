import {ListNodeS} from "../ListNode";

class ReorderList {
  head: ListNodeS

  constructor(head: ListNodeS) {
    this.head = head
  }

  exec(): void {
    let slow: ListNodeS | null = this.head, fast: ListNodeS | null = this.head;

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
    let left: ListNodeS | null = null, right: ListNodeS | null = slow;
    while(right){
      const temp: ListNodeS | null = right.next;
      right.next = left;
      left = right
      right = temp;
    }

    // merge two lists
    let first: ListNodeS | null = this.head, second = left;
    while(second){
      // @ts-ignore
      const temp1: ListNodeS | null = first.next;
      // @ts-ignore
      first.next = second;
      first = temp1;

      const temp2: ListNodeS | null = second.next;
      second.next = first;
      second = temp2;
    }
    // @ts-ignore
    first.next = null
  }

}

export default ReorderList
