# HomeRegression


![neighborhood.jfif](./images/neighborhood.jfif?raw=true)

## Overview

This project encapsulates using multiple regression for modeling home sales data.

## Business Problem

We are a small company looking for properties to purchase and remodel to either sell or rent in the King’s County, WA housing market.  We will analyze housing data in order to understand the differing areas and factors which could lead to investment property strategy.

## Data

In the data directory is the kc_house_data.csv.  The data is over 21,000 records of home sales from Kings County, Washington.  The data columns are:
id - unique identified for a house <br>
date - house was sold <br>
price - is prediction target <br>
bedrooms- of Bedrooms/House<br>
bathrooms- of bathrooms/bedrooms<br>
sqft_living - footage of the home<br>
sqft_lot - footage of the lot<br>
floors - Total floors (levels) in house<br>
waterfront - House which has a view to a waterfront<br>
view - Has been viewed<br>
condition - How good the condition is ( Overall )<br>
grade - overall grade given to the housing unit, based on King County grading system<br>
sqft_above - square footage of house apart from basement<br>
sqft_basement - square footage of the basement<br>
yr_built - Built Year<br>
yr_renovated - Year when house was renovated<br>
zipcode - zip<br>
lat - Latitude coordinate<br>
long - Longitude coordinate<br>
sqft_living15 - The avg square footage of interior housing living space for the nearest 15 neighbors<br>
sqft_lot15 - The avg square footage of the land lots of the nearest 15 neighbors<br>

## Methods

We performed Inferential Analysis on over 21,00 home sales from Kings County and by removing any data with a outliers which had a z score larger than 3.  In a normal distribution 99% or all data falls with a z score of under 3.  
We also performed a multiple regression analysis which allows us to build a pricing model and assess the strength and relationship and importance of the different features and their relation to an estimate price of a property.
A new feature we created was distance from four major employment locations in Kings County.
We also created the district feature to divid the county into 10 separate districts based on zipcodes.
We also binned the Grade category into 3 bins, Low grade <=6, Medium 6-8, Hight Grade >8 to 13.

## Results

Our Model accounts for 80% of variance in the pricing data.  
The log(price) is equal to 8.1479 <br>
-0.02722363 * (bedrooms) + .04637777 * (bathrooms)<br>
+ 0.00074775 * (age) + 0.14952887 * (view_1)<br>
+ 0.13703141 * (view_2) + 0.54902297 * log(sqft_living)<br>
+ 0.06060631 * log(sqft_living15)<br>
- 0.02257943 * (distance) + 0.09696137 * (grade_6_8)<br>
+ 0.2341256 * (grade_8_13)<br>
+ 0.20976453 * (d_anerural_1) + 0.40560228 * (d_bellvue_7)<br>
+ 0.21335096 * (d_dtseattle_10) + 0.62208309 * (d_mercer_6)<br>
+ 0.67828833 * (d_nseattle_9) + 0.25678864 * (d_redmond_8)<br>
- 0.04204509 * (d_renton_5)<br>
+ 0.09428725 * (d_serural_2) + 0.18774062 * (d_vi_4)<br>
-0.05456986 * (distance * d_nseattle_9)<br>

A significant interaction we included is the distance multiplied by the existance of d_nseattle_9 category.

## Conclusions

We have observed with our analysis that the districts of N Seattle and Mercer Island increase the estimated house price the most in regard to the 10 districts.
A major opportunity is to find home which fall into the low grade category and possibly renovate them in order to change the grade to the middle to high categories in order to to increase the estimated sales price.

Influential factors in the model are the existence of a home in the N seattle district as compared to the base Fedway district increases the estimated price by 67%.  If a home is on Mercer Island the estimated price is increased by 62% compared to a home in Fedway district.
A home with a grade of 8 to 13 has a price increase of 23% compared  to a home with grade of <6.  The grading system ranks from 4 to 13 with 13 being top grade.
Distance away from a major employer has a negative effect on the estimated price.


## Next Steps

Identify other options instead of the defined 10 districts.<br>
Is the OLS the best model to use for this data?  Identify other models to use with multiple regression.<br>

## For More Information

See the full analysis in the [Jupyter Notebook](https://github.com/SunTzuLombardi/HomeRegression/blob/main/code/HomeRegression.ipynb) or review this [presentation](https://github.com/SunTzuLombardi/HomeRegression/blob/main/presentation.pdf)

For additional info, contact Daniel M. Smith at danielmsmith1@gmail.com

## Repository Structure

├── code<br>
│   ├── __init__.py<br>
│   ├── districts.py<br>
│   ├── outliers.py<br>
├── data<br>
├── images<br>
├── __init__.py<br>
├── README.md<br>
├── presentation.pdf<br>
├── gitbhub.pdf<br>
├── notebook_HomeRegression.pdf<br>
├── HomeRegression.ipynb<br>



