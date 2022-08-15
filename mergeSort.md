# Merge Sort Project
<a href="https://www.patika.dev " target="_blank">Patika Dev</a>

<a href="https://app.patika.dev/courses/veri-yapilari-ve-algoritmalar/merge-sort-proje" target="_blank">Merge Sort Project</a>

<a href="https://app.patika.dev/pasha" target="_blank">My Patika Profile</a>

Question 1)<br>
Show the Merge Sort steps for the array above.<br>
The Merge Sort algorithm works as a divide-conquer-and-join strategy. What do I mean by that? First, we split our array into 2 parts 
until every element in the array is left alone. Then we compare and order these elements one by one with the elements next to them,
and we follow this process until the elements of the array come together. <br>
Okay lets dive into merging sort steps;<br>

[16, 21, 11, 8, 12, 22]<br>
|16, 21, 11| - |8, 12, 22|<br>
|16| - |21, 11| - |8, 12| - |22|<br>
|16| - |21| - |11| - |8| - |12| - |22|<br>
Okay this is the part where we started to compare each element with the elements next to them and combine them.<br>
|16| - |11, 21| - |8, 12| - |22|<br>
|11, 16, 21| - |8, 12, 22|<br>
[8, 11, 12, 16, 21, 22]<br>

Question 2)<br>
Show the time complexity as Big O notation<br>
O(nlogn)


