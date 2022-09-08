import ListNodeT, {ListNode} from "./ListNode";

class ListT<T> {
  head: ListNodeT<T> | null

  constructor() {
    this.head = null;
  }
}

class ListS {
  head: ListNode | null

  constructor() {
    this.head = null;
  }
}

export default ListT;

export {ListS}
