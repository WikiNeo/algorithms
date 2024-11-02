# Island Count

## Problem

Write a function, islandCount, that takes in a grid containing Ws and Ls. W represents water and L represents land. The function should return the number of islands on the grid. An island is a vertically or horizontally connected region of land.

## Thoughts

1. The grid is 2D array, so we can +1 -1 for row & col to move
   - bound check
1. DFS with true/false for island
1. visited Set for undirected graph
1. main driver to count number of islands
