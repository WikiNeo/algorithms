package max_depth

import (
	"algorithms/go/tree"
)

/*
*
The max depth of a node is the max depth of left & right + 1
*/
func maxDepth(root *tree.Node) int {
	if root == nil {
		return 0
	}
	return max(maxDepth(root.Left), maxDepth(root.Right)) + 1
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}
