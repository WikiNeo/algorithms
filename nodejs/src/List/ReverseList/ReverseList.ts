import {ListNodeS} from "../ListNode";

class ReverseList {
  head: ListNodeS

  constructor(head: ListNodeS) {
    this.head = head;
  }

  exec(): ListNodeS | null {
    // special check for empty or single node list
    if(this.head === null || this.head.next === null) return this.head;

    // for list problem, we usually have a dummy head
    let left: ListNodeS | null = null, right: ListNodeS | null = this.head;

    while(right !== null){
      const temp: ListNodeS | null = right.next;
      right.next = left;
      left = right;
      right = temp
    }

    return left;
  }
}

export default ReverseList;
