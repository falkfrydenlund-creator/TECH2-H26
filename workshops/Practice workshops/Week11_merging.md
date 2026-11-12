# Practice Workshop — Week 11: Concatenating and merging

```python
import pandas as pd

january = pd.DataFrame({
    "shop_id": [1, 2],
    "month": ["Jan", "Jan"],
    "revenue": [120, 90]
})

february = pd.DataFrame({
    "shop_id": [1, 3],
    "month": ["Feb", "Feb"],
    "revenue": [140, 75]
})

shops = pd.DataFrame({
    "shop_id": [1, 2, 3, 4],
    "city": ["Oslo", "Bergen", "Tromsø", "Stavanger"]
})
```

## Exercise 1: Concatenate rows

1. Combine `january` and `february` into one sales DataFrame.
2. Make its row index run from 0 without repeated index labels.
3. How many rows should the result have?

## Exercise 2: Merge tables

1. Merge the combined sales data with `shops` on `shop_id`.
2. Use an inner join first. How many rows do you get?
3. Try an outer join. Which shop has no sales record?
4. Explain why a shop can appear more than once in the merged result.

## Exercise 3: Handle a missing value

In the outer-join result:

1. Find rows with missing `revenue`.
2. Fill missing revenue with 0 in a copy of the result.
3. Consider whether 0 means the same thing as “unknown revenue.” Write one sentence explaining your choice.

**Think about:** Which table should be on the left if you want to keep every shop?