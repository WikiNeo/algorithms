/**
 * I TrieNode has two fields:
 *  1. a map that maps character to next TrieNode
 *  2. a boolean that marks if current TrieNode is the end of a word or not
 */
class TrieNode {
  children: Map<string, TrieNode>
  isEnd: boolean

  constructor() {
    this.children = new Map<string, TrieNode>()
    this.isEnd = false;
  }
}

export default TrieNode;
