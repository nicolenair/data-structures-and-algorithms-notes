**Source Text**: McDowell, G. L. (2015). Chapter 8: Recursion & Dynamic programming in Cracking the Coding Interview in 189 Programming Questions and Solutions. CareerCup.

* **recursive solutions** = built off of solutions to subproblems
  * example: to get f(n) we modify f(n-1)
  * example: solve the problem for one half of the dataset and then for the other & merge results
* **approaches**:
  * bottom-up
    * build the solution for one case off of a previous case
  * top-down
    * divide the problem for case N into subproblems
  * half-and-half approaches
    * examples: merge sort, binary search
* **recursive vs iterative solutions**
  * recursion can be space inefficient --> each recursive call adds a new layer to the stack


## Dynamic Programming & Memoization
  * mostly a matter of taking recursive problem and finding the *overlapping subproblems* & *caching* them for future recursive calls OR changing to iteration
  * famous & cool example: computing the nth Fibonacci number
  
![alt text](https://github.com/nicolenair/data-structures-and-algorithms-notes/blob/master/assets/Screen%20Shot%202020-06-19%20at%2022.13.06.png)

  * we can see that the runtime will be O(2^N). to fix this, we use DP. 
  * top down dynamic programming/memoization
    * find identical nodes
    * to compute fib(N), we should not have to make more than O(N) calls because there are only O(N) possible values to throw at fib
    * so CACHE
    * if you're stuck computing a runtime of a recursive algorithm, then you should try *expanding the shallower nodes before the deeper nodes* --> helps intuition
  * bottom-up dynamic programming
    * basically the same as top down, but we compute the lower n cases FIRST (opposite order)
 
    
  
