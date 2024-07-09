###########################################################
#  Computer Project #4
#  This program reads a file and displays the data in a format
#  that shows the maximum and minimum values of the livestock
#  The data is displayed in a format that shows the state, max year, max value, min year, min value
#  The program also prompts the user to enter a variety and displays the data in the format
#  The program has a menu that allows the user to search for a variety or terminate
#  The program also has a banner that displays the title
#  The program also has a prompt that asks the user to enter a file name
#  The program also has a prompt that asks the user to enter a variety
# The data is read from a csv file
#This program uses a dictionary to store the data
#This program sorts the data in the dictionary according to the max value and min value
###########################################################


import csv

STATES = ['Alaska', 'Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
    'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
    'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
    'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
    'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
    'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

HEADER_FORMAT = "{:<20s}{:>10s}{:>6s}{:>10s}{:>6s}"  # state, max year, max value, min year, min value in this order
DATA_FORMAT = "{:<20s}{:>10d}{:>6d}{:>10d}{:>6d}"  # state, max year, max value, min year, min value in this order

MENU = '''\nOptions:
    a - Search and display livestock for a variety
    q - Terminate the program'''

PROMPT = "\n:~Enter one of the listed options ~:"

'\n:~Enter a file name ~:'
"\nError in file name: {}. Please try again."
'Invalid option! Try again'
"\nLivestock: {}"
":~Please enter a variety ~:"
"\nThank you for exploring the world of Genetically Engineered Livestock with us!"

def display_banner():
    """
    Prints the banner on genetically engineered livestock adoption analysis.
    """

    banner = """
*****************************************************
*      Genetically Engineered Livestock             *
*         Adoption Analysis 2010-2024               *
*                                                   *
*   Analyzing Moo-ving Trends and Piggy Stats       *
*****************************************************
    """
    print(banner)

def open_file():
    """
    Prompts the user for a file name and opens the file.
    If the file is not found, it prompts the user to try again.
    Returns the file object.
    """

    while True:
        try:
            file_name = input("\n:~Enter a file name ~:")
            file = open(file_name)
            return file
        except FileNotFoundError:
            print("\nError in file name: {}. Please try again.".format(file_name))

def read_file(file):
    """
    Reads the file object and returns a list of lists containing the data.
    """
    data = {}
    reader = csv.reader(file)
    next(reader)
    for line in reader:
      if line[0] not in data:
          if line[0].strip() not in STATES:
           continue
          data[line[0]] = []  # state is the key, the rest of the data is the value
          data[line[0]].append(line[1:])
      else:
            data[line[0]].append(line[1:])
    return data

def show_options():
    """
    Displays the menu options.
    """
    print(MENU)

def get_option():
    """
    Prompts the user for an option and returns the option.
    """
    option = input(PROMPT)
    if option == 'a' or option == 'q':
        return option
    else:
        print('Invalid option! Try again')
        return get_option()

def get_variety():
    '''
    prompts the user for a variety and returns the variety
    '''
    variety = input(":~Please enter a variety ~:")
    return variety

def search_variety(data, variety):
    '''
    searches for the variety in the data and returns the state with the variety
    '''
    states = {}
    for state,lists in data.items():
        for li in lists:
            if variety in li:
                if state not in states:
                    states[state] = []
                    try:
                        if li[0] == 'Other States ':
                            pass
                        else:
                            states[state].append([li[0],li[1],li[2],int(li[3]),li[4],int(li[5])])
                    except :
                        pass
                else:
                    try:
                        if li[0] == 'Other States ':
                            pass
                        else:
                            states[state].append([li[0],li[1],li[2],int(li[3]),li[4],int(li[5])])
                    except :
                        pass
    new_dict={}
    for state in states:
        new_dict[state]={}
        for line in states[state]:
            if line[0] not in new_dict[state]:
                new_dict[state][line[0]]=[]
            new_dict[state][line[0]].append([line[1],line[2],line[3],line[4],line[5]])
    for values in new_dict:
        for val in new_dict[values]:
            new_dict[values][val].sort(key=lambda x: (x[4], -x[2]))
    return new_dict

def find_max_min(data,livestock):
    '''
    finds the max and min of the livestock in the data
    parameters:
    data: dictionary
    livestock: string
    returns: dictionary
    '''
    results = {}
    for state, livestock_data in data.items():
        if livestock in livestock_data:
            records = livestock_data[livestock]
            sorted_records = sorted(records, key=lambda x: (x[4], x[2]))
            max_value = max(sorted_records, key=lambda x: x[4])
            min_value = min(sorted_records, key=lambda x: x[4])
            results[state] = {
                'Max Year': max_value[2],
                'Max': max_value[4],
                'Min Year': min_value[2],
                'Min': min_value[4]
            }
    return results

def extract_live_stock(data):
    '''
    extracts the livestock from the data and returns the data

    '''
    livestock = []
    for state in data:
        for line in data[state]:
            if line not in livestock:
                livestock.append(line)
    return livestock
def display_data(data):
    '''
    displays the data in the format
    parameters: dictionary
    '''
    print(HEADER_FORMAT.format('State', 'Max Year', 'Max', 'Min Year', 'Min'))

def search_and_filter(data, variety):
    '''
    searches for the variety in the data and displays the data
    parameters: dictionary, string
    '''
    state_data = search_variety(data, variety)
    the_live_stock = extract_live_stock(state_data)
    the_live_stock.sort()
    myKeys = list(state_data.keys())
    myKeys.sort()
    state_data = {i: state_data[i] for i in myKeys}
    print(state_data)
    some_new_data= {}
    for values in the_live_stock:
        some_new_data[values] = find_max_min(state_data, values)
    for values in some_new_data:
        print("\nLivestock: {}".format(values))
        display_data(some_new_data[values])
        for state in some_new_data[values]:
            print(DATA_FORMAT.format(state, some_new_data[values][state]['Max Year'], some_new_data[values][state]['Max'], some_new_data[values][state]['Min Year'], some_new_data[values][state]['Min']))

def main():
    display_banner()
    file = open_file()
    data = read_file(file)
    show_options()
    option = get_option()
    while option != 'q':
        variety = get_variety()
        search_and_filter(data, variety)
        show_options()
        option = get_option()
    print("\nThank you for exploring the world of Genetically Engineered Livestock with us!")
    file.close()

# DO NOT CHANGE THE FOLLOWING 2 LINES
if __name__ == "__main__":
    main()
    