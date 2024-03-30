from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from database import models
from database.db import engine
from scrapping.scrapping import main_scrapper


def get_all_country():
    countries = main_scrapper()
    for country in countries:
        with Session(engine) as session:
            country_save_to_db(
                session,
                country.name,
                country.population,
                country.region
            )


def country_save_to_db(db: Session, name: str, population: int, region: str):
    try:
        country_save = models.Country(
            name=name,
            population=population,
            region=region,
        )
        db.add(country_save)
        db.commit()
        db.refresh(country_save)
    except IntegrityError:
        print(f"{name} country is already in the database or equal None")
    except ValueError:
        print(f"Invalid population value for {name} country")


if __name__ == '__main__':
    get_all_country()
