<h1 align="center">PDF-Parser</h1>

<p align="center">
<a href="https://github.com/pdf-reports-parser/backend/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/pdf-reports-parser/backend?color=red&style=for-the-badge"></a>
<a href="https://github.com/pdf-reports-parser/backend/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/pdf-reports-parser/backend?style=for-the-badge"></a>
<a href="https://github.com/pdf-reports-parser/backend/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/pdf-reports-parser/backend?color=green&style=for-the-badge"></a>
<a href="https://github.com/pdf-reports-parser/backend"><img alt="GitHub license" src="https://img.shields.io/github/license/pdf-reports-parser/backend?style=for-the-badge"></a>
<img alt="Build" src="https://img.shields.io/badge/build-docker-blueviolet?style=for-the-badge">
</p>
<img src="./read_me/PDF-start.png" width="100%">

<h2 align="center"><a  href="https://yandex.ru">Live Demo</a></h2>

### [Contributions are Welcome](https://github.com/pdf-reports-parser/backendhttps://github.com/pdf-reports-parser/backend)
## Description
Implementation of an application with a web interface designed for parsing data from PDF reports, storing them in a database and further output to reporting forms in the required formats (WORD)

## How to use
...

## System Requirements
To start the service, the following software must be installed on your working machine:
* docker
* docker-compose
* the "make" utility

## Technologies used
* service - python 3.10.2, with libraries:
  - Flask = "^2.0.3"
  - SQLAlchemy = "^1.4.32"
  - psycopg2-binary = "^2.9.3"
  - pydantic = "^1.9.0"

* data-base - postgresql 14
* containerization - docker

## Unique features of the service
...

## Start service
```bash
make service.run
```
## Support on Beerpay
...