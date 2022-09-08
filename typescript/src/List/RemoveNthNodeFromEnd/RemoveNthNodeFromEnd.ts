import {ListNode} from "../ListNode";

class RemoveNthNodeFromEnd {
  head: ListNode | null
  n: number

  constructor(head: ListNode | null, n: number) {
    this.head = head
    this.n = n
  }

  exec(): ListNode | null {
    // dummy head that points to next
    const dummy: ListNode = new ListNode()
    dummy.next = this.head;

    // make left and right distance to be n + 1
    let left: ListNode | null = dummy, right: ListNode | null = dummy;
    while(this.n >= 0){
      // @ts-ignore
      right = right.next
      this.n--;
    }

    // move right until right is null, then left is before nth node to the end
    while(right){
      // @ts-ignore
      left = left.next;
      right = right.next;
    }

    // remove left next node
    // @ts-ignore
    left.next = left.next.next

    // return result
    return dummy.next;
  }
}

export default RemoveNthNodeFromEnd;
