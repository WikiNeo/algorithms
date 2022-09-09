import TrieNode from "../TrieNode";

class AddAndSearchWord {
  root: TrieNode;

  constructor() {
    this.root = new TrieNode()
  }

  /**
   * Add word character by character to Trie & mark the end
   *
   * @param word
   */
  addWord(word: string): void {
    let cur: TrieNode = this.root;

    for(const c of word){
      if(!cur.children.has(c)) cur.children.set(c, new TrieNode())
      // @ts-ignore
      cur = cur.children.get(c)
    }
    cur.isEnd = true;
  }

  search(word: string): boolean {
    let res: boolean = false;
    const LEN: number = word.length
    let cur: TrieNode = this.root

    const exec = (i: number, node: TrieNode) => {
      if(res === true) return;
      if(i === LEN){
        if(node.isEnd === true) res = true
        return;
      }

      if(word[i] === '.') {
        for(const c of node.children.keys()){
          // @ts-ignore
          exec(i + 1, node.children.get(c))
        }
      } else if(node.children.has(word[i])){
        // @ts-ignore
        exec(i + 1, node.children.get(word[i]))
      }
    }

    exec(0, cur)

    return res;
  }
}

export default AddAndSearchWord;
