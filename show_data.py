from sqlalchemy import distinct, func
from sqlalchemy.orm import Session, Query

from database.db import engine
from database import models
from flask import Flask, render_template

app = Flask(__name__)


def get_info_region(query: Query, region: str) -> dict:
    info_region = {
    }
    total_population = query.with_entities(
        func.sum(models.Country.population)
    ).scalar()
    biggest_country = query.order_by(models.Country.population.desc()).first()
    smallest_country = query.order_by(models.Country.population).first()
    info_region["name_region"] = region
    info_region["total_population"] = total_population
    info_region["smallest_name_country"] = smallest_country.name
    info_region["smallest_population_country"] = smallest_country.population
    info_region["biggest_name_country"] = biggest_country.name
    info_region["biggest_population_country"] = biggest_country.population
    return info_region


@app.route("/")
def show_data():
    with Session(engine) as session:
        countries = session.query(models.Country)
        regions = countries.distinct(models.Country.region).all()
        context_region_info = []
        for region in regions:
            region_query = countries.filter(models.Country.region == region.region)
            info_region = get_info_region(region_query, region.region)
            context_region_info.append(info_region)
    print("working it's strange")
    return render_template("show_data.html", info=context_region_info)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
