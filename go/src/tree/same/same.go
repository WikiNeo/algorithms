package same

import "algorithms/go/tree"

func isSameTree(p *tree.Node, q *tree.Node) bool {
	// if both trees are traversed, we are done
	if p == nil && q == nil {
		return true
	}
	// if either is null or the value is not the same, return false
	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	// recursively check left & right
	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}
