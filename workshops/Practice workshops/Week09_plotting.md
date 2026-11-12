# Practice Workshop — Week 9: Plotting

Use the same data for each plot, and give every plot a useful title and axis labels.

```python
import pandas as pd
import matplotlib.pyplot as plt

monthly = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "online": [80, 95, 90, 120, 135, 150],
    "in_store": [110, 105, 115, 100, 95, 90]
})
```

## Exercise 1: Compare changes over time

1. Make a line plot of `online` against `month`.
2. Add `in_store` to the same plot.
3. Add a legend.
4. Describe the two trends in one or two sentences.

## Exercise 2: Compare months

1. Make a bar plot of online sales by month.
2. Which month has the highest online sales?
3. Explain why a line plot may be more useful than a bar plot when your main question is about change over time.

## Exercise 3: Choose a plot

Create a new column for total monthly sales (`online + in_store`).

1. Plot the total for each month.
2. Choose either a line or bar plot.
3. Write one sentence explaining your choice.

**Check:** Can a reader understand each plot without looking at your code?