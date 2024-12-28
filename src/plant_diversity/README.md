# Plant Diversity data preparation
## Input
An input file is an ODS excel-type file that has multiple sheet tabs within it.
It's expected to be under this filepath: `data/input/plant_diversity/DIversity.ods`. 

## Sheet tabs
1. Part of this data represents a plot of land divided into smaller chunks that have their code names. Information about these chunks is stored within the sheet tab named 'Plots'.
2. Another part of the data represents metrics associated with the soil of each chunk _(e.g. pH)_.
3. Remaining data shows various plant species _(latin names)_ quantities within each chunk of land.

The data from points 2 and 3 is stored together within a single sheet tab in a table format.
Soil properties and species names are the headers of the table (columns).
Land chunk names are listed within the 1st column _('Plot_reference')_ and the chunks themselves are represented by a table row.

Data from points 2 and 3 was collected over multiple years. Each year's data has its own sheet tab named by that year's integer number (e.g. 2021)

## Problem statement
Data analysis code requires some data clean-up and restructuring.

1. While soil properties were present across all of the 'Year Sheets', the plant species column headers were not. Species found during one year, may not be found another year, so there's a column mismatch.

2. Additionally, some species names being lating, understandibly have spelling mistakes in them as well as shortened latin words within some sheets. Both these factors make it so the column name that would be considered unique, is programmatically not unique due to not being consistently entered across differnt Year Sheets.

3. Lastly, data analysis done using R language expects a single sheet where the data from all of the Year Sheets is combined. Normally, this wouldn't be an issue to combine within R, but the above mentioned complications make it easier to create this single CSV list in Python given the available experience.

# What is this code for?
Scripts within this sub-directory were made to:
1. Make it quicker to find/identify spelling mistakes and shortened words within plant species names _(column_checks.py)_.
2. Make it quick and easy to compile a **full set of unique** plant species column names and subsequently check which Year Sheets are missing which columns from the complete set _(column_checks.py)_.
3. Reindex each Year Sheet to have the **full set** of plant species columns, and then merge those sheets together into a single CSV for further data analysis via R _(plant_diversity.py)_.

## Outputs
Outputs are expected to go to the `data/output/plant_diversity/` directory.
1. The column checks script will produce multiple CSV files for extracting various column set data. Usecases will vary, the committed code only shows the last used files - there have been more.
2. The plant diversity script will output a single CSV file called `combined_sheets.csv` that contains merged Year Sheet data with the full set of columns, plus 1 additional Year column to show to which year the given row data came from.
