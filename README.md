# MicroService Series - Product Feature
## [Part of Microsevices Architecture](https://github.com/OpenRnD007/microservices/)

## Introduction
The Product project is a Django-based web application that provides an interface to manage and display title information. It utilizes Django REST Framework for API development and includes features such as caching for improved performance.

## Installation

To set up the project on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/OpenRnD007/microservice-product-feature.git
```

2. Navigate to the project directory:
```bash
cd microservice-product-feature
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the migrations to create the database schema:

```bash
python manage.py migrate
```

5. Start the development server:
```bash
python manage.py runserver
```

## Usage

The project includes the following main components:

- `Titles`: A model representing the details of a title, including fields such as `tconst`, `titleType`, `primaryTitle`, and more.

- `Genres`: An abstract model representing a genre of titles.

- `TitlesSerializer`: A serializer class for the `Titles` model, handling the conversion between model instances and JSON.

- `HeroDetail` and `HeroAdd`: Views that handle the retrieval, creation, updating, and deletion of title instances.

- `CacheHelper`: A utility class for managing cache operations, improving the performance of the application.


## Contributing

Contributions to the Hero project are welcome! If you have suggestions for improvements or new features, feel free to fork the repository, make your changes, and submit a pull request.

## License

[MIT License](LICENSE.md)

## TODO
- Tests