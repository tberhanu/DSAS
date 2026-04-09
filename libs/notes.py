from collections import defaultdict
from collections import deque
from collections import Counter
from collections import OrderedDict
from collections import namedtuple
from email.policy import default
import heapq
from xxlimited import foo

lookup_freq = Counter(arr) # O(N)
lookup_freq.most_common() # returns list of (elem, count) sorted by count desc

# Binary Search: O(logN)
bisect.bisect_left(arr, elt) # returns the leftmost index where x should be inserted to maintain sorted order
bisect.bisect_right(arr, elt) # returns the rightmost index where x should be inserted to maintain sorted order

# both bisect_left and bisect_right result same if the element is not present in the array

# Priority Queue: O(logN) for push and pop
minHeap, maxHeap = [], [] # maxHeap takes negative of the values  
heapq.heappush(minHeap, (priority, tie_breaker,item)) # O(logN) Note: tie_breaker if used TUPLE only  
heapq.heappush(maxHeap, -priority) # O(logN) Note: tie_breaker is NOT NEEDED here since no TUPLE 
priority, item = heapq.heappop(minHeap) # O(logN) 
heapq.heapify(arr) # O(N)

# In-place sorting: O(NlogN), returns None, modifies the original array
arr.sort() # O(NlogN)
arr.sort(key=lambda x: x[1]) # O(NlogN) sort by second element of the tuple
arr.sort(reversed=True) # O(NlogN) sort in descending order
arr.sort(key=lambda x: foo(x)) # O(NlogN) sort by the result of foo(x)  

# Sorting and returning a new sorted list: O(NlogN)
sorted_arr = sorted(arr) # O(NlogN)
sorted_arr = sorted(arr, key=lambda x: x[1]) # O(NlogN) sort by second element of the tuple
sorted_arr = sorted(arr, reversed=True) # O(NlogN) sort in descending order
sorted_arr = sorted(arr, key=lambda x: foo(x)) # O(NlogN) sort by the result of foo(x)


arr = str.split(",") # O(N) splits the string by the delimiter and returns a list of substrings
str.join(arr) # O(N) joins the list of strings into a single string
arr2 = str.split("") # O(N) splits the string into a list of characters
arr3 = str.split() # O(N) splits the string by whitespace and returns a list of substrings
arr4 = str.split(" ", 1) # O(N) splits the string by SPACE and returns a list of 2 substrings
arr5 = str.split(",", k) # O(N) splits the string by COMMA and returns a list of (k + 1) substrings


d1 = defaultdict(int) # O(1) default value is 0
d2 = defaultdict(list) # O(1) default value is []
d3 = defaultdict(set) # O(1) default value is set()
d4 = defaultdict(lambda: 0) # O(1) default value is 0
d5 = defaultdict(lambda: [[]]) # O(1) default value is [[]]
d6 = defaultdict(tuple)


d1 = {}
value = d1.get(key, default) # O(1) returns the value for key if key is in the dictionary, else default


# Set: update vs add
s = set()
s.add(1)
s.add(2)
s.update([2, 3, 4], (5, 6))
print(s)  # {1, 2, 3, 4, 5, 6} (Order may vary)

# List: extend vs append
l = [1, 2]
l.append(3)
l.extend([2, 3])
print(l)  # [1, 2, 3, 2, 3]


str.isupper() # O(N) returns True if all characters in the string are uppercase
str.islower() # O(N) returns True if all characters in the string are lowercase
str.isdigit() # O(N) returns True if all characters in the string are digits (Numbers only)
str.isalpha() # O(N) returns True if all characters in the string are alphabetic (Letters only)
str.isalnum() # O(N) returns True if all characters in the string are alphanumeric (Number or Letter)
str.istitle() # O(N) returns True if the string is a titlecased string (uppercasefirst letter)
