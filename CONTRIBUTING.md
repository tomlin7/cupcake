# CONTRIBUTING
Thank you for considering to contribute to Cupcake! To keep the code clean and for understanding our naming conventions, here are some  guidelines and a list of coding tools used. 

## Dependencies
For package management and dependencies this project uses [**poetry**](https://python-poetry.org/docs/#installation)

After installation of poetry, you will be able to install all dependencies of cupcake with the following command
```
poetry install
``` 

## Running Tests 
Cupcake uses [**pytest**](https://docs.pytest.org/) to run tests. After installation of poetry, you will be able to run the following command
```
poetry run pytest
```
Otherwise, you can also run pytest directly
```
pytest tests
```
