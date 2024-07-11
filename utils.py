import os
from datetime import datetime, date as Date
from glob import glob
import re


def validate_date(date, format="%Y-%m-%d"):
    # Convert strings to datetime objects if input dates are strings
    try:
        if isinstance(date, str):
            date = datetime.strptime(date, format).date()
        elif isinstance(date, datetime):
            date = date.date()
        elif isinstance(date, Date):
            pass
        else:
            raise ValueError("Input must be a string or datetime object.")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")
    return date


def get_handles(dir: str):
    files = glob(f"{dir}/*.json")
    # handles = [os.path.basename(f).removesuffix(".json") for f in files]
    file_pattern = r"^(\w+)(_tweets_\d{4}-\d{2}-\d{2}_\d{4}-\d{2}-\d{2})?(\.json)$"
    handles = [re.sub(file_pattern, r"\1", os.path.basename(f)) for f in files]
    return handles
