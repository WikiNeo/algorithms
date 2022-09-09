package lca_bst

import "algorithms/go/tree"

func lowestCommonAncestor(root, p, q *tree.Node) *tree.Node {
	if root == nil {
		return nil
	}

	for {
		if root.Val < p.Val && root.Val < q.Val {
			root = root.Right
		} else if root.Val > p.Val && root.Val > q.Val {
			root = root.Left
		} else {
			return root
		}
	}

}
