#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

#city_data include names of cities format csv
CITY_DATA = { 'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

MONTH_PARAMETER = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_PARAMETER = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

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
    city_info = ''
    while city_info.lower() not in CITY_DATA:
        city_info = input("\nSelect City: \n")
        if city_info.lower() in CITY_DATA:
            city = CITY_DATA[city_info.lower()]
        else:
            print("City not valid please try again.\n")

# TO DO: get user input for month (all, january, february, ... , june)
    month_info = ''
    while month_info.lower() not in MONTH_PARAMETER:
        month_info = input("\nSelect month or choose all: \n")
        if month_info.lower() in MONTH_PARAMETER:
            month = month_info.lower()
        else:
            print("Month not valid, please try again.\n")


# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_info = ''
    while day_info.lower() not in DAY_PARAMETER:
        day_info = input("\nSelect day or choose all: \n")
        if day_info.lower() in DAY_PARAMETER:
            day = day_info.lower()
        else:
            print("Day not valid, please try again.\n")

    print('-'*40)
    return city, month, day

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

    #dataframe
    df = pd.read_csv(city)

    # Get time/day/hour from Start Time column
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['dow'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour



    # filters
    if month != 'all':
        month = MONTH_PARAMETER.index(month)
        df = df.loc[df['month'] == month]

    if day != 'all':
        df = df.loc[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print("The most common month is: " + MONTH_PARAMETER[most_common_month].title())

    # TO DO: display the most common day of week
    most_common_dow = df['dow'].mode()[0]
    print("The most common day of week is: " + most_common_dow)

    # TO DO: display the most common start hour
    most_common_starthour = df['hour'].mode()[0]
    print("The most common start hour is: " + str(most_common_starthour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + most_common_start_station)

    # TO DO: display most commonly used end station
    most_common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + most_common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start and end station is: {}, {}"          .format(most_frequent_station[0],most_frequent_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total travel time is: " + str(travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types = df['User Type'].value_counts()
    print("The count of user by types is: \n" + str(types))

    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    # TRY  and EXCEPT is used to print the data correctly for cities without gender and birth year not available
    try:
        gender = df['Gender'].value_counts()
        minbirth = df['Birth Year'].min()
        maxbirth = df['Birth Year'].max()
        modebirth = df['Birth Year'].mode()
        print(gender.reset_index())
        print('Display earliest, most recent, and most common year of birth :',minbirth)
        print('Display earliest, most recent, and most common year of birth :',maxbirth)
        print('Display earliest, most recent, and most common year of birth :',modebirth)

    except:
        print('Column gender not available') # o Gender not available
        print('Column Bith Year not available') # o Gender not available

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to view next five row of raw data? Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while True:
            view_raw_data = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if view_raw_data.lower() != 'yes':
                break
            raw_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
