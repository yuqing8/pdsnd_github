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
    city=input("Among chicago,new york city and washington,which city you want to look into?: ")
    
    while city not in CITY_DATA.keys():
        city=input("city you entered is invalid. Please choose a city from chicago, new york city,  washington: ").lower()
    
    # To get filter type from users
    print("Do you want filter by month,day,both or none?Type month,day,both or none: ")
    filter_type=input("").lower()
    
    while filter_type not in ['month','day','both','none']:
        filter_type=input("filter you entered is invalid. enter again: ")
    
    if filter_type=='month' or filter_type=='both':
    # TO DO: get user input for month (january, february, ... , june)
        month=input("please enter month from january through june: ").lower()
        
        while month not in ['january','february','march','april','may','june']:
            month=input("month you entered is invalid. please enter month from january through june: ").lower()
            
    else:
        month='all'
     
    if filter_type=='day' or filter_type=='both':      
    # TO DO: get user input for day of week (monday, tuesday, ... sunday)
        day=input("please enter day of week : ").title()
        
        while day not in ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']:
            day=input("day of week you entered is invalid. enter again: ").title()
    else:
        day='all'
          
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert the Start and End Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # create new columns: month and weekday
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    
    #filter df by month
    list_of_month=['all','january','february','march','april','may','june']
    cond1=(df['month'] == list_of_month.index(month))
    cond2=(df['weekday']==day)
    
    if month!='all' and day!='all':
        df=df[cond1&cond2]
    elif month!='all' and day=='all':
        df=df[cond1]
    elif month=='all' and day!='all':
        df=df[cond2]
    else:
        df=df
    return df
   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print("The most common month is: {}".format(
        str(df['month'].mode().values[0]))
    )

    # TO DO: display the most common day of week
    print("The most common month day of week: {}".format(
        str(df['weekday'].mode().values[0]))
    )

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    print("The most common start hour: {}".format(
        str(df['start_hour'].mode().values[0]))
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most common used station is: {}".format(
        str(df['Start Station'].mode().values[0]))
    )

    # TO DO: display most commonly used end station
    print("The most common used station is: {}".format(
        str(df['End Station'].mode().values[0]))
    )

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station']+ " to " + df['End Station']
    print("The most common start and end station combo is: {}".format(
        df['trip'].mode().values[0])
    )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is: {}".format(str(df['Trip Duration'].sum())))

    # TO DO: display mean travel time
    print("The total travel time is: {}".format(str(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    if "Gender" in df.columns:
        # TO DO: Display counts of user types
        df['User Type'].value_counts()

        # TO DO: Display counts of gender
        df['Gender'].value_counts()

        # TO DO: Display earliest, most recent, and most common year of birth
        print("The earliest birth is: {}".format(str(df['Birth Year'].min())))
        print("The most recent birth is: {}".format(str(df['Birth Year'].max())))
        print("The most common birth is: {}".format(str(df.mode()['Birth Year'][0])))
    else:
        print("Column Gender or User Type not found.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
       
        answer=input("Do you want to see 5 rows? enter yes or no : ")
        i=0
        while answer =='yes':
            i=i+5
            print(print(df.loc[i:i+5]))np
            answer=input("Do you want to see 5 more rows? enter yes or no : ")
            
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

    
"""citation:
https://knowledge.udacity.com/questions/181095
https://stackoverflow.com/questions/46380075/pandas-select-n-middle-rows
"""