# Твоё общежитие

### Чтобы запустить приложение на локале:
```
uvicorn src.main:api.app --host 0.0.0.0 --port 3000 --reload
```

### Чтобы запустить тесты:
```
pytest
```

### Docker:
```
docker build -t your_dormitory_backend . 
docker run -d --name your_dormitory_backend -p 3000:3000 your_dormitory_backend
```