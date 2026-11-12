# Practice Workshop — Week 11: Concatenating and merging

## Data

You will use monthly US data from FRED:

- `FRED_monthly_2000.csv` and `FRED_monthly_2010.csv`: the same columns, one decade each
- `UNRATE.csv`: unemployment rate (%), from 1948
- `FEDFUNDS.csv`: federal funds interest rate (%), from 1954

```python
import pandas as pd

df_2000 = pd.read_csv('../../data/FRED/FRED_monthly_2000.csv')
df_2010 = pd.read_csv('../../data/FRED/FRED_monthly_2010.csv')
unrate = pd.read_csv('../../data/FRED/UNRATE.csv')
fedfunds = pd.read_csv('../../data/FRED/FEDFUNDS.csv')
```

## Exercise 1: Concatenate rows

1. How many rows should the result have if you stack `df_2000` and `df_2010`? Predict first.
2. Combine them into one DataFrame with `pd.concat()`.
3. Check for repeated index labels with `.index.duplicated().sum()`.
4. Make its row index run from 0 without repeated index labels.

## Exercise 2: Merge tables

1. Check the first and last `DATE` in `unrate` and `fedfunds`. Do they cover the same months?
2. Merge `unrate` and `fedfunds` on `DATE` with an inner join. How many rows do you get?
3. Try an outer join. How many rows do you get now?
4. Explain the difference in row counts using what you found in step 1.

## Exercise 3: Handle missing values

In the outer-join result:

1. Find the rows with a missing `FEDFUNDS`. Which period do they cover?
2. Find the rows with a missing `UNRATE`. Why do you think these months are missing?
3. Fill missing `FEDFUNDS` with 0 in a copy of the result.
4. Does 0 mean the same thing as “unknown” here? Write one sentence explaining whether filling with 0 was a good choice.

**Think about:** Which join would you use if you only want months where both series are available?

## Exercise 4 (challenge): Many-to-one merge

```python
houses = pd.read_csv('../../data/ames_houses.csv')
```

1. Make a table with the mean `SalePrice` for each `Neighborhood` (see Week 10).
2. Merge it back onto `houses` so each house gets its neighborhood’s mean price.
3. Explain why each neighborhood mean appears many times in the result.
