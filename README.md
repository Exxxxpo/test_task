# Тестовое задание на позицию разработчика в тестировании *Тензор*

## Описание проекта
Автоматическое тестирование некоторых элементов сайта sbis.ru, tenzor.ru (по тестовому заданию).
## Технологии
- Python 3.12
- pytest 8.3
- selenium 4.23
## Особенности
- Используется Page Object Pattern.
- Используется встроенное логирование pytest.
- Используется фикстура для инициализации драйвера.
## Пример запуска проекта
Создать виртуальное окружение:
```
python3 -m venv env`
```
Активировать виртуальное окружение:
```
source env/bin/activate
```
Обновить pip:
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить тесты
```
pytest
```