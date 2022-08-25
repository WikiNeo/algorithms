import {ListNodeS} from "../ListNode";

class ListCycle {
  head: ListNodeS;

  constructor(head: ListNodeS) {
    this.head = head;
  }

  exec(): boolean {
    let slow: ListNodeS | null = this.head, fast: ListNodeS | null = this.head

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
