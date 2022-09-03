package invert_binary_tree

import "algorithms/go/tree"

func invertTree(root *tree.TreeNode) *tree.TreeNode {
	// base case
	if root == nil {
		return nil
	}

	// swap left & right node
	root.Left, root.Right = root.Right, root.Left

	// invert left & right node
	invertTree(root.Left)
	invertTree(root.Right)

	return root
}
