# TradingView-test-case

Бегущая строка биржевых данных

# Setup

Что бы запустить проект, для начала следует загрузить зависимости `pip install -r requirements.txt`.  
После успешной загрузки, для запуска сервера `python manage.py runserver`.  
Теперь сервер будет доступен по адресу [http://localhost:8000](http://localhost:8000).  
Для начала сбора данных с API https://www.alphavantage.co/ `python manage.py stats_grabber`.  
stats_grabber отсылает запросы на https://www.alphavantage.co/ каждые 10 минут с паузой 20 секунд для каждого символа.  

# Описание API

`/api/v1/symbols/list` - для получения всех символов и их полей.  
При добавлении `?fields` будут возвращаться указанные поля.  
Например `/api/v1/symbols/list?fields=name,price,delta` вернет значения имени, цены и изменения цены для всех символов.  
Добавление `?page=2` вернет указанную страницу символов (размер страницы - 5 элементов).  
`?batch=3` вернет значения первых 3х элементов.  
Все перечисленные параметры можно комбинировать, т.е. при запросе `/api/v1/symbols/list?fields=name,precent,delta&page=2&batch=3`.  
Ответом будут имена, цена и изменение цены трёх символов со второй страницы.  

`/api/v1/symbols/data` - запрос без аргументов не возвращает ничего, доступные аргументы: ?fields и ?name.  
`/api/v1/symbols/data?name=BTC` ответит всеми полями символа с именем BTC.  
`/api/v1/symbols/data?name=BTC&fields=id,price,close` ответит полями id, цены, и цены за предыдущий день.  
