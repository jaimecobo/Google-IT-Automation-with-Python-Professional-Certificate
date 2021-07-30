FILE_URL = "https://storage.googleapis.com/gwg-hol-assets/gic215/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""
    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""
    # Download the file over the internet
    response = requests.get(url, stream=True)
    lines = []

    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    # We want all employees that started at the same date 
    my_data = {}
    for row in reader: 
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        full_names ="{} {}".format(row[0], row[1])
        # append employee name of the same date to dic
        my_data[row_date] = my_data.get(row_date,[]) + [full_names]
    for employee_date in my_data.keys():
      if employee_date > start_date:
        print("Started on {}: {}".format(employee_date.strftime("%b %d, %Y"), my_data[employee_date]))  

def main():
    start_date = get_start_date()
    get_same_or_newer(start_date)

if __name__ == "__main__":
    main()