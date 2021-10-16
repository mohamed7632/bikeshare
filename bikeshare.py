import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    cities=['chicago', 'new york', 'washington']
    months=['january','february','march' ,'april','may','june']
    #week_days=[1,2,3,4,5,6,7]
    print("hello! let's explore some US bikeshare data!")
    while True:
                 
                    
                 city=input('would you like to see data for chicago , new york or washington \n' ).lower()
                 if city not in cities:
                     print("please enter a name of one  of these cities ( chicago , new york or washington)")
                     continue
                 check_filter=input("would you like to filter data by month, day , both or not at all? type 'none' for no time filter\n")
                 if check_filter== "none":
                      break
                 month=input('which month? january, february, march, april, may or june\n')
                 day=int(input('which day? please type your response as an integer(e.g., 1=sunday)\n'))

                 if city in cities and month in months and day in range(1,8) :
                      print( city ,month, day)
                      break
                 
            

    
    print('-'*40)
    return city, month, day,check_filter


def load_data(city, month, day,check_filter):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
   
    df=pd.read_csv(CITY_DATA[city],index_col=0)
    #convert Start Time to datetime formate
    df['Start Time']=pd.to_datetime( df['Start Time'])
    # extract month and day of week , hours from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.weekday_name 
    df['hour']= df['Start Time'].dt.hour
    
    if month != 'all':
       months = ['january', 'february', 'march', 'april', 'may', 'june']
       month=months.index(month)+1
       df=df[df['month']==month]
      
    if day != 'all':
       week_days=['sunday','monday','tuesday','wednesday','thursday','friday','saturday'] 
       df=df[df['day_of_week']==week_days[day-1].title()]
    


    return df


def time_stats(df,check_filter):
    """Displays statistics on the most frequent times of travel."""
    months=['january','february','march' ,'april','may','june']
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if check_filter == "day":
        most_common_mon=months[df['month'].value_counts().idxmax()]
        month_count=df['month'].value_counts().max()
        print("most popular month: ",most_common_mon," count: ",month_count,"filter: ",check_filter)
    # TO DO: display the most common day of week
    elif check_filter == "month":
       most_common_day=df['day_of_week'].value_counts().idxmax()
       day_count=df['day_of_week'].value_counts().max()
       print("most popular day: ",most_common_day," count: ",day_count,"filter: ",check_filter)
    
    # TO DO: display the most common start hour
    elif check_filter == 'both':
        most_common_hour=df['hour'].value_counts().idxmax()
        hour_count=df['hour'].value_counts().max()
        print("most popular hour: ",most_common_hour," count: ",hour_count,"filter: ",check_filter)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df,check_filter):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start_station=df['Start Station'].value_counts().idxmax()
    count_most_common_start_station=df['Start Station'].value_counts().max()
    print(" start station: ",most_common_start_station," count: -",count_most_common_start_station," filter: ",check_filter)
    # TO DO: display most commonly used end station
    most_common_end_station=df['End Station'].value_counts().idxmax()
    count_most_common_start_station=df['End Station'].value_counts().max()
    print("end station: ",most_common_end_station,",  count: -",count_most_common_start_station," filter: ",check_filter)
    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip=df.groupby(['Start Station','End Station']).size().idxmax()
    count_most_common_trip=df.groupby(['Start Station','End Station']).size().max()
    
    print("trip: ",most_common_trip,",","count: ",count_most_common_trip," filter: ",check_filter)                       
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df,check_filter):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
#     df['End Time']=pd.to_datetime(df['End Time'])
#     df['total_travel_time']=df['End Time'].values-df['Start Time'].values
    total_travel_time=df['Trip Duration'].sum()
    
    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
                                
    print("total durationd ", total_travel_time," count: ",len(df['Trip Duration'])," Average duration: ",mean_travel_time, "filter:",check_filter)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,check_filter):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_first_type=df['User Type'].value_counts().idxmax()
    user_first_type_counts=df['User Type'].value_counts().max()
    user_second_type=df['User Type'].value_counts().idxmin()
    user_second_type_counts=df['User Type'].value_counts().min()
    print(user_first_type,' : ',user_first_type_counts,' , ',user_second_type," : ",user_second_type_counts, 'filter: ',check_filter)
    # TO DO: Display counts of gender
    gender_1=df['Gender'].value_counts().idxmax()
    gender_1_counts=df['Gender'].value_counts().max()
                                
    gender_2=df['Gender'].value_counts().idxmin()
    gender_2_counts=df['Gender'].value_counts().min()
    print( gender_1,' : ',gender_1_counts,', ',gender_2,' : ',gender_2_counts, "filter:",check_filter)
     
    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_year_of_birth=df['Birth Year'].min()
    most_recent_year_of_birth=df['Birth Year'].max()
    most_common_year_of_birth=df['Birth Year'].mode()[0]     
    print("earliest year of birth : ",earliest_year_of_birth,"most recent year of birth : ",most_recent_year_of_birth,"most common year of birth",most_common_year_of_birth," filter: ",check_filter)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?\n").lower()
    start_loc = 0
    while (view_data=='yes'):
       print(df.iloc[start_loc:start_loc+5])
       start_loc += 5
       view_display = input("Do you wish to continue?: \n").lower()
       if view_display == 'no':
            break
           
    
def main():
    while True:
        city, month, day,check_filter = get_filters()
        df = load_data(city, month, day,check_filter)
        if 'Gender' in df:
            time_stats(df,check_filter)
            station_stats(df,check_filter)
            trip_duration_stats(df,check_filter)
            user_stats(df,check_filter)
        else:
            print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
            time_stats(df,check_filter)
            station_stats(df,check_filter)
            trip_duration_stats(df,check_filter)
        
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
