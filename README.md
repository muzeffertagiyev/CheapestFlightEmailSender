# Flight Tracker and Notification System

This project is a flight tracking and notification system that alerts users about cheap flight deals. It integrates with Google Sheets to fetch data, queries a flight search API to find deals, and sends email notifications to users about these deals.

## Features

- **Fetch Flight Data**: Retrieves flight information from a Google Sheet.
- **Search Flights**: Queries an external flight API for flight deals.
- **Send Notifications**: Emails users about flight deals with links to book the flights.
- **Update IATA Codes**: Updates IATA codes in the Google Sheet if missing.

## Table of Contents


- [Usage](#usage)
- [Code Overview](#code-overview)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run this project, you need to have Python installed on your system. Follow these steps:

## Usage

1. **Run the Application**:

   Execute the `main.py` script to start the application:

   ```bash
   python main.py
   ```

   This will:
   - Fetch data from the Google Sheet.
   - Update missing IATA codes if needed.
   - Search for flight deals.
   - Send email notifications if flight prices drop below a certain threshold.

## Code Overview

### `data_manager.py`

This module interacts with Google Sheets API to:
- **Fetch Data**: Retrieve flight-related data from the Google Sheet.
- **Update Destination Codes**: Update IATA codes in the Google Sheet.
- **Get Customer Emails**: Retrieve user email data for notifications.

### `flight_data.py`

Defines the `FlightData` class that structures flight information, including:
- Price
- Origin city and airport
- Destination city and airport
- Outbound and return dates

### `flight_search.py`

This module interacts with the flight search API to:
- **Get Destination Code**: Retrieve the IATA code for a city.
- **Check Flights**: Search for flight deals based on parameters like origin, destination, and travel dates.

### `main.py`

The entry point of the application:
- Fetches flight data from the Google Sheet.
- Updates missing IATA codes.
- Searches for flight deals.
- Sends notifications to users if there are cheaper flights.

### `notification_manager.py`

Handles email notifications:
- **Sending Email**: Sends out emails to users with details of flight deals and booking links.

## Project Structure

- `data_manager.py`: Handles interaction with Google Sheets.
- `flight_data.py`: Structures flight data.
- `flight_search.py`: Queries flight search API.
- `main.py`: Main script to coordinate fetching data, searching for flights, and sending notifications.
- `notification_manager.py`: Sends email notifications.

## Environment Variables

Ensure that the following environment variables are set in your `.env` file:

- `SHEET_API`: Endpoint for Google Sheets API.
- `SHEET_USERS_API`: Endpoint for user data.
- `SHEETY_TOKEN`: Authorization token for Google Sheets API.
- `TEQUILA_ENDPOINT`: Endpoint for Tequila API (flight search).
- `TEQUILA_API_KEY`: API key for Tequila API.
- `EMAIL`: Email address for sending notifications.
- `PASSWORD`: Password for the email account used for sending notifications.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please submit a Pull Request. Ensure your contributions are well-documented and tested.

