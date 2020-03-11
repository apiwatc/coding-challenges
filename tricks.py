"""
XOR
1. Any number XOR itself is zero. This is sometimes used in machine code to clear a register.
2. If you XOR by the same number twice, you get the original value back. In other words, (𝑛⊻𝑦)⊻𝑦=𝑛.
   This has been used for cheesy encryption schemes and for some old-school computer graphics effects.

This example swaps integers without a temporary variable using XOR
"""
a = 2
b = 8
a ^= b
b ^= a
a ^= b
