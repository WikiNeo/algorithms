import {ListNode} from "../ListNode";

class CopyWithRandomPointer {
  head: ListNode

  constructor(head: ListNode) {
    this.head = head;
  }

  exec(): ListNode | null {
    const oldToCopy: Map<ListNode | null, ListNode | null> = new Map<ListNode | null, ListNode | null>();
    oldToCopy.set(null, null);

    // old node to new node copy
    let cur: ListNode | null = this.head;
    while(cur){
      let copy = new ListNode(cur.val)
      oldToCopy.set(cur, copy)
      cur = cur.next
    }

    // move cur from head to end
    cur = this.head;
    while(cur) {
      let copy = oldToCopy.get(cur)
      // @ts-ignore
      copy.next = oldToCopy.get(cur.next);
      // @ts-ignore
      copy.random = oldToCopy.get(cur.random);
      cur = cur.next
    }

    // @ts-ignore
    return oldToCopy.get(this.head)
  }

}

export default CopyWithRandomPointer;
