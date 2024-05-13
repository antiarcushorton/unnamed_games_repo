from datetime import datetime
from datetime import timedelta

today = datetime.today().strftime('%Y-%m-%d')
thirty_days = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
