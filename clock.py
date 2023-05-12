import datetime
import time
import asyncio

def get_current_time() -> str:
    """Returns the current time as a string formatted as HH:MM:SS"""
    time = datetime.datetime.now().time()
    return time.strftime("%H:%M:%S")

def get_current_date() -> str:
    """Returns the current date as a string formatted as YYYY-MM-DD"""
    date = datetime.datetime.now().date()
    return date.strftime("%Y-%m-%d")

def get_date_or_time(query: str) -> str:
    """Returns the current date or time, depending on the query"""
    if "date" in query and "time" in query:
        return f"The current date is {get_current_date()} and the current time is {get_current_time()}"
    elif "time" in query:
        return get_current_time()
    elif "date" in query:
        return get_current_date()
    else:
        return "I don't know, include 'date' or 'time' in your query."
    

def set_timer(seconds: str) -> str:
    num_seconds = "".join([char for char in seconds if char.isnumeric() or char == "."])
    count = int(float(num_seconds))
    task = asyncio.run(timer(count))
    return f"Timer set for {count} seconds."

async def timer(seconds: int) -> str:
    """Counts down from the given number of seconds"""
    # remove all non-numeric characters
    
    await asyncio.sleep(seconds)
    print("Timer done.")
    return "Timer done."
