# Practice Workshop — Week 9: Plotting

Give every plot a useful title and axis labels with units.

## Data

You will use `FRED_annual.csv`, which has US macro data for each year from 1954 to 2025:
`UNRATE` (unemployment rate, %), `INFLATION` (%) and `FEDFUNDS` (interest rate, %), among others.

```python
import pandas as pd
import matplotlib.pyplot as plt

annual = pd.read_csv('../../data/FRED/FRED_annual.csv')
```

## Exercise 1: Compare changes over time

1. Make a line plot of `UNRATE` against `Year`.
2. Add `INFLATION` to the same plot.
3. Add a legend.
4. Describe the two series in one or two sentences. Can you spot periods where both were high at the same time?

## Exercise 2: Compare years

1. Select the years from 2000 onwards.
2. Make a bar plot of the unemployment rate for each of those years.
3. Which year has the highest unemployment rate? What happened around then?
4. Explain why a line plot may be more useful than a bar plot when your main question is about change over time.

## Exercise 3: Choose a plot

Create a new column `REALRATE` for the real interest rate (`FEDFUNDS - INFLATION`).

1. Plot the real interest rate for every year.
2. Choose either a line or bar plot, and write one sentence explaining your choice.
3. Add a horizontal line at 0 with `plt.axhline()`. In which periods was the real interest rate negative?

**Check:** Can a reader understand each plot without looking at your code?
