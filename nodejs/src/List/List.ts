import ListNodeT from "./ListNode";

class List<T> {
  head: ListNodeT<T> | null

  constructor() {
    this.head = null;
  }
}

export default List;
