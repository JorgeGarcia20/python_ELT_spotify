from datetime import datetime, timedelta
from app import extract

if __name__ == '__main__':
    date = datetime.today() - timedelta(days=1)
    data_raw = extract(date)

    print(data_raw['items'])