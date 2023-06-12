# sqlalchemy-challenge

# Climate Analysis and API

This project involves the analysis of climate data using SQLAlchemy and the creation of a Flask API to provide access to the analyzed data. The project utilizes a SQLite database containing climate data for various stations in Hawaii.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project is divided into two parts:

1. Climate Analysis: The climate_starter.ipynb Jupyter Notebook contains the analysis of the climate data. It explores the precipitation and temperature trends, identifies the most active station, and analyzes the temperature data for a specific date range.

2. Climate App: The app.py file contains a Flask application that serves as the backend for the climate API. It provides various endpoints to access the climate data, including precipitation, station information, temperature observations, and statistics.

## Installation

To run the Climate Analysis and API locally, follow these steps:

1. Clone the repository.

2. Navigate to the project directory.

3. Install the required dependencies.

4. Set up the database:
- Ensure you have a SQLite database file named `hawaii.sqlite` in the root directory.

## Usage

To run the Climate App and access the API, follow these steps:

1. Ensure you have completed the installation steps mentioned above.

2. Start the Flask development server.

3. Once the server is running, open a web browser and go to `http://localhost:5000` to access the home page of the Climate App.

4. Navigate to the available API endpoints to retrieve the climate data.

## API Endpoints

The Climate App provides the following API endpoints:

- `/api/v1.0/precipitation`: Retrieves the last 12 months of precipitation data as a JSON object.
- `/api/v1.0/stations`: Retrieves the list of stations as a JSON array.
- `/api/v1.0/tobs`: Retrieves the temperature observations for the most active station over the last year as a JSON array.
- `/api/v1.0/<start>`: Retrieves the minimum, average, and maximum temperatures for dates greater than or equal to the specified start date as a JSON object.
- `/api/v1.0/<start>/<end>`: Retrieves the minimum, average, and maximum temperatures for dates between the specified start and end dates (inclusive) as a JSON object.

## Contributing

Contributions to the project are welcome! If you find any issues or want to suggest improvements, please open an issue or submit a pull request on the GitHub repository.
