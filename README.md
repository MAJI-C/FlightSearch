# Flight Deal Finder

This is a Python program that helps you find flight deals based on the destination and minimum price.

##### Flight:
The Flight class represents a single flight that can be booked. It contains information about the flight number, departure and arrival airports, departure and arrival times, the airline, and the price.

##### FlightSearch:
The FlightSearch class represents the search functionality of your flight booking system. It allows the user to search for available flights between two cities on a specified date. It takes in the departure city, arrival city, and date as input parameters and returns a list of available flights.

##### FlightTracker:
The FlightTracker class tracks the status of each flight in real-time. It provides information about the flight's current location, estimated arrival time, and any delays or cancellations.


### Getting Started 

#### Prerequisites

1. Python 3.x
2. pip3 

#### Installation

1. Clone the repository:

```python 
git clone https://github.com/your_username_/Project-Name.git
```
2. Install packages:

```python 
pip3 install -r requirements.txt
```
3. Create a .env file in the root directory with the following variables:
```python
SERVICE_ACCOUNT_FILE=<your-service-account.json>
SPREADSHEET_ID=<your-spreadsheet-id>
TQ_KIWI_API_KEY=<your-tequila-kiwi-api-key>
```
### Usage

1. Open your terminal.
2. Change directory to the root of the project.
3. Run the program with the following command:
```python 
    python3 main.py
```
4. The program will run and display any flight deals that meet your specified criteria.

### Built With

* Python 3.x
* Google Sheets API
* Tequila Kiwi API
