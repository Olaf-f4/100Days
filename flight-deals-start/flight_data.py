import requests

class FlightData:
    def __init__(self, location, leave_date, return_date):
        self.location = location
        self.leave_date = leave_date
        self.return_date = return_date

    def scan(self):
        query = requests.get(f'')