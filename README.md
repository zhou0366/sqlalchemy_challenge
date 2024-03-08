# SQLAlchemy Surfs Up
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.![output]

## Precipitation Analysis
![output](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/04c62886-e935-4036-a355-911afe3da90b)
The precipitation for the 1-year shown displays around 4 times where there are large spikes in precipitation over a few days. Ignoring these spikes, the period with the least amount of precipitation occurs from January to April during this period. The heaviest precipitation occurs between August through December. Based on the plot of this year's data, the ideal period is between January and April. 

## Station Analysis
![output1](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/3a4d49b5-cddd-4321-a963-e4aff907b5dd)
The histogram shows that the station's median temperature is around 75 degrees with a skew to the left.


## Climate app results

Overview

Available Routes:
Precipitation: /api/v1.0/precipitation
Stations: /api/v1.0/stations
Temperatures for previous year: /api/v1.0/tobs
Temperatures from start date: /api/v1.0/start (date format yyyy-MM-dd)
Temperatures from between time range: /api/v1.0/start/end (date format yyyy-MM-dd)

Some screenshots are included to display the results of using the climate app

Home page

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/53756d13-fe7a-4ecb-b05f-9bd4dab5c984)

Precipitation page

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/0819f4ba-a174-4f62-b8de-04ef4e2a8d6c)

Station data

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/c72e0c06-8350-4247-b2be-053fd83ecfc2)

The past year's temperature observation page

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/8de55302-e455-4ab8-8e56-6be93c11397d)

Example of temperature observation page stats starting on January 1st 2012

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/a57f0f80-bdf7-4473-88b4-17cd97619ac3)

Example of temperature observation page stats between January 1st 2012 and January 1st 2017

![image](https://github.com/zhou0366/sqlalchemy_challenge/assets/22827830/fe6b250c-ab89-44da-a9bb-aa1840536d6f)

