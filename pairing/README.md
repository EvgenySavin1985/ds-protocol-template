# Uniform Random Groups Generator

- [Uniform Random Groups Generator](#uniform-random-groups-generator)
  - [Purpose](#purpose)
  - [Work Flow](#work-flow)
  - [Pros and Cons](#pros-and-cons)
---
## Purpose
To create pairs every time uniformly. So each person pairs with every other in a group and we avoid repetition.

NOTE: Currently on works for 2 persons groups. Can expand for more later.

---
## Work Flow
1. A random seed is fixed at starting (We can also fix it as any number for all the bootcamps)
2. We start with creating combinations of pair of students
   - A folder named `groups` is created
   - Two files are created (.pkl files)
     - One, where we put the combinations of pairs.
     - Second, we create a dictionary for all the combination of pairs and initialize their values with 0.
3. To create pairs for current day
   1. Loop through each pair from the combinations list
   2. Check if a person has already been in a group before
   3. If both are not in a group then also check if this paired has already formed before using the dictionary count
   4. At the end check if we have all persons in some group
      - If not, then make groups from remaining persons
4. Then we loop through all the pairs 
   - Remove pairs from the combinations list
   - Increment the dictionary values for formed pairs
   - NOTE: Combinations can only be either (a,b) or (b,a) for a pair
   - If we don't find (a,b) 
     - Then we remove (b,a) and check for increment as well in the same way
   - If both (a,b) and (b,a) doesn't exist in pairing list, we still form a group and increment the dictionary.
  5. At last, we save both the updated files.

---
## Pros and Cons
 * Pros
   - Probability of forming an already formed group will be low.
   - For example, if we have 14 students in a bootcamp, then we can form 91 different combinations and for atleast 9-10 times we will not see an already formed group (Hopefully).
* Cons
  - Can only work for pair programming exercises (for now)
  - Files have to be saved and oad everytime.
    - So every time one has to pull and push to github
    - Pro -> Can be a good way to practice git.
---