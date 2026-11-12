# Practice Workshop — Week 8: Intro to pandas

Use a notebook or Python file to solve these tasks. Keep the original DataFrame unchanged when cleaning it.

## Data

Exercises 1 and 2 use `titanic.csv`, the passenger list of the Titanic. Its main columns are
`Survived` (1 = survived), `Pclass` (ticket class 1–3), `Sex`, `Age` and `Fare` (in pounds).

Exercise 3 uses `UNRATE.csv`, the monthly US unemployment rate in percent.

```python
import numpy as np
import pandas as pd

titanic = pd.read_csv('../../data/titanic.csv')
```

## Exercise 1: Inspect and clean

1. Display the first few rows and inspect the column types with `.info()`.
2. Count the missing values in every column. Which column has the most?
3. Make a copy called `clean_titanic`.
4. Fill its missing `Age` values with the mean of the available ages.
5. Check that `titanic` still contains its missing values.

**Think about:** Should you calculate the mean before or after filling the missing values? Is the mean age a good guess for a missing age?

## Exercise 2: Select and summarize

1. Select passengers who paid a fare greater than 100. How many are there?
2. Select female passengers in first class (`Pclass == 1`). How many are there?
3. Find the minimum, maximum and mean age in `clean_titanic`. Compare the mean with the mean in `titanic`.
4. Count how many passengers travelled in each class.
5. What share of all passengers survived? *Hint:* What is the mean of a column of 0s and 1s?

## Exercise 3: Work with dates

```python
unrate = pd.read_csv('../../data/FRED/UNRATE.csv')
```

1. Check the type of the `DATE` column. Then convert it to dates using pandas.
2. Make a copy with `DATE` as its index.
3. Use `.loc[]` to select the 2020 observations. In which month was unemployment highest?
4. Use `.loc[]` to select June 2025 to January 2026. Is anything missing?
5. Explain one advantage of having dates as the index for this task.
