import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    cities={ 'chicago': 'chicago',
              'new york city': 'new_york_city',
              'washington': 'washington' }

    months={ 'january': 'january',
              'february': 'february',
              'march': 'march',
              'april': 'april',
              'may': 'may',
              'june': 'june',
              'all': 'all'}

    days={ 'monday': 'monday',
              'tuesday': 'tuesday',
              'wednesday': 'wednesday',
              'thursday': 'thursday',
              'friday': 'friday',
              'saturday': 'saturday',
              'sunday': 'sunday',
              'all': 'all'}

    while True:
        try:
            choice_c = input('Which city do you want to check?:')
            city = cities[choice_c.lower()]
            print ('Nice choice! You chooseed: {}'.format(city.title()))
            break
        except (KeyError, AttributeError):
            print('Please enter one of the followings: chicago, new york city, washington')


    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        try:
            choice_m  = input('In which month?:').lower()
            month = months[choice_m]
            print ('Nice choice! You chooseed: {}'.format(month.title()))
            break
        except (KeyError, AttributeError):
            print('Please enter one of the followings: january, february, march, april, may, june')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        try:
            choice_d  = input('In which day?:').lower()
            day = days[choice_d]
            print ('Nice choice! You chooseed: {}'.format(day.title()))
            break
        except (KeyError, AttributeError):
            print('Please enter one of the followings: monday, tuesday, wednesday, thursday, saturday, sunday')



    print( 'Summary of your choices: ', city.title(), month.title(), day.title())
    print('-'*60)
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
    df=pd.read_csv('{}.csv'.format(city))

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    print('Your data set based on your choices looks like this:','\n', df.head())
    return df

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""
    df['hour'] = df['Start Time'].dt.hour

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    months = ['january', 'february', 'march', 'april', 'may', 'june']

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', months[popular_month-1])
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day is: ',popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_ss = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_ss)

    # TO DO: display most commonly used end station
    popular_es = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_es)

    # TO DO: display most frequent combination of start station and end station trip
    df['Form']= 'FROM: '
    df['To']= '  TO: '
    df['Start & End Station']=   df['Form'] + df['Start Station'] + df['To'] + df['End Station']

    popular_ess = df['Start & End Station'].mode()[0]
    print('Most Popular Start and End Station combination:', popular_ess)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['dur']=df['End Time']-df['Start Time']
    # TO DO: display total travel time
    print ('The main descriptive statistics about the total travel time is the following:','\n', df['dur'].describe())
    print ('The 5 longest travel:','\n', df.sort_values(by=['dur'],ascending=False).head())
    # TO DO: display mean travel time
    print ('The mean travel time is :',  df['dur'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('counts of user types :', df['User Type'].value_counts())


    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        print ('counts of user types :', df['Gender'].value_counts() )
    else:
        print ('Your data set does not contain Gender information. Sorry...' )


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print (' The earliest year of birth :', int(min(df['Birth Year'])))
        print ('The most recent year of birth :', int(max(df['Birth Year'])))
        print ('The most common year of birth :', int(df['Birth Year'].mode()))
    else:
          print ('Your data set does not contain Birth Year information. Sorry...' )
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    answers = ['yes','no']
    question= ''
    while question not in answers:
         question = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
         if question in answers:
             print ('okay lets see.....................................:')
         else:
             print ('please write either "no" or "yes"')

    start_loc = 0

    question2 ='yes'

    while question2 =='yes':
        for i in range(start_loc, start_loc+5):
            print ("\n",df.iloc[i])
        start_loc =+5
        question2 = input('Do you want to check another 5 rows? (Type "yes" if yes or anything else if no: ').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
