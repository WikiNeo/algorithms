# BFS (Breadth-First Search) Algorithms

This directory contains implementations of various BFS algorithms and optimizations.

## 📚 Contents

### Word Ladder Problem Suite
- **[Word_Ladder_Bidirectional_BFS_Guide.md](Word_Ladder_Bidirectional_BFS_Guide.md)** - Comprehensive guide to the Word Ladder problem and bidirectional BFS optimization
- **[word_ladder_bidirectional.py](word_ladder_bidirectional.py)** - Core bidirectional BFS implementation with path reconstruction
- **[word_ladder_comparison.py](word_ladder_comparison.py)** - Performance comparison between regular and bidirectional BFS
- **[word_ladder_visualization.py](word_ladder_visualization.py)** - Step-by-step exploration visualization
- **[word_ladder_optimized.py](word_ladder_optimized.py)** - Production-ready optimized implementation

### Other BFS Problems
- **[rotting_oranges.py](rotting_oranges.py)** - Multi-source BFS problem

## 🎯 Quick Start

### Run Word Ladder Examples
```bash
# Basic bidirectional BFS demo
python word_ladder_bidirectional.py

# Performance comparison
python word_ladder_comparison.py

# Step-by-step visualization
python word_ladder_visualization.py

# Optimized version with explanations
python word_ladder_optimized.py
```

### Key Learning Points
- **Bidirectional BFS**: Reduces search space from O(b^d) to O(b^(d/2))
- **Graph Recognition**: Identifying hidden graph problems
- **Optimization Techniques**: Always expand smaller frontier, early termination
- **Real-world Applications**: Social networks, navigation, puzzle solving

## 📖 Study Guide

1. **Start with**: [Word_Ladder_Bidirectional_BFS_Guide.md](Word_Ladder_Bidirectional_BFS_Guide.md) for complete problem walkthrough
2. **Experiment with**: [word_ladder_comparison.py](word_ladder_comparison.py) to see performance differences
3. **Understand internals**: [word_ladder_visualization.py](word_ladder_visualization.py) for step-by-step execution
4. **Production code**: [word_ladder_optimized.py](word_ladder_optimized.py) for interview-ready implementation

## 🔗 External Resources
- [LeetCode 127 - Word Ladder](https://leetcode.com/problems/word-ladder/)
- [LeetCode 126 - Word Ladder II](https://leetcode.com/problems/word-ladder-ii/)
