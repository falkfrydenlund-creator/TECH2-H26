# Practice Workshop — Week 7: NumPy

Work through the tasks in order. Before running each result, predict what you expect to see.

## Data

You will use `FRED_annual.csv`, which has US macro data for each year from 1954 to 2025.
Its columns are: `Year`, `GDP` (real GDP, billions of 2017 USD), `CPI`, `UNRATE` (unemployment rate, %),
`FEDFUNDS` (interest rate, %) and `INFLATION` (%).

```python
import numpy as np

file = '../../data/FRED/FRED_annual.csv'
data = np.genfromtxt(file, delimiter=',', skip_header=1)
```

## Exercise 1: Load and explore

1. Check the shape of `data`. How many years and how many columns are there?
2. Store the columns you need in their own arrays: `year` (column 0), `gdp` (column 1) and `unrate` (column 3).
3. Find the mean, lowest and highest unemployment rate.
4. Find the **position** of the year with the highest unemployment rate.
5. Use that position to print the year and its unemployment rate.

**Think about:** Does `np.argmax()` give you a position or a value?

## Exercise 2: Growth rates

GDP growth in percent from one year to the next is:

`growth = (gdp this year / gdp last year - 1) * 100`

1. Calculate the growth rate for every year in one array operation, without a loop.
   *Hint:* `gdp[1:]` and `gdp[:-1]` are the same array shifted by one year.
2. Why is your growth array one element shorter than `gdp`?
3. Find the year with the lowest growth. Be careful about which `year` values match your growth array.
4. Write a second version using a `for` loop. Do both versions agree?

## Exercise 3: Missing values and comparing approaches

Store column 5 in an array called `inflation`.

1. Calculate `inflation.mean()`. Why is the result `nan`?
2. Use `np.nanmean()` instead. What does it do differently?
3. Count the years when inflation was above 5%, first with a boolean mask (`inflation > 5`) and then with a `for` loop.
4. Make a list version of `gdp` with `gdp.tolist()`. In a Jupyter notebook, use `%timeit` to compare `sum()` on the list with `np.sum()` on the array.
5. Write two sentences explaining your result. Does NumPy have to be faster when the collection is this small (72 values)?

**Think about:** Why does this file need `np.genfromtxt()` rather than `np.loadtxt()`?
