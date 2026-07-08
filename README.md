1. Tower of Hanoi
Problem

The Tower of Hanoi is a classic recursion problem.

You have:

Three rods:
Source (A)
Auxiliary (B)
Destination (C)

Rules:

Only one disk can be moved at a time.
A larger disk cannot be placed on a smaller disk.
Move all disks from Source to Destination.
Recursive Algorithm

If there is only one disk:

Move it directly.

Otherwise:

Move n−1 disks from Source to Auxiliary.
Move the largest disk to Destination.
Move n−1 disks from Auxiliary to Destination.
