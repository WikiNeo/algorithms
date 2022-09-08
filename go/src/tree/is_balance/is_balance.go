package is_balance

import "algorithms/go/tree"

func isBalanced(root *tree.Node) bool {
	res = true

	depth(root)

	return res
}

var res bool

func depth(node *tree.Node) int {
	if node == nil {
		return 0
	}

	var left int = depth(node.Left)
	var right int = depth(node.Right)
	if abs(left-right) > 1 {
		res = false
	}

	return max(left, right) + 1
}

func max(a int, b int) int {
	if a > b {
		return a
	}

	return b
}

func abs(num int) int {
	if num > 0 {
		return num
	}
	return -num
}
