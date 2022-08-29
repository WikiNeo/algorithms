import {ListNodeS} from "../ListNode";

class MergeTwoLists {
  list1: ListNodeS | null
  list2: ListNodeS | null

  constructor(list1: ListNodeS, list2: ListNodeS) {
    this.list1 = list1
    this.list2 = list2;
  }

  exec(): ListNodeS | null {
    const head: ListNodeS = new ListNodeS();
    let cur: ListNodeS = head;

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
