# API Automation Tests

Проект с автоматизированными тестами для [API Course Test Server](https://github.com/Nikita-Filonov/qa-automation-engineer-api-course).  
Тесты написаны с использованием **Python**, **Pytest**, **Allure**, **Pydantic**, **Faker** и **HTTPX**.

## Обзор проекта


- **API-клиенты** для структурированного взаимодействия с эндпоинтами
- **Pytest-фикстуры** для повторного использования кода и создания удобной структуры тестов
- **Pydantic-модели** для строгой валидации данных
- **Валидация схем** для проверки соответствия API-контракту
- **Генерация тестовых** данных с помощью Faker для имитации реальных сценариев
- Отчетность с **Allure**
- **CI/CD** через GitHub Actions + автоматическая публикация **Allure-отчета** на **GitHub Pages**
## Allure Отчёт
<div align="center">
  <img src="https://github.com/Vladimir-KNHV/api-tests/blob/gh-pages/Desktop%20Screenshot%202026.07.20%20-%2015.14.32.14.png" alt="Allure Report Dashboard" width="80%"/>
</div>

[Открыть полный отчёт →](https://vladimir-knhv.github.io/api-tests/10/index.html)


## Начало работы

### Клонирование репозитория

Для начала работы необходимо клонировать репозиторий проекта с помощью Git:

```bash
git clone https://github.com/Vladimir-KNHV/api-tests.git
cd api-tests
```

### Создание виртуального окружения

Рекомендуется использовать виртуальное окружение для управления зависимостями проекта.  
Следуйте инструкциям для вашей операционной системы:

#### Linux / MacOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

После активации виртуального окружения установите зависимости проекта из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Запуск тестов с генерацией Allure-отчета

Для запуска тестов и создания Allure-отчета используйте команду:

```bash
pytest -m "regression" --alluredir=./allure-results
```

Команда запустит все тесты проекта и выведет результаты выполнения в терминал.

### Просмотр Allure-отчета

После выполнения тестов можно сгенерировать и открыть Allure-отчет с помощью команды:

```bash
allure serve allure-results
```

Команда автоматически создаст отчет и откроет его в браузере по умолчанию.