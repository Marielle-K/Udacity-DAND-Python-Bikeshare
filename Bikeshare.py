import csv
import datetime
import time

f_c = open('chicago.csv','r')
rows = csv.reader(f_c)
chicago_w_header = list(rows)
chicago = chicago_w_header[1:]

f_n = open('new_york_city.csv','r')
rows = csv.reader(f_n)
new_york_w_header = list(rows)
new_york = new_york_w_header[1:]

f_w = open('washington.csv','r')
rows = csv.reader(f_w)
washington_w_header = list(rows)
washington = washington_w_header[1:]

def get_city():
    ''' (none) -> str
    Asks the user for a city and returns the name of the city for which the user would like to see bike share
    statistics as a string.
    '''
    while True:
        city = input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York, or Washington?\n')

        if city.lower() == 'chicago':
            return 'chicago'
            break
        elif city.lower() == 'new york':
            return 'new_york'
            break
        elif city.lower() == 'washington':
            return 'washington'
            break
        else:
            print("I'm sorry, your input was not recognized. Please enter 'Chicago', 'New York' or 'Washington'. Try again:")

def get_time_period():
    ''' (none) -> str
    Asks the user for a time period and returns the specified time period (month or day),
    or none when no time period is specified, as a string.
    '''
    while True:
        time_period = input('\nWould you like to filter the data by month, day, or not at'
                            ' all? Type "none" for no time filter.\n')

        if time_period.lower() == 'none':
            return 'none'
            break
        elif time_period.lower() == 'month':
            return 'month'
            break
        elif time_period.lower() == 'day':
            return 'day'
            break
        else:
            print("I'm sorry, your input was not recognized. Please enter 'day', 'month' or 'none'. Try again:")


def get_month():
    ''' (none) -> str
    Asks the user for a month between January and June and returns the specified month as a string.
    '''

    while True:
        month = input('\nWhich month? January, February, March, April, May, or June?\n')

        if month.lower() == 'january':
            return '-01-'
        elif month.lower() == 'february':
            return '-02-'
        elif month.lower() == 'march':
            return '-03-'
        elif month.lower() == 'april':
            return '-04-'
        elif month.lower() == 'may':
            return '-05-'
        elif month.lower() == 'june':
            return '-06-'
        else:
            print("Your input was not recognized. Please enter a month between January and June. Try again:")


def get_day():
    '''(str) -> int
    Asks the user for a day of the week and returns the day as an integer
    where 1 is the first day of the month and 31 the last day of the month.
    '''

    while True:
        day = int(input('\nWhich day? Please type your response as an integer.\n'))
        if day == 1:
            return '-01'
            break
        elif day == 2:
            return '-02'
            break
        elif day == 3:
            return '-03'
            break
        elif day == 4:
            return '-04'
            break
        elif day == 5:
            return '-05'
            break
        elif day == 6:
            return '-06'
            break
        elif day == 7:
            return '-07'
            break
        elif day == 8:
            return '-08'
            break
        elif day == 9:
            return '-09'
            break
        elif day == 10:
            return '-10'
            break
        elif day == 11:
            return '-11'
            break
        elif day == 12:
            return '-12'
            break
        elif day == 13:
            return '-13'
            break
        elif day == 14:
            return '-14'
            break
        elif day == 15:
            return '-15'
            break
        elif day == 16:
            return '-16'
            break
        elif day == 17:
            return '-17'
            break
        elif day == 18:
            return '-18'
            break
        elif day == 19:
            return '-19'
            break
        elif day == 20:
            return '-20'
            break
        elif day == 21:
            return '-21'
            break
        elif day == 22:
            return '-22'
            break
        elif day == 23:
            return '-23'
            break
        elif day == 24:
            return '-24'
            break
        elif day == 25:
            return '-25'
            break
        elif day == 26:
            return '-26'
            break
        elif day == 27:
            return '-27'
            break
        elif day == 28:
            return '-28'
            break
        elif day == 29:
            return '-29'
            break
        elif day == 30:
            return '-30'
            break
        elif day == 31:
            return '-31'
            break
        else:
            print("I'm sorry, your input was not recognized. Please enter day of the week as an integer.")

def filter_month(city, month):
    ''' (list, str) -> list
    Returns the filtered city file for the city specified by the user and the month
    specified by the user.
    '''
    city_month = []

    for row in city:
        if month in row[0]:
            city_month.append(row)

    return city_month


def filter_day(city, month, day):
    ''' (list, str) -> list
    Returns the filtered city file for the city specified by the user and the day of the month
    specified by the user.
    '''
    city_day = []

    for row in city:
        if month in row[0] and day in row[0]:
            city_day.append(row)

    return city_day

def popular_month(city):
    ''' (str, str) -> str
    Returns the most popular month to start a ride for the city selected by the user,
    where city_file is the output for the read_csv function and time_period for the get_time_period function.
    This function will only be called if the user entered 'none' as time_period.
    '''
    month_list = []

    for row in city:
        month = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').strftime('%B')
        month_list.append(month)

    pop_month = max(set(month_list), key=month_list.count)

    return pop_month

def popular_day(city):
    ''' (str, str) -> str
    Returns the most popular day to start a ride for the city selected by the user,
    where city_file is the output for the read_csv function and time_period for the get_time_period function.
    This function will only be called if the user entered 'none' or 'month' as time_period.
    '''
    day_list = []

    for row in city:
        day_of_week = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').strftime('%A')
        day_list.append(day_of_week)

    pop_day = max(set(day_list), key=day_list.count)

    return pop_day

def popular_hour(city):
    ''' (str, str) -> str
    Returns the most popular hour to start a ride for the city selected by the user,
    where city_file is the output for the read_csv function and time_period for the get_time_period function.
    '''
    hour_list = []

    for row in city:
        hour = datetime.datetime.strptime(row[0], '%Y-%m-%d %H:%M:%S').strftime('%H')
        hour_list.append(hour)

    pop_hour = max(set(hour_list), key=hour_list.count)

    return pop_hour

def trip_duration(city):
    ''' (str, str) -> str
    Returns the total trip duration and average trip duration for the city specified by the user over the
    time period specified by the user. If the user entered "none" as time_period, the total and average
    trip duration will be displayed per month.
    '''
    trip_int_list = []

    for row in city:
        int_trip = int(float(row[2]))
        trip_int_list.append(int_trip)

    total_trip = sum(trip_int_list)
    total_trip_format = time.strftime('%H:%M:%S', time.gmtime(total_trip))
    average_trip = total_trip/len(trip_int_list)
    average_trip_format = time.strftime('%H:%M:%S', time.gmtime(average_trip))

    return total_trip_format, average_trip_format

def popular_stations(city):
    ''' (str, str) -> str
    Returns the most popular start station and most popular end station for the city specified by the user over the
    time period specified by the user.
    '''
    start_stations = []
    end_stations = []

    for row in city:
        start = row[3]
        start_stations.append(start)

    for row in city:
        end = row[4]
        end_stations.append(end)

    pop_start_station = max(set(start_stations), key=start_stations.count)
    pop_end_station = max(set(end_stations), key=end_stations.count)

    return pop_start_station, pop_end_station

def popular_trip(city):
    '''(str, str) -> str
    Returns the most popular trip (start station - end station) for the city specified by the user over the
    time period specified by the user.
    '''
    start_stations = []
    end_stations = []

    for row in city:
        start = row[3]
        start_stations.append(start)

    for row in city:
        end = row[4]
        end_stations.append(end)

    start_end = list(zip(start_stations, end_stations))

    pop_pair = max(set(start_end), key=start_end.count)

    pop_trip_start = pop_pair[0]
    pop_trip_end = pop_pair[1]

    return pop_trip_start, pop_trip_end


def users(city):
    ''' (str, str) -> str
    Returns the total number of customers and subscribers that used a bike for the city specified
    by the user over the time period specified by the user.
    '''
    count_cust = 0
    count_sub = 0

    for row in city:
        if row[5] == 'Customer':
            count_cust += 1
        elif row[5] == 'Subscriber':
            count_sub += 1

    return count_cust, count_sub


def gender(city):
    '''(str, str) -> str
    Returns the numbers of men and women that used a bike in the city specified by the user
    over the time period specified by the user.
    '''
    count_male = 0
    count_female = 0

    for row in city:
        if row[-2] == 'Male':
            count_male += 1
        elif row[-2] == 'Female':
            count_female += 1

    return count_male, count_female


def birth_years(city):
    '''(str, str) -> str
    Returns the earliest, most recent and most popular birth year of the bike users for
    a city specified by the user and a time period specified by the user.
    '''
    birth_years = []

    for row in city:
        birth_year = row[-1]
        birth_years.append(birth_year)

    birth_year_list = list(filter(None, birth_years))

    most_popular_by = max(set(birth_year_list), key=birth_year_list.count).strip('.0')
    recent_by = max(birth_year_list).strip('.0')
    early_by = min(birth_year_list).strip('.0')

    return most_popular_by, recent_by, early_by

def display_data(city):
    ''' (str) -> dict
    Displays five lines of data for the city chosen by the user if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say no.
    '''
    index_start = 0
    index_end = 5

    while True:
        display = input('Would you like to view individual trip data? '
                    'Type \'yes\' or \'no\'. ')
        if display == 'yes' or display == 'Yes' or display == 'y':
            print(city[index_start:index_end])
            index_start += 5
            index_end += 5
        elif display not in ('no', 'n', 'No', 'stop'):
            print("I'm sorry, your input was not recognized. Please enter 'yes' or 'no'. Try again:")
        else:
            break

def statistics():
    ''' (none) -> none
    Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.
    '''
    # Filter by city (Chicago, New York, Washington)
    city_name = get_city()

    if city_name == 'washington':
        city_file = washington
    elif city_name == 'new_york':
        city_file = new_york
    elif city_name == 'chicago':
        city_file = chicago

    # Filter by time period (month, day, none)
    time_period = get_time_period()

    if time_period == 'month':
        month = get_month()
        filtered_month = filter_month(city_file, month)
        start_time = time.time()
        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        print("The most popular day for a ride is {}.".format(popular_day(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular hour of day for start time?
        print("The most popular hour of the day to start a ride is the hour starting at {}.00.".format(popular_hour(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the total trip duration and average trip duration?
        print("The total and average trip duration for this city are: {}.".format(trip_duration(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular start station and most popular end station?
        print("The most popular start and end stations are: {}.".format(popular_stations(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular trip?
        print("The most popular trip is made between the following start and end station: {}.".format(popular_trip(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What are the counts of each user type?
        print("This city has the following number of customers and subscribers: {}.".format(users(filtered_month)))
        print("That took %s seconds." % (time.time() - start_time))
        if city_file == washington:
            print("There are no more statistics available for Washington")
            pass
        else:
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the counts of gender?
            print("Number of men and women: {}.".format(gender(city_file)))
            print("That took %s seconds." % (time.time() - start_time))
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the earliest, most recent, and most popular birth years?
            print("Birth year of the oldest person, birth year of the youngest person, most popular birth year: {}.".format(birth_years(city_file)))
            print("That took %s seconds." % (time.time() - start_time))
    elif time_period == 'day':
        month = get_month()
        day = get_day()
        filtered_day = filter_day(city_file, month, day)
        start_time = time.time()
        # What is the most popular hour of day for start time?
        print("The most popular hour of the day to start a ride is the hour starting at {}.00.".format(popular_hour(filtered_day)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the total trip duration and average trip duration?
        print("The total and average trip duration for this city are: {}.".format(trip_duration(filtered_day)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular start station and most popular end station?
        print("The most popular start and end stations are: {}.".format(popular_stations(filtered_day)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular trip?
        print("The most popular trip is made between the following start and end station: {}.".format(popular_trip(filtered_day)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What are the counts of each user type?
        print("This city has the following number of customers and subscribers: {}.".format(users(filtered_day)))
        print("That took %s seconds." % (time.time() - start_time))
        if city_file == washington:
            print("There are no more statistics available for Washington")
            pass
        else:
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the counts of gender?
            print("Number of men and women: {}.".format(gender(city_file)))
            print("That took %s seconds." % (time.time() - start_time))
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the earliest, most recent, and most popular birth years?
            print("Birth year of the oldest person, birth year of the youngest person, most popular birth year: {}.".format(birth_years(city_file)))
            print("That took %s seconds." % (time.time() - start_time))
    else:
        start_time = time.time()
        # What is the most popular month for start time?
        print("The most popular month to start a ride is {}.".format(popular_month(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
        print("The most popular day for a ride is {}.".format(popular_day(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular hour of day for start time?
        print("The most popular hour of the day to start a ride isis the hour starting at {}.00.".format(popular_hour(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the total trip duration and average trip duration?
        print("The total and average trip duration for this city are: {}.".format(trip_duration(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular start station and most popular end station?
        print("The most popular start and end stations are: {}.".format(popular_stations(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What is the most popular trip?
        print("The most popular trip is made between the following start and end station: {}.".format(popular_trip(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        print("Calculating the next statistic...")
        start_time = time.time()
        # What are the counts of each user type?
        print("This city has the following number of customers and subscribers: {}.".format(users(city_file)))
        print("That took %s seconds." % (time.time() - start_time))
        if city_file == washington:
            print("There are no more statistics available for Washington")
            pass
        else:
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the counts of gender?
            print("Number of men and women: {}.".format(gender(city_file)))
            print("That took %s seconds." % (time.time() - start_time))
            print("Calculating the next statistic...")
            start_time = time.time()
            # What are the earliest, most recent, and most popular birth years?
            print("Birth year of the oldest person, birth year of the youngest person, most popular birth year: {}.".format(birth_years(city_file)))
            print("That took %s seconds." % (time.time() - start_time))

    # Display five lines of data at a time if user specifies that they would like to
    display_data(city_file)

    # Restart?
    restart = input('Would you like to restart? Type \'yes\' or \'no\'.')
    if restart.lower() == 'yes':
        statistics()

if __name__ == "__main__":
	statistics()

f_c.close()
f_n.close()
f_w.close()
