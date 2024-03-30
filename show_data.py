import typing

from sqlalchemy import func
from sqlalchemy.orm import Session, Query

from database.db import engine
from database import models
from flask import Flask, render_template

app = Flask(__name__)


def get_region_data(session: Session, region_data: typing.Any) -> dict:
    print(region_data)
    smallest_country = (
        session.query(models.Country.name, models.Country.population)
        .filter(models.Country.region == region_data.region,
                models.Country.population == region_data.smallest_population)
        .first()
    )
    biggest_country = (
        session.query(models.Country.name, models.Country.population)
        .filter(models.Country.region == region_data.region,
                models.Country.population == region_data.biggest_population)
        .first()
    )
    return {
        "name_region": region_data.region,
        "total_population": region_data.total_population,
        "smallest_name_country": smallest_country.name,
        "smallest_population_country": smallest_country.population,
        "biggest_name_country": biggest_country.name,
        "biggest_population_country": biggest_country.population
    }


@app.route("/")
def show_data():
    with Session(engine) as session:
        region_info = (
            session.query(
                models.Country.region,
                func.sum(models.Country.population).label("total_population"),
                func.min(models.Country.population).label("smallest_population"),
                func.max(models.Country.population).label("biggest_population")
            )
            .group_by(models.Country.region)
            .all()
        )
        context_region_info = [get_region_data(session, region_data) for region_data in region_info]

    return render_template("show_data.html", info=context_region_info)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
