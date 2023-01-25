# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.
from datetime import datetime, timedelta


from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.get_data()

flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = 'GYD'


if sheet_data[0]['iataCode'] == '':
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    data_manager.sheet_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
three_months_later = tomorrow.now() + timedelta(days=90)


for row in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=row['iataCode'],
        from_time=tomorrow,
        to_time=three_months_later
    )
    if flight is not None and flight.price < row['lowestPrice']:
        users = data_manager.get_customer_emails()
        emails = [row['email'] for row in users]
        names = [row['firstName'] for row in users]


        link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}." \
               f"{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
        message = f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} " \
                  f"to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} " \
                  f"to {flight.return_date}\n"

        # msg = message.encode('ascii', errors='ignore')
        # new_msg = msg.decode('ascii', errors='ignore')
        notification_manager.sending_email(message=message, emails=emails, google_flight_link=link)


