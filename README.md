Запуск приложения:
```
. start_app.sh
```
А еще можно порт прописать:
```
. start_app.sh -app_port 8001
```
Остановка приложения:
```
. stop_app.sh
```
Запрос на получение токена:
```
curl --location --request GET "http://127.0.0.1:8000/api/login/" --form "username=q" --form "password=q"
```
Запрос на сохранение статистики, поля views, clicks и cost - опциональные:
```
curl --location --request POST "http://127.0.0.1:8000/api/statistic/" -H "Authorization: Token ****" --form "date=****" --form "clicks=****" --form "views=****" --form "cost=****"
```
Запрос на показ статистики, поле order_by - опциональное:
```
curl --location --request GET "http://127.0.0.1:8000/api/statistic/" -H "Authorization: Token ****" --form "from=****" --form "to=****" --form "order_by=****"
```
Запрос на удаление всей статистики:
```
curl --location --request POST "http://127.0.0.1:8000/api/statistic/delete_all/" -H "Authorization: Token ****"
```
Задание: https://docs.google.com/document/d/1xs8PeM_7MHPD72QS1gGNOCt6eqb6COUq/
