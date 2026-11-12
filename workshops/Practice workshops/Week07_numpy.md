# Practice Workshop — Week 7: NumPy

Work through the tasks in order. Before running each result, predict what you expect to see.

## Exercise 1: Arrays and calculations

```python
import numpy as np

prices = np.array([5, 10, 15, 20, 25])
quantities = np.array([40, 32, 25, 16, 8])
```

1. Calculate the revenue at every price (`price × quantity`) without a loop.
2. Find the total revenue across all five observations.
3. Find the position of the observation with the highest revenue.
4. Use that position to print its price and revenue.

**Think about:** Does `np.argmax()` give you a position or a value?

## Exercise 2: Search a grid

Suppose profit at price `p` is:

`profit = p * (60 - p) - 200`

1. Create 61 candidate prices from 0 to 60 with `np.linspace()`.
2. Calculate the profit at every candidate price in one array operation.
3. Find the price with the highest profit.
4. Write a second version using a `for` loop. Do both versions agree?

## Exercise 3: Compare approaches

Create a list and a NumPy array containing the integers from 0 to 9,999.

1. Calculate the sum of each.
2. In a Jupyter notebook, use `%timeit` to compare their sum operations.
3. Write two sentences explaining your result. Does the result necessarily stay the same for very small collections?