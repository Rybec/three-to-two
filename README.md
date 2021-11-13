# three-to-two
What is the simplest way to convert a roll of 3d6 into 2d6?


## Why did I do it?

Five year late response to Stand-up Maths: https://www.youtube.com/watch?v=hBBftD7gq7Y


## What does it do?

This rolls 3d6 in right angle trough oriented pointed away from the user, so that
each die has two upward faces, one on the right and one on the left.

The roll is converted into 2d6 by summing the right faces for one die and left
faces for the other, those sums are then put through the function (6 - (sum % 6)),
to get the final left and right roll values.

This program generates all possible permutations that could be rolled this way,
and then compares the roll distributions to that of rolling real 2d6.


## Summary of Results

This doesn't perfectly match the distribution of rolling 2d6, but it the biggest
deviation is a mere 0.5%.  When summing the 2d6 being simulated, the distribution
is very slightly flatter.  When considering the values as a pair, the biggest
deviation is 0.2%.  For table top games, this is well within reasonable tolerances,
and this deviation may actually be less than the deviation caused by wear on the
dice themselves.


## Program Output

```
3d6 rolled in a right angle trough, where the left and right sides are treated as
separate d6 rolls, using (6 - (sum % 6)), to get a range from 1 to 6.


Sum comparison

          2      3      4      5      6      7      8      9     10     11     12 
3d6:    2.6%   5.2%   8.3%  11.5%  14.1%  17.2%  14.1%  10.4%   8.3%   5.7%   2.6%
2d6:    2.8%   5.6%   8.3%  11.1%  13.9%  16.7%  13.9%  11.1%   8.3%   5.6%   2.8%


Roll pair frequency comparison

Pairs       3d6      2d6
(1, 1)      2.6%     2.8%
(1, 2)      2.6%     2.8%
(1, 3)      2.9%     2.8%
(1, 4)      2.9%     2.8%
(1, 5)      2.9%     2.8%
(1, 6)      2.9%     2.8%
(2, 1)      2.6%     2.8%
(2, 2)      2.6%     2.8%
(2, 3)      2.9%     2.8%
(2, 4)      2.9%     2.8%
(2, 5)      2.9%     2.8%
(2, 6)      2.9%     2.8%
(3, 1)      2.9%     2.8%
(3, 2)      2.9%     2.8%
(3, 3)      2.6%     2.8%
(3, 4)      2.9%     2.8%
(3, 5)      2.9%     2.8%
(3, 6)      2.6%     2.8%
(4, 1)      2.9%     2.8%
(4, 2)      2.9%     2.8%
(4, 3)      2.9%     2.8%
(4, 4)      2.6%     2.8%
(4, 5)      2.6%     2.8%
(4, 6)      2.9%     2.8%
(5, 1)      2.9%     2.8%
(5, 2)      2.9%     2.8%
(5, 3)      2.9%     2.8%
(5, 4)      2.6%     2.8%
(5, 5)      2.6%     2.8%
(5, 6)      2.9%     2.8%
(6, 1)      2.9%     2.8%
(6, 2)      2.9%     2.8%
(6, 3)      2.6%     2.8%
(6, 4)      2.9%     2.8%
(6, 5)      2.9%     2.8%
(6, 6)      2.6%     2.8%
```
