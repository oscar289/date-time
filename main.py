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
