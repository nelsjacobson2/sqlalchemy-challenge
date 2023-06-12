# Import the dependencies.
import datetime as dt
import numpy as np
import pandas as pd

# Import SQLAlchemy dependencies
from sqlalchemy import create_engine, func
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# Import Flask dependencies
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

# Create engine to connect to the database file
engine = create_engine("sqlite:////Users/nels.jacobson2/Desktop/Analytics_Class_Folder/05012023_Challenge/sqlalchemy-challenge/SurfsUp/Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# Create an instance of Flask
app = Flask(__name__)

# Define the root route
@app.route("/")
def home():
    return (
        f"Welcome to the Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation - Precipitation data for the last year<br/>"
        f"/api/v1.0/stations - List of weather stations<br/>"
        f"/api/v1.0/tobs - Temperature observations for the previous year<br/>"
        f"/api/v1.0/start_date - Min, Avg, and Max temperatures from a given start date<br/>"
        f"/api/v1.0/start_date/end_date - Min, Avg, and Max temperatures for a date range<br/>"
    )

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query the precipitation data for the last year
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).\
        order_by(Measurement.date).all()

    # Convert the results to a dictionary
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():
    # Query all weather stations
    results = session.query(Station.station).all()

    # Convert the results to a list
    station_list = list(np.ravel(results))

    return jsonify(station_list)

# Define the temperature observations route
@app.route("/api/v1.0/tobs")
def tobs():
    # Calculate the date one year ago from the last date in the database
    last_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0]
    one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query the temperature observations for the previous year for the most active station
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= one_year_ago).\
        filter(Measurement.station == 'USC00519281').\
        order_by(Measurement.date).all()

    # Convert the results to a list of dictionaries
    tobs_data = []
    for date, tobs in results:
        tobs_data.append({
            "date": date,
            "tobs": tobs
        })

    return jsonify(tobs_data)

# Define the start date route
@app.route("/api/v1.0/<start>")
def start_date(start):
    # Query the minimum, average, and maximum temperatures for dates greater than or equal to the start date
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).all()

    # Convert the results to a list of dictionaries
    temperature_data = []
    for result in results:
        temperature_data.append({
            "TMIN": result[0],
            "TAVG": result[1],
            "TMAX": result[2]
        })

    return jsonify(temperature_data)

# Define the start date and end date route
@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    # Query the minimum, average, and maximum temperatures for dates between the start and end dates (inclusive)
    results = session.query(
        func.min(Measurement.tobs),
        func.avg(Measurement.tobs),
        func.max(Measurement.tobs)
    ).filter(Measurement.date >= start).filter(Measurement.date <= end).all()

    # Convert the results to a list of dictionaries
    temperature_data = []
    for result in results:
        temperature_data.append({
            "TMIN": result[0],
            "TAVG": result[1],
            "TMAX": result[2]
        })

    return jsonify(temperature_data)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)



#################################################
# Flask Routes
#################################################
