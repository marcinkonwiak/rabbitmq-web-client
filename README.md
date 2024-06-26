<div align="center">
<h1>RabbitMQ Web Client</h1>
<h5>HTMX + FastAPI app for sending messages to RabbitMQ</h5>

![Work In Progress](https://img.shields.io/badge/Work%20In%20Progress-orange?style=for-the-badge)

<img src="screenshots/screenshot.png" width="800" alt="Screenshot"/>
</div>

## Installation

### Docker

```bash
docker run -p 8000:8000 -v rabbitmq-web-client:/app/data marcinkonwiak/rabbitmq-web-client
```

## Development

### Running the project locally

In a virtual environment:
```bash
pip install -r requirements-dev.txt
alembic upgrade head
uvicorn src.main:app --reload
```

### Compiling webpack
```bash
npx webpack
```

### Running Tailwind
```bash
npm install
npx tailwindcss -i ./src/static/css/input.css -o ./src/static/css/main.css --watch
```

### Testing

```bash
pytest
```
