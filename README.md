# SltnsCrkdCpp
Implementations of problems in Cracking the Coding Interview in C++

Changing to Python because I'm sick and fucking tired of navigating through countless stackoverflow pages to get basic stuff like stacks, concatenating numbers to strings, passing 2d arrays as a reference etc. done. Too many constraints that hinder me from thinking about the actual fucking problem. Wasting SHIT LOAD of time. Anyway Python is here so YAY! 

Rant Over.

Here are some tricks I learned while solving problems, as well as ones in the book. Listing them chapter wise

## Tricks I learned

## Rule of thumb
Always try to get a solution with O(N) time complexity within O(1) space

### Chapter 1 - Strings and Arrays

1. Checking if the string has duplicates? An array of size 128 (size of ASCII, if unicode it is 1,111,998 although it is usually ASCII) helps as a counter for each character. If anything is more than 1, your string has duplicates

2. An array of size 128 (be sure to ask if it is ASCII) can also be used to determine if two strings have the same characters

3. An 8-bit number can be used to check if a permutation of a string is a palindrome

4. Two indexes can be used to check if two strings have exactly one difference (missing char, different character etc.)

5. To rotate a matrix by 90 degrees, do it by swapping elements iteratively in a circular way. Do this swapping layer by layer.

6. To check if a string1 is a rotation of another string2, check if string1 is a substring of string2string2

### Chapter 2 - Linked Lists

1. To remove duplicates from linked lists without a buffer, use two pointers to check if a number occurs elsewhere in the list. O(1) space but O(n^2) complexity

2. To get kth element from last, use two pointers - one iterates through the list, from head to end, until counter increases from 1 to k and the second one iterates as the first one goes from k to end.

3. To delete middle node just copy the contents of next node and delete the next node

4. To add two numbers in represented by two lists, think about how you add two multiple-digit numbers in real life and replicate it (Pass on extra number to the next digit - carry). Same goes for subtraction (Take an extra one in case digit subtraction is not possible). Just pad the shorter number with zeros

5. To check if a linked list is a palindrome - a stack can be used to store first half to check the remaining half is equal to the stack

6. To check if a linked list is a cycle, see if a node has been visited more than once. To know at which node the loop starts we can use two pointers. The pointers, one moving twice the speed of the other, to see if there is a collision of nodes. When there is a collision move the slower pointer to the head and move both the pointers at the same pace. They should meet at the beginning of the loop


