# Desafio Estante Mágica
This is a back-end FastAPI application that has been dockerized with PostgreSQL and pgAdmin4. This application was made for a technical test at Estante Mágica, the application can register books, texts and images and generate magic keys for the books, which can then be
used for searching them via the API.

<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://github.com/tiangolo/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster" target="_blank">
    <img src="https://github.com/tiangolo/fastapi/workflows/Test/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/tiangolo/fastapi" target="_blank">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/tiangolo/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi" target="_blank">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

## Prerequisites

- Linux or WSL version 2
- Docker and Docker Compose
- A web browser

## Getting Started

Clone the repository:

```bash
git clone https://github.com/NixonMSilva/DesafioEstanteMagica
cd DesafioEstanteMagica
```

Create a .env file from the provided .env.example file:

```bash
cp .env.example .env
```

Edit the .env file and set the required environment variables.

Start the application:

```bash
docker-compose up -d
```

Run the migrations:

```bash
docker-compose run app sh -c 'alembic upgrade head'
```    

Open a web browser and navigate to http://localhost:8000/ to access the FastAPI application, or http://localhost:5050/ to access the pgAdmin4 interface.

## Usage

The FastAPI application provides a RESTful API for managing books. The API supports the following endpoints:

- POST /book/add: Creates a new book in the database.
- GET /book/list/{magic_key}: Returns a single book with the specified Magic Key.
- POST /text/add: Creates a new text in the database.
- POST /image/add: Creates a new image in the database.

To interact with the API, you can use a tool like curl or a REST client like Insomnia or Postman.

## pgAdmin4

pgAdmin4 is a web-based interface for managing PostgreSQL databases. To access the pgAdmin4 interface, open a web browser and navigate to http://localhost:5050/. Log in with the email and password specified in the .env file.

From the pgAdmin4 interface, you can create, view, and modify database objects like tables, views, and indexes.

## Contributing

Contributions are welcome! If you find a bug or would like to suggest a new feature, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT license](LICENSE).