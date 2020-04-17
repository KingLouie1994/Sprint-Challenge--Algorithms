#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n) - a equals n**3 after the code runs n times so the while loop stops

b)

O(n log(n)) - The outer for loop is O(n) because it runs n times. The inner while loop is O(log n) because j doubles everytime it runs.
Because of this it's O(n) * O(log n) = O(n log(n))

c)

O(n) - This recursive code runs as often as the number of bunnies as input.

## Exercise II

When there is more than one floor we have to find the halfway point between the highest floor (floor n) and the lowest floor (floor 1)
floor 1 + floor n / 2 
In that floor we drop the first egg
If the egg breaks it means we are too high, if it doesn't break we can go higher
The new middle floor is the floor between the old middle floor and floor 1 or floor n 
We keep halving the number of floors and dropping eggs to make new decisions in which direction we have to go till we found the 
floor were the egg doesn't break
This is our floor f

This Exercise is an example for binary search. The runtime complexity is O(log(n))

