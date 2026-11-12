# Practice Workshop — Week 8: Intro to pandas

Use a notebook or Python file to solve these tasks. Keep the original DataFrame unchanged when cleaning it.

```python
import numpy as np
import pandas as pd

orders = pd.DataFrame({
    "date": ["2026-01-05", "2026-01-12", "2026-02-03",
             "2026-02-18", "2026-03-02", "2026-03-15"],
    "region": ["North", "South", "North", "South", "North", "South"],
    "amount": [120.0, 95.0, np.nan, 140.0, 160.0, 105.0]
})
```

## Exercise 1: Inspect and clean

1. Display the first few rows and inspect the column types.
2. Count the missing values in `amount`.
3. Make a copy called `clean_orders`.
4. Fill its missing `amount` with the mean of the available amounts.
5. Check that `orders` still contains its missing value.

**Think about:** Should you calculate the mean before or after filling the missing value?

## Exercise 2: Select and summarize

1. Select orders with an amount greater than 110.
2. Select orders from `North` with an amount greater than 110.
3. Find the minimum, maximum, and mean cleaned amount.
4. Count how many orders belong to each region.

## Exercise 3: Work with dates

1. Convert `date` to dates using pandas.
2. Make a copy with `date` as its index.
3. Use `.loc[]` to select the February orders.
4. Explain one advantage of having dates as the index for this task.