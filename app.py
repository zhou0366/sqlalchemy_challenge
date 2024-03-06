# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt
#################################################
# Database Setup
#################################################
# reflect an existing database into a new model
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return(
        f"Available Routes:<br/>"
        f"Precipitation: /api/v1.0/precipitation<br/>"
        f"Stations: /api/v1.0/stations<br/>"
        f"Temperatures: /api/v1.0/tobs<br/>"
        f"Temperatures from start: /api/v1.0/start<br/>"
        f"Temperatures from between time range: /api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    #link to db
    session = Session(engine)
    """Return all precipitation measurements with dates"""
    #query
    result = session.query(Measurement.date, Measurement.prcp).all()
    session.close()

    #create dictionary
    allprcp = []
    for date, prcp in result:
        prcp_dict = {}
        prcp_dict[date] = prcp
        allprcp.append(prcp_dict)
    return jsonify(allprcp)

@app.route("/api/v1.0/stations")
def stations():
    #link to db
    session = Session(engine)
    """Return all stations"""
    #query
    result = session.query(Station.id, Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()
    session.close()

    #create dictionary
    stations = []
    for id, station, name, latitude, longitude, elevation in result:
        station_dict = {}
        station_dict['id'] = id
        station_dict['station'] = station
        station_dict['name'] = name
        station_dict['latitude'] = latitude
        station_dict['longitude'] = longitude
        station_dict['elevation'] = elevation
        stations.append(station_dict)
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    #link to db
    session = Session(engine)
    """Return all temperature observations"""
    #query
    
    # Starting from the most recent data point in the database. 
    recent = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    last_date = dt.datetime.strptime(recent[0], '%Y-%m-%d')

    # Calculate the date one year from the last date in data set.
    last_year= dt.date(last_date.year - 1, last_date.month, last_date.day)
    result = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= last_year).all()
    session.close()

    #create dictionary
    alltobs = []
    for date, tobs in result:
        tobs_dict = {}
        tobs_dict["Date"] = date
        tobs_dict["Tobs"] = tobs
        alltobs.append(tobs_dict)
    return jsonify(alltobs)

@app.route("/api/v1.0/<start>")
def calc_start_date(start):
    #link to db
    session = Session(engine)
    """Get min, max, and average temperatures for dates after a start date"""
    #query
    result = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >=start).all()
    session.close()

    #create dictionary
    alltobs = []
    for min, max, avg in result:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["max"] = max
        tobs_dict["avg"] = avg
        alltobs.append(tobs_dict)
    return jsonify(alltobs)

@app.route("/api/v1.0/<start>/<end>")
def calc_date_range(start, end):
    #link to db
    session = Session(engine)
    """Get min, max, and average temperatures dates in a range"""
    #query
    result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

    #create dictionary
    alltobs = []
    for min, max, avg in result:
        tobs_dict = {}
        tobs_dict["min"] = min
        tobs_dict["max"] = max
        tobs_dict["avg"] = avg
        alltobs.append(tobs_dict)
    return jsonify(alltobs)

if __name__ == '__main__':
    app.run(debug=True)
