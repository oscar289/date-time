import datetime

def seconds_until_end_of_year():
    """
    Calculates the number of seconds remaining until the end of the year.

    Returns:
      int: The number of seconds remaining until the end of the year.
    """
    x = datetime.datetime.now()
    s = int(x.strftime("%S"))
    m = int(x.strftime("%M"))*60
    h = int(x.strftime("%H"))*3600
    d = int(x.strftime("%j"))*86400

    # 1 an moins le temps deja passer
    seconds = 31536000 - (s + m + h + d)
    return seconds


seconds = seconds_until_end_of_year()
print(f"There are {seconds} seconds remaining until the end of the year.")


def seconds_until_end_of_year_2():
  # Get the current date and time
  now = datetime.datetime.now()

  # Compute the date and time for the end of the year
  end_of_year = datetime.datetime(now.year, 12, 31, 23, 59, 59)

  # Calculate the difference between the two dates and times
  time_delta = end_of_year - now

  # Return the total number of seconds in the time delta
  return time_delta.total_seconds()


seconds = seconds_until_end_of_year_2()
print(f"There are {seconds} seconds remaining until the end of the year.")
