package sub

import "algorithms/go/tree"

func isSameTree(p *tree.Node, q *tree.Node) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	return isSameTree(p.Left, q.Left) && isSameTree(p.Right, q.Right)
}

func isSubtree(root *tree.Node, subRoot *tree.Node) bool {
	if root == nil && subRoot == nil {
		return true
	}

	if subRoot == nil {
		return true
	}

	if root == nil || subRoot == nil {
		return false
	}

	return (root.Val == subRoot.Val && isSameTree(root, subRoot)) || isSubtree(root.Left, subRoot) || isSubtree(root.Right, subRoot)
}
