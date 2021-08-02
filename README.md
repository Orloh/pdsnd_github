# Project: Udacity Explore US Bikeshare Data
_Basic Udacity project using Python to learn basic programming._

## Project Overview
In this project I made  use of Python to write a program that explores data related to a bike share system for three major cites in the United States - Chicago, New York City and Washington - I have written code to import the data and answer interesting questions about it by computing descriptive statistics. The program takes in raw input to create an interactive experience in the terminal to present these statistics.

## Project Details

### Bike Share Data
Bike sharing systems have become more popular and are being used more frequently in cities across the world over the past decade.

The use of information technologies has made easier to acquire data about the use of the bike-sharing systems which can be used to explore how the system is used.

In this project, I made use of data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United States, to uncover bike share usage patterns.

### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core **six (6)** columns:

+ Start Time
+ End Time
+ Trip Duration (in seconds)
+ Start Station
+ End Station
+ User Type

The Chicago and New York City files also have the following two columns:

+ Gender
+ Birth Year

The original files are much larger and messier, and you don't need to download them. These files had more columns and they differed in format in many cases. Some data wrangling was performed by the Udacity staff to condense these files to the above core six columns.

## The Program
The program is written in Python making use of the Numpy and Pandas libraries.

### Program Requirements
* Language: Python 3.8 or above
* Libraries: Pandas, Numpy and Time

### Running the program
The program is in the `bikeshare.py` file. Download the file and run the following command in the terminal: `python bikeshare.py`.

### Program Details
The program receives user input for the city, month and days of the week for which the user wants to view data.

Upon input the program displays the following calculated statistics:

#### Popular times of travel (i.e., occurs most often in the start time)

+ most common month
+ most common day of week
+ most common hour of day

#### Popular stations and trip

+ most common start station
+ most common end station
+ most common trip from start to end (i.e., most frequent combination of start station and end station)

#### Trip duration

+ total travel time
+ average travel time

#### User info

+ counts of each user type
+ counts of each gender (only available for NYC and Chicago)
+ earliest, most recent, most common year of birth (only available for NYC and Chicago)

### Acknowledments
Pending
