import {ListNodeS} from "../ListNode";

class ListCycle {
  head: ListNodeS;

  constructor(head: ListNodeS) {
    this.head = head;
  }

  exec(): boolean {
    let slow: ListNodeS = this.head, fast: ListNodeS = this.head

    while(fast && fast.next){
      slow = slow.next
      fast = fast.next.next
      if(slow === fast) return true
    }

    return false;
  }
}

export default ListCycle;
