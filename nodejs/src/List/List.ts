import ListNodeT, {ListNodeS} from "./ListNode";

class ListT<T> {
  head: ListNodeT<T> | null

  constructor() {
    this.head = null;
  }
}

class ListS {
  head: ListNodeS | null

  constructor() {
    this.head = null;
  }
}

export default ListT;

export {ListS}
