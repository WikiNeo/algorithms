import {ListNode} from "../ListNode";

class MergeTwoLists {
  list1: ListNode | null
  list2: ListNode | null

  constructor(list1: ListNode, list2: ListNode) {
    this.list1 = list1
    this.list2 = list2;
  }

  exec(): ListNode | null {
    const head: ListNode = new ListNode();
    let cur: ListNode = head;

    while(this.list1 && this.list2){
      if(this.list1.val < this.list2.val){
        cur.next = this.list1
        this.list1 = this.list1.next
      } else {
        cur.next = this.list2
        this.list2 = this.list2.next
      }
      cur = cur.next;
    }

    while(this.list1){
      cur.next = this.list1
      cur = cur.next
      this.list1 = this.list1.next
    }

    while(this.list2){
      cur.next = this.list2
      cur = cur.next
      this.list2 = this.list2.next
    }

    return head.next
  }
}

export default MergeTwoLists;
