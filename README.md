# 8-Queen-problem-simulated-annealing
Coursework done for 4th year Artificial Intelligence module.
Currently the answers are obtained via x,y coordinate system. An instance of obtained answer is shown below.


Board: randomly generated (x,y) locations for the board

(0, 0)
(1, 0)
(2, 4)

(3, 4)

(4, 6)

(5, 2)

(6, 0)

(7, 1)


Solution: Successfully optimized locations for 8 Queens

(0, 5)
(1, 2)
(2, 0)
(3, 6)
(4, 4)
(5, 7)
(6, 1)
(7, 3)


It will be futher improved as follows;

Generated Board:

|---|---|---|---|---|---|---|---|
| Q |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Q |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   | Q |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   | Q |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | Q |   |
|---|---|---|---|---|---|---|---|
|   |   | Q |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Q |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   | Q |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|

Solution: Successfully optimized locations for 8 Queens

|---|---|---|---|---|---|---|---|
|   |   |   |   |   | Q |   |   |
|---|---|---|---|---|---|---|---|
|   |   | Q |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| Q |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | Q |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   | Q |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   |   | Q |
|---|---|---|---|---|---|---|---|
|   | Q |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|   |   |   | Q |   |   |   |   |
|---|---|---|---|---|---|---|---|

It also outputs "Solution: Unsuccessful" when the algorithm is unable to generate a solution.
