
# Binary Search Tree Project
<a href="https://www.patika.dev " target="_blank">Patika Dev</a>

<a href="https://app.patika.dev/courses/veri-yapilari-ve-algoritmalar/binary-search-tree-proje" target="_blank">Binary Search Tree Project</a>

<a href="https://app.patika.dev/pasha" target="_blank">My Patika Profile</a>



Question 1)<br>
Write the Binary-Search-Tree steps of the array [7, 5, 1, 8, 3, 6, 0, 9, 4, 2].<br>
<p>
  <img src="https://github.com/semihguezel/Data-Structures-and-Algorithms/blob/Main/images/BinarySearchTree.png" width="600" height = "500" title="Insertion Sort">
</p>

- First step; We have select the root number. Root number can be first or last index of the array, so we select 7 as root.
- Then we check index 1 which is 5 , it is smaller than 7 so we have to move 5 to left side of the tree.
- Now we are at index 2 which corrensponds  to 1,  it is both smaller than 7 and 5 so we will place it leftmost node of the tree.
- Our current index reached 3 it gives 8 and it is greater than 7 so we have to move 8 right side of the tree.
- Index is 4 , it corrensponds to 3, it is both smaller than 7 and 5 but greater than 1. In this case we move 3 as a child of 5 to the left side.
- Index is 5 , it corrensponds 6, it is smaller than 7 but greater than 5. In this case we move 6 as a child of 5 to the right side.
- Index is 6 , it corrensponds 0, it is smaller than 7, 5 and 1 so we will move 0 as child of 1 to the left side.
- Index is 7 , it corrensponds 9, it is greater than 7 and 8 so we will move 9 as child of 8 to the right side.
- Index is 8 , it corrensponds 4, it is smaller than 7, 5 but greater than 3 so we will move 4 as child of 3 to the right side.
- Finally we reached last index of array which corrensponds 2, it is smaller than 7, 5 and 3 so we will move 2 as child of 3 to the left side.
