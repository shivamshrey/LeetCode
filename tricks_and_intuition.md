## Tricks and Intuition behind some problems
* 205. __Isomorphic Strings__ (Easy): Mark characters at the same index in both the strings point with the same number (`i` in this case). But before doing that, check if they are differently marked. If yes, then that means that this character is mapped to some other character already. So return `False`.
* 448. __Find All Numbers Disappeared in an Array__ (Easy): For each number `nums[i]` in `nums`, we mark the number that `nums[i]` points to as negative. Then we filter the list, get all the indexes which points to a positive number.
* 605. __Can Place Flower__ (Easy): Use Greedy approach. Start from start of array. Check if current place is viable (for ends of array consider a 0 padding). If yes, then place a flower there and increment `count` by `1`. If `i = len(arr) - 1` or `count >= n`, then exit loop. Outsided the loop, if `count == n`, then return `True`.
* 665. __Non-decreasing Array__ (Medium): If `nums[i - 1] > nums[i]` then there are 2 possibilities: 
        * `nums[i - 2] > nums[i]`, then we have two choices:
            1. demote previous 2 elements
            2. promote current element
            
            So we promote the current element as it is only one modification. 
        * `nums[i - 2] <= nums[i]`, then we demote `nums[i - 1]`. 
    
        Return `True` if `count <= 1`.
* 703. __Kth Largest Element in a Stream__ (Easy): Add all elements to min heap. Pop `k` elements. This leaves you with `k` largest elements in the heap, with `heap[0]` being the kth largest. Now, before adding a new `val`, if `len(heap)` < `k`, then push `val` to heap else if `val` > `heap[0]`, then pop from heap and push `val` (i.e. `heapreplace()`). In both cases, the new `heap[0]` will be the kth largest element.
* 705. __Design HashSet__ (Easy): Use hashing function https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing. Use separate chaining to handle collisions. Trick for faster modulo: `s % t = s & ((1 << t) - 1)`.
* 752. __Open The Lock__ (Medium): BFS will be most likely used whenever you have to reach from a source to a destination. Create `visited` set out of deadends to have constant look up time. Append source `"0000"` to `queue` (use deque for speed). Set `depth` to `-1`. Do the following till `queue` is not empty.
        - Increment depth by 1.
        - Calculate length of current `queue`
        - Run a loop for `queue` length times, pop one node from `queue`.
        - If it is equal to `target`, return `depth`.
        - If it is present in visited, then skip and `continue`.
        - Otherwise, add this `node` to `visited`.
        - And extend the `queue` by all the successors of this node.

        When the `queue` becomes empty, return -1.

        In the `successors()` function, find all successors by incrementing and decrementing one value (wheel) at a time and adding them to `result`. Trick used when decrementing one value so that it doesn't overflow: `-1 % 10 = 9`. Return this `result`.
