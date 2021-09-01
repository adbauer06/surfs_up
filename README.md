# Surfs_up

## Project Overview
The purpose of this project was to analyze the weather, specifically temperature data, on Oahu for the months of June and December.  This information will be used in order to determine the sustainability of operating a surf and ice cream shop year-round. 


##  Resources
The following resources were used to complete this analysis:
- Input Data Sources:  hawaii.sqlite database containing weather measurements and weather station info for Oahu, Hawaii
- Software:  Jupyter Notebook, Visual Studio Code


## Project Analysis
### Analysis Overview
Temperature information for both the months of June and December for the years between 2010 and 2017 was queried.  The information was then uploaded into a dataframe in Jupyter Notebook where summary statistics could be run.  Following are the results of both analyses.

![june_temp_stats](https://github.com/adbauer06/surfs_up/blob/main/june_temp_stats.PNG)

![december_temp_stats](https://github.com/adbauer06/surfs_up/blob/main/december_temp_stats.PNG)

### Analysis Results 
- Both summaries were taken from a good size sample of data of 1517 and 1700 temperature readings, spanning 7 years.
- Overall, the month of June has higher temperatures than December. 
- The average temperature for June is about 4 degrees higher than December. 
- The maximum temperatures are fairly close, only two degrees different.
- There was a more significant difference in the minimum temperatures, eights degrees, showing December definitely has the potential to have cooler days.
- Comparing each month within itself, temperatures span a larger range in December than they do in June.



## Summary
Overall, there is not an extremely large difference between temperature data in June and December.  The average monthly temperatures are fairly close, as well as the high temperatures for the month.  The biggest concern would be the minimum temperature in December.  A couple of additional queries that could provide more insight into this would be:
- To summarize information by month and year, which could provide some insight as to whether this low was a random occurence one uncharacteristically cold year or if that is the norm.
    - For example, the original query can be modified to bring back just the year from the date in order to run analysis on that:  
    session.query(extract('year',Measurement.date), Measurement.tobs).filter(extract('month',Measurement.date) == 12))

- To summarize by month and day, to see if there are trends over the course of a month where the beginning or end of the month might be cooler, but temperatures are more moderate at other times within the month.
    - For example, the query can be modified to bring back just the day from the date in order to run analysis on that:  
    session.query(extract('day',Measurement.date), Measurement.tobs).filter(extract('month',Measurement.date) == 12))

This particular project focused specifically on temperature, but precipitation trends may be worth analyzing also, as they can possibly have an impact on temperature trends.
- For example, the query can be modified to bring back precip info rather than temps
    session.query(Measurement.date, Measurement.prcp).filter(extract('month',Measurement.date) == 12)


