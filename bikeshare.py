import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
def editfor_github_project():
    print("First edit")

def info():
    print("raghad bayounes ")

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city_ch = input("\nPlease choose a city from the following: chicago, new york city, washington\n")
        city_chosen = city_ch.lower()
        if city_chosen not in ('chicago', 'new york city', 'washington'):
            print("Sorry , Try again!.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month_ch = input(
            "\nPlease choose a month from the following: january, february, march, april, may, june or 'all' if you prefer:\n")
        month_chosen = month_ch.lower()
        if month_chosen not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("Sorry , Try again!.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_cho = input(
            "\nPlease choose a day from the following: sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all' if you prefer:\n")
        day_chosen = day_cho.lower()
        if day_chosen not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
            print("Sorry , Try again!.")
            continue
        else:
            break

    print('-' * 40)
    return city_chosen, month_chosen, day_chosen


def load_data(city_chosen, month_chosen, day_chosen):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # loads data for the specified city into a dataframe
    df = pd.read_csv(CITY_DATA[city_chosen])

    # extract the start time
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract the day of week and month from start time column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['month'] = df['Start Time'].dt.month

    # if applicable to filter by day
    if day_chosen != 'all':
        # to create a new dataframe to filter by day
        df = df[df['day_of_week'] == day_chosen.title()]

    # if applicable to filter by month
    if month_chosen != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month_chosen = months.index(month_chosen) + 1

        # to create a new dataframe to filter by month
        df = df[df['month'] == month_chosen]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("The most common month is: ", months[common_month - 1])

    # display the most common day of week
    # extract day of week from the Start Time column
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    common_day = df['day_of_week'].mode()[0]
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    print("The most common day of week is: ", days[common_day])

    # display the most common start hour
    # extract the hour from start time column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is: ", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common used start station: ', df['Start Station'].mode()[0])

    # display most commonly used end station
    print('The most common used end station: ', df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip using groupby
    freq_stations = df.groupby(['Start Station', 'End Station'])
    print(freq_stations.size().sort_values(ascending=False).head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is:", df['Trip Duration'].sum())

    # display mean travel time
    print("The mean travel time is:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    try:
        usertype_count = df['User Type'].value_counts()
        print("\nUser type count is:", usertype_count)
    except KeyError:
        print("\nSorry! , there is no available data")

    # display counts of gender using value_count()
    try:
        gender_count = df['Gender'].value_counts()
        print("\nGender count is:\n", gender_count)
    except KeyError:
        print("\nSorry! , there is no available data.")

    # display earliest, most recent, and most common year of birth using min,max,mode
    # use try and except to handle the errors
    try:
        earliest_year = df['Birth Year'].min()
        print("\nThe earliest year of birth:", earliest_year)
    except KeyError:
        print("\nSorry! , there is no available data")

    try:
        max_year = df['Birth Year'].max()
        print("The recent year of birth:", max_year)
    except KeyError:
        print("\nSorry! , there is no available data")

    try:
        common_year = df['Birth Year'].mode()[0]
        print("The most common year of birth: ", common_year)
    except KeyError:
        print("\nSorry! , there is no available data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def view_data(df):
    """
    Displays raw data based on user request.
    """
    print(df.head())
    lines = 0
    while True:
        rawData = input('\n("Do you like to view five rows of the trip data? please enter yes or no")\n')
        if rawData.lower() != 'yes':
            return
        lines = lines + 5
        #print the five rows based on user request
        print(df.iloc[lines:lines+5])

def main():
    while True:
        city_chosen, month_chosen, day_chosen = get_filters()
        df = load_data(city_chosen, month_chosen, day_chosen)

        #call the functions
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        while True:
            rawData = input('\n("Do you like to view five rows of the trip data? please enter yes or no")\n')
            if rawData.lower() != 'yes':
                break
            view_data(df)
            break

        restart = input('\nWould you like to restart? please enter yes or no\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
    main()
