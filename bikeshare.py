import time
import pandas as pd
import numpy as np
import tabulate

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_city():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
    """
    city_list = ['chicago', 'new york', 'washington']
    city = input("Would you like to see data from Chicago, New York or Washington? ").lower()
    while True:
        if city in city_list:
            return city
        else:
            city = input('You typed wrong the city. Type: Chicago, New York or Washington: ').lower()

def get_month():
    """
    Asks user to specify a month to analyze.

    Returns:
    (str) month - name of the month ("jan", "feb", "mar", "apr", "may", "jun") to filter by, or "all" to apply no month filter
    """
    month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'all']
    month = input('Which month? Type: jan, feb, mar, apr, may, jun or all: ').lower()
    while True:
        if month in month_list:
            return month
        else:
            month = input('You typed wrong the month. Type: jan, feb, mar, apr, may, jun or all: ').lower()

def get_day():
    """
    Asks user to specify a day to analyze.

    Returns:
    (str) day - name of the day ("sun", "mon", "tue", "wed", "thu", "fri", "sat") to filter by, or "all" to apply no day filter
    """
    day_list = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'all']
    day = input('Which day of the week? Type:sun, mon, tue, wed, thu, fri, sat or all: ').lower()
    while True:
        if day in day_list:
            return day
        else:
            day = input('You typed wrong the day of the week. Type: mon, tue, wed, thu, fri, sat, sun  or all: ').lower()

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = get_city()

    # Get user to filter by month, day both, or no filter
    choice = input('Would you like to filter by month, day, both or none? ').lower()
    while True:
        if  choice == 'month':
            month = get_month()
            day = 'all'
            break
        elif choice == 'day':
            month = 'all'
            day = get_day()
            break
        elif choice == 'both':
            month = get_month()
            day = get_day()
            break
        elif choice == 'none':
            month, day = 'all', 'all'
            break
        else:
            choice = input("You typed wrong your choice. Type: month, day, both or none: ").lower()

    print('-'*40)
    return city, month, day

def filter_month(df, month):
    """
    Filters a data frame by month

    Returns:
        (DataFrame) df - filtered df by month
    """
    month_dict = {'jan': 1, 'feb': 2, 'mar': 3, 'apr':4, 'may': 5, 'jun': 6}
    return df[df['Start Time'].dt.month == month_dict[month]]

def filter_day(df, day):
    """
    Filters a data frame by week day

    Returns:
        (DataFrame) df - filtered df by week day
    """
    day_dict = {'mon': 0, 'tue': 1, 'wed': 2, 'thu': 3, 'fri': 4, 'sat': 5, 'sun': 6}
    return df[df['Start Time'].dt.weekday == day_dict[day]]

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    #Renames the first column of the data frame to Id
    df.rename(columns = {df.columns[0]: "Id"}, inplace=True)

    #Changes to datetime datatype
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # Filter by month
    if month != 'all':
        df = filter_month(df, month)

    # Filter by day of the week
    if day != 'all':
        df = filter_day(df, day)

    return df

def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    if month == 'all':
        common_m = df['Start Time'].dt.month_name().value_counts()
        print('The most commmon month is: {} (count: {}).'.format(common_m.index[0], common_m.iloc[0]))

    # Display the most common day of week
    if day == 'all':
        common_d = df['Start Time'].dt.day_name().value_counts()
        print('The most commmon day is: {} (count: {}).'.format(common_d.index[0], common_d.iloc[0]))

    # Display the most common start hour
    common_h = df['Start Time'].dt.hour.value_counts()
    print('The most commmon start hour is: {}:00 (count: {}).'.format(common_h.index[0], common_h.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start = df['Start Station'].value_counts()
    print('The most common starting station is: {} (count: {}).'.format(common_start.index[0], common_start.iloc[0]))

    # Display most commonly used end station
    common_end = df['End Station'].value_counts()
    print('The most common end station is: {} (count: {}).'.format(common_end.index[0], common_end.iloc[0]))

    # Display most frequent combination of start station and end station trip
    common_combo = df['Start Station'].str.cat(df['End Station'], sep =" - ").value_counts()
    print('The most frequent combination of start and end station trip is: {} (count: {}).'.format(common_combo.index[0], common_combo.iloc[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum(axis=0)
    print('The total time travelled by users is: {:.2f} minutes'.format(total_travel_time))

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean(axis=0, skipna=True)
    print('The mean travel time by users is: {:.2f} minutes'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User types:')
    try:
        user_types = df['User Type'].value_counts(dropna=False)
        for index, value in user_types.items():
            print('{}s: {}'.format(index, value))
    except:
        print('There is no User Type data to share')

    # Display counts of gender
    print('\nGender Count:')
    try:
      gender = df['Gender'].value_counts(dropna=False)
      for index, value in gender.items():
        print('{}: {}'.format(index, value))
    except:
      print('There is no gender data to share')

    # Display earliest, most recent, and most common year of birth
    print('\nBirth year stats:')
    try:
      common_y = df['Birth Year'].value_counts()
      recent_y = int(df['Birth Year'].max())
      earliest_y = int(df['Birth Year'].min())
      print('\n\t\tYear of birth')
      print('Earliest \t\t{}\nMost Recent \t{}\nMost Common \t{} (count: {})'.format(earliest_y, recent_y, int(common_y.index[0]), common_y.iloc[0]))
    except:
      print('There is no birth year data to share')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def get_confirmation(city, month, day):
    """
    Asks user to confirm the selected city and  filters.

    Returns:
        (bool) True or False - confirmation to selected city and filters. 'yes' = True and 'no' = False
    """
    print("You chose the following \nCity:{}\nMonth:{}\nDay:{}".format(city.title(), month, day))
    confirmation = input("Do you wish to continue? Type: 'yes' or 'no': ").lower()
    while True:
        if confirmation == 'yes':
            print('-'*40)
            return True
        elif confirmation == 'no':
            print('-'*40)
            return False
        else:
            confirmation = input("You typed wrong your choice? Type: 'yes' or 'no': ".format(city.title())).lower()

def print_n(index, data, n):
    """Displays n rows of a dataframe starting from the given index."""
  print(data[index: index + n])
  return index + n

def print_raw_data(df):
    """Displays the raw data 5 rows at a time."""
    while True:
    display_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
    if display_data.lower() != 'yes':
        break
    print(tabulate(df_default.iloc[np.arange(0+i,5+i)], headers ="keys"))
    i+=5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        confirmation = get_confirmation(city, month, day)
        if not confirmation:
            continue

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        print_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print()
            break

if __name__ == "__main__":
	main()
