import TrieNode from "./TrieNode"

class Trie {
  // use root to access Trie
  root: TrieNode

  /**
   * Initially the Trie is a TrieNode
   */
  constructor() {
    this.root = new TrieNode()
  }

  /**
   * Insert each character into the Trie, creating new TrieNode if needed.
   *
   * @param word
   */
  insert(word: string): void {
    let cur: TrieNode = this.root;

    for(let c of word) {
      if(!cur.children.has(c)) cur.children.set(c, new TrieNode())
      // @ts-ignore
      cur = cur.children.get(c)
    }

    // mark end
    cur.isEnd = true;
  }

  search(word: string): boolean {
    let cur: TrieNode = this.root;

    for(let c of word) {
      // if ever we can't find the next TrieNode, return false
      if(!cur.children.has(c)) return false
      // @ts-ignore
      cur = cur.children.get(c)
    }

    // check if the TrieNode is the end
    return cur.isEnd;
  }

  /**
   * The startsWith is similar with search except that it doesn't need check the TrieNode end
   *
   * @param word
   */
  startsWith(word: string): boolean {
    let cur: TrieNode = this.root;

    for(let c of word) {
      if(!cur.children.has(c)) return false
      // @ts-ignore
      cur = cur.children.get(c)
    }

    return true
  }
}

export default Trie
