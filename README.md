# SltnsCrkdCpp
Implementations of problems in Cracking the Coding Interview in C++

Changing to Python because I'm sick and fucking tired of navigating through countless stackoverflow pages to get basic stuff like stacks, concatenating numbers to strings, passing 2d arrays as a reference etc. done. Too many constraints that hinder me from thinking about the actual fucking problem. Wasting SHIT LOAD of time. Anyway Python is here so YAY! 

Rant Over.

Here are some tricks I learned while solving problems, as well as ones in the book. Listing them chapter wise

## Codefights

I am simultaneously solving problems from Codefights interview track so I can apply the concepts I have learned. The challenges are in the folder CdFtsIntQ

## Tricks I learned

These are some tips and tricks I have picked up from CTCI book and by reading solutions elsewhere.

### Rule of thumb
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

7. It helps to think about the list in a linear way. Counting the nodes from start and end will help you solve some problems.

8. Using two pointers can be very useful

9. Recurse to reverse a linked list

### Chapter 3 - Stacks

1. Stacks are useful to reverse lists - Two Stacks help form a queue

2. Two stacks can be used to sort a list of numbers

3. Arrays can be used to build stacks

4. To get the minimum of elements is a stack, maintain a variable that constantly checks for min values as soon as a value is pushed


### Chapter 4 - Trees and Graphs

1. BFS is level wise traversal and DFS is branch wise traversal.

2. Recursive Traversal of tree is very useful for checking if conditions hold all over the tree

3. Inorder DFS traversal of Binary Search Tree is a sorted array of elements

4. Shortest Path - Djikstra's

5. Minimum Spanning Tree - Prim / Kruskal

6. Inorder traversal without recursion or stack - Morris tree traversal. Works by adding the next node of traversal to the leaf node.

### Chapter 5 - Bit Manipulation

1. Bitwise left shift = multiplication by 2^n

2. Bitwise right shift = division by 2^n

3. Test kth bit - n & (1 << k)

4. Toggle kth bit - n = n ^ (1 << k)

5. Get lowest set bit - n & -n

6. Get lowest unset bit - ~n & (n+1)

7. Swap values x & y 1. x = x ^ y 2. y = x ^ y 3. x = x ^ y


### Chapter 6 - Math and Logic

1. Prime numbers - Sieve of Eratosthenes

2. 

### Regular Expressions

Rule - Write regexes as specific as possible

1. \d - match any digit 0-9
2. abc... - letters
3. def... - numbers
4. \D - any non-digit character
5. . - any character
6. \. - period
7. [abc] - only a,b or c
8. [^abc] - not a,b nor c
9. [0-9] - all digits between 0 and 9 (incl)
10. [a-g] - all chars between a and g (incl)
11. \w - any alphanumeric character
12. \W - any non-alphanumeric character
13. {m} - m repetitions of a character
14. {m,n} - m to n repetitions
15. \s - any whitespace char
16. \S - any non-whitespace char
17. (abc) - groups
18. (a(bc)) - sub groups

# System Design Questions

## System Design - The Process

1. Listen and gather requirements carefully.
    * important to identify classes and actions
    * also to identify relationships between them
2. Ask questions to clarify users and constraints. 
    * Who is going to use it?
    * How are they going to use it?
    * How many users are there?
    * What does the system do?
    * What are the inputs and outputs of the system?
    * How much data do we expect to handle?
    * How many requests per second do we expect?
    * What is the expected read to write ratio?
3. Create high level design
    * draw the components and relationships
    * try to validate them using tests
4. Add more details to components
    * data structures to be used
    * algorithms to use and their complexity
    * database schema
5. Scale the design
    * identify bottlenecks and address them
    * horizontal vs vertical scaling to solve problems
    * database sharding?
    * load balancer in the case of horizontal scaling
    * Caching?

## System Design - Scalability

### Part 1 - Clones

1. A scalable web service has many different application servers that serve thousands or even millions of requests at a time.

2. Every server contains exactly the same codebase and does not store any user-related info or sessions on it's HD

3. An external database or cache contains the session data and the servers need to query for data

4. A code change can be deployed across multiple servers by tools like Capistrano 

### Part 2 - Database

1. If we implement the above architecture and use an RDBMS database like MySQL. The web service keeps getting slower.

2. Denormalization will improve the performance of SQL queries but all the joins need to happen in application code.

3. A very good alternative is a NoSQL database - MongoDB, Cassandra etc.

4. Even then, the application gets slower eventually. For this we need cache.

### Part 3 - Cache

1. Cache means in-memory caches like Redis or Memcached. Not file based cache.

2. A cache is a simple key value storage. Buffers between application layer and data storage. 

3. Application should first try to read the data from cache. If it's not there then read from data storage and make a copy on cache (for future reqs).

4. An issue with above cache implementation is expiration. When one piece of data changes you need to delete all cached queries related to that data piece.

5. Alternative approach is to consider data as objects. Store data itself as objects inside cache and when something changes the objects can be discarded instead of queries. Examples of objects to store in cache: user sessions, fully rendered blog articles, user - friend relationships etc.

### Part 4 - Asynchronism

1. Async means that the resources will not stop all operations until a specific job is done. Instead they are constantly checking if that job is done and will report when it is done.

2. Some websites process all dynamic content in advance and store them as static content (HTML). This will allow users to access the features without much delay.

3. Another way of doing things is to maintain a job queue and ask resources to check for the specific job's completion status.


# SQL

## Joins

1. Inner Join - Common records of A and B
2. Left Join - All records of A and common records of A and B
3. Right Join - All records of B and common records of A and B
4. Full Join - All records of A and B (A+B)
5. Cross Join - All records of A and B (A * B -  Cartesian product)

# Questions to ask the interviewer

1. What is the breakdown of a developer's day, e.g. how much time for support or troubleshooting, how much time for coding, analysing requirements, etc.?

2. Do you allow time for peer reviews of code?

3. How is a code review done at your company?

4. Do you have a standard template for estimating development effort for new work to make sure nothing is overlooked?

5. Does your company allow its employees to work from home?

6. What gear will be provided for me to work on? Will that have administrative priviliges?


