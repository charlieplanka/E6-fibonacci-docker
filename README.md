# Числа Фибоначчи

Приложение — это сервер, который принимает запрос на эндпоинт `/<k>`, где `k` — порядковый номер числа Фибоначчи, и возвращает JSON с посчитанным числом:
```
curl http://89.208.223.62/10

{
  "fibo": 34
}
```

Приложение запущено в **докер-контейнере** в [облаке](http://89.208.223.62/10) с использованием **nginx**.

Как запустить (на Linux):
1. Склонируйте репозиторий.
2. Соберите контейнер из файла docker-compose:
```
sudo docker-compose build
```
3. Запустите контейнер:
```
sudo docker-compose up
```

По умолчанию приложение запускается на 5000 порту.
