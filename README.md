Программа показывает погоду по GPS координатам. Координаты берутся
из файла `local_settings.py` локально сохранного на компьютере пользователя. Содержимое файла:
```python
OPENWEATHER_TOKEN = ""  # paste API token here
OPENWEATHER_URL = (
    "https://api.openweathermap.org/data/2.5/weather?"
    "lat={latitude}&lon={longitude}&"
    "appid=" + OPENWEATHER_TOKEN + "&lang=ru&"
    "units=metric"
)
GPS_COORDS = () # paste your GPS coordinates here (latitude, longitude) 
```

Получение погоды по координатам происходит в сервисе
[OpenWeather](https://openweathermap.org/api).

Для запуска используйте python 3.10 (внешние библиотеки не требуются для работы
приложения), в `local_settings.py` проставьте API ключ для доступа к OpenWeather и 
запустите:

Для *nix систем
```bash
./weather
```
Для Windows
```
python weather.py
```


