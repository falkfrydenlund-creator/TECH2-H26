# Practice Workshop — Week 10: Grouping and aggregation

## Data

You will use `ames_houses.csv`, which has 2,930 houses sold in Ames, Iowa, between 2006 and 2010.
Useful columns are `Neighborhood`, `BuildingType`, `CentralAir` (Y/N), `LivingArea` (square meters),
`Bedrooms` and `SalePrice` (in thousands of USD).

```python
import pandas as pd

houses = pd.read_csv('../../data/ames_houses.csv')
```

## Exercise 1: One grouping variable

1. Find the total value of all sales (`SalePrice`) for each `BuildingType`.
2. Find the mean sale price for each `BuildingType`.
3. Count the number of houses sold of each `BuildingType`.
4. Explain why the total and the mean answer different questions. Which building type wins on each?

## Exercise 2: Two grouping variables

1. Find the mean sale price for each combination of `BuildingType` and `CentralAir`.
2. Which combination has the highest mean price? Which has the lowest?
3. One combination is missing from the result. Which one, and why?
4. Check one of your answers against the original rows by filtering `houses` yourself.

## Exercise 3: Multiple statistics

1. Use `.agg()` to report the mean and maximum sale price for each `Neighborhood`.
2. Sort the result to find the three neighborhoods with the highest mean price.

**Challenge:** Use named aggregation to report the number of houses, the mean price and the mean living area for each neighborhood, with descriptive column names.

**Think about:** Does grouping change the original `houses` DataFrame?
