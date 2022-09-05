package diameter

import "algorithms/go/tree"

var res int

func depth(node *tree.Node) int {
	if node == nil {
		return 0
	}

	// get left and right edge count
	var left int = depth(node.Left)
	var right int = depth(node.Right)
	// update res
	res = max(left+right, res)

	// recursive formula for depth
	return max(left, right) + 1
}

func diameterOfBinaryTree(root *tree.Node) int {
	// note the update here
	res = 0

	depth(root)

	return res
}

func max(a int, b int) int {
	if a > b {
		return a
	}

	return b
}
