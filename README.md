# exploratory_data_analysis


# Problem Definition

 a renewable energy company operates a farm of wind turbines. The turbines generate power based on wind speed and direction, and their output is measured in megawatts (MW). It is asked to build a data processing pipeline that ingests raw data from the turbines and performs the following operations:

●	Cleans the data: The raw data contains missing values and outliers, which must be removed or imputed.

●	Calculates summary statistics: For each turbine, calculate the minimum, maximum, and average power output over a given time period (e.g., 24 hours).

●	Identifies anomalies: Identify any turbines that have significantly deviated from their expected power output over the same time period. Anomalies can be defined as turbines whose output is outside of 2 standard deviations from the mean.

●	Stores the processed data: Store the cleaned data and summary statistics in a database for further analysis.


# Summary of steps followed
Loading the source Data: The data is loaded into a  DataFrame from the source directory and the timestamp is converted to a datetime object.
Cleaning Data:
Missing values are imputed with the column mean.
Outliers beyond 3 standard deviations are removed.

Summary Statistics:
Minimum, maximum, and average power output are calculated for each turbine.
here's some example output
turbine_id  min_output  max_output  avg_output 
    
0          11         1.5         4.5    2.959140

1          12         1.5         4.5    3.051210



Identify Anomalies:
Anomalies are detected as outputs beyond 2 standard deviations for each turbine.

--(No anomalies were detected; all turbines operated within 2 standard deviations from the mean.)

Storing the output data:

Final output saved in a database.
