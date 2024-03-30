# Population Data Service

This service parses population data of countries from the 
[United Nations population data table](https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959), 
saves it to a PostgreSQL database, and aggregates and displays summary data by regions.

### Implementation Details
- Data Source: United Nations population data table
- Scrapping: Implemented using Python with Request, BeautifulSoup for web scraping.
- Framework: Flask for print data
- ORM: SQLAlchemy for saving and working with data
- Database: PostgreSQL database is automatically deployed and managed using Docker Compose.

### Setup

1. Clone this repository:
    ```
   git clone https://github.com/Sparix/TestTask_PY
   cd <repository-directory>
   ```
2. Start the services using Docker Compose:
    ```
    docker-compose up get_data
    docker-compose up print_data  
    ```
   
### Description
- `get_data`: Parses, and saves population data to the PostgreSQL database.

- `print_data`: Retrieves data from the database and displays it on the screen 