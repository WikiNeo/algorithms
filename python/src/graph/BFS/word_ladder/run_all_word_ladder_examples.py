#!/usr/bin/env python3
"""
Word Ladder Demo Runner
Run all Word Ladder examples in sequence for easy comparison and learning
"""

import os
import time
from pathlib import Path


def run_example(filename, description):
    """Run a single example with nice formatting"""
    print("=" * 80)
    print(f"🎯 {description}")
    print("=" * 80)
    print(f"Running: {filename}")
    print("-" * 40)

    # Add small delay for readability
    time.sleep(1)

    try:
        exit_code = os.system(f"python {filename}")
        if exit_code == 0:
            print(f"✅ {filename} completed successfully")
        else:
            print(f"❌ {filename} failed with exit code {exit_code}")
    except Exception as e:
        print(f"❌ Error running {filename}: {e}")

    print()
    input("Press Enter to continue to next example...")
    print()


def main():
    """Run all Word Ladder examples in logical order"""

    # Change to the BFS directory
    script_dir = Path(__file__).parent
    os.chdir(script_dir)

    print("🚀 WORD LADDER ALGORITHM DEMONSTRATION")
    print("This will run all examples in sequence for complete understanding")
    print()

    examples = [
        (
            "word_ladder_bidirectional.py",
            "Basic Bidirectional BFS - Shows core algorithm with path reconstruction",
        ),
        (
            "word_ladder_comparison.py",
            "Performance Comparison - Regular BFS vs Bidirectional BFS metrics",
        ),
        (
            "word_ladder_visualization.py",
            "Step-by-Step Visualization - See exactly how each algorithm explores",
        ),
        (
            "word_ladder_optimized.py",
            "Production Implementation - Optimized version with detailed explanations",
        ),
    ]

    print(f"📚 Will run {len(examples)} examples:")
    for i, (filename, desc) in enumerate(examples, 1):
        print(f"   {i}. {desc}")
    print()

    response = input("Continue? (y/n): ").lower().strip()
    if response not in ["y", "yes"]:
        print("Cancelled.")
        return

    print()

    for filename, description in examples:
        if os.path.exists(filename):
            run_example(filename, description)
        else:
            print(f"⚠️ File not found: {filename}")

    print("🎉 All Word Ladder examples completed!")
    print("\n📖 For detailed explanations, see: Word_Ladder_Bidirectional_BFS_Guide.md")


if __name__ == "__main__":
    main()
