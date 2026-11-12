# Practice Workshop — Week 10: Grouping and aggregation

```python
import pandas as pd

sales = pd.DataFrame({
    "shop": ["A", "A", "B", "B", "A", "B", "A", "B"],
    "category": ["Books", "Food", "Books", "Food",
                 "Books", "Food", "Food", "Books"],
    "revenue": [120, 80, 90, 150, 160, 130, 100, 110]
})
```

## Exercise 1: One grouping variable

1. Find total revenue for each shop.
2. Find mean revenue per observation for each category.
3. Count the number of observations for each shop.
4. Explain why the total and mean answer different questions.

## Exercise 2: Two grouping variables

1. Find total revenue for each combination of `shop` and `category`.
2. Which shop–category combination has the greatest total?
3. Check your answer against the original rows.

## Exercise 3: Multiple statistics

Use `.agg()` to report both the mean and maximum revenue for each shop.

**Challenge:** Give the resulting columns descriptive names using named aggregation.

**Think about:** Does grouping change the original `sales` DataFrame?