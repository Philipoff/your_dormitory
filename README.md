# Твоё общежитие
[![Backend CI](https://github.com/Philipoff/your_dormitory/actions/workflows/backend-ci.yml/badge.svg)](https://github.com/Philipoff/your_dormitory/actions/workflows/backend-ci.yml)  

[![Backend CD](https://github.com/Philipoff/your_dormitory/actions/workflows/backend-cd.yml/badge.svg)](https://github.com/Philipoff/your_dormitory/actions/workflows/backend-cd.yml)
[![Client CD](https://github.com/Philipoff/your_dormitory/actions/workflows/client-cd.yml/badge.svg)](https://github.com/Philipoff/your_dormitory/actions/workflows/client-cd.yml)
[![Admin CD](https://github.com/Philipoff/your_dormitory/actions/workflows/admin-cd.yml/badge.svg)](https://github.com/Philipoff/your_dormitory/actions/workflows/admin-cd.yml)

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
