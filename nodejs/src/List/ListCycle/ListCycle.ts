import {ListNode} from "../ListNode";

class ListCycle {
  head: ListNode;

  constructor(head: ListNode) {
    this.head = head;
  }

  exec(): boolean {
    let slow: ListNode | null = this.head, fast: ListNode | null = this.head

    while(fast && fast.next){
      // @ts-ignore
      slow = slow.next
      fast = fast.next.next
      if(slow === fast) return true
    }

    return false;
  }
}

export default ListCycle;
