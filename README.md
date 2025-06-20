## 1\. Файловая структура проекта

---

```plaintext
├── data/                                           # Директория для хранения данных.
│    ├── locators/                                  # Директория для хранения локаторов страниц.
│    │   ├── home_page_locators                     # Локаторы элементов страницы домашней страницы пользователя.
│    │   ├── login_page_locators                    # Локаторы элементов страницы авторизации.
│    │   ├── main_page_locators                     # Локаторы элементов главной страницы.
│    │   └── sqlex_locators                         # Локаторы элементов страницы sql-ex.ru.
│    │
│    └──  urls                                      # Файл для хранения url.
│
├── drivers/
│    ├── IEDriverServer.exe                         # Драйвер IExplorer (драйверы остальных загружаются через DriverManager).
│    └── driver_factory                             # Модуль фабрики браузеров.
│
├── pages/                                          # Директория с модулями страниц.
│    ├── base_page                                  # Класс и методы базовой страницы.
│    ├── home_page                                  # Класс и методы домашней страницы пользователя.
│    ├── login_page                                 # Класс и методы страницы авторизации.
│    ├── lifetime_page                              # Класс и методы страницы LifeTime Membership.
│    ├── main_page                                  # Класс и методы главной страницы.
│    ├── page_factory                               # Модуль фабрики страниц.
│    └── sqlex_page                                 # Класс и методы страницы sql-ex.
│
├── scripts/
│    ├── run_failed_tests                           # Скрипт запуска упавших в предыдущую сессию тестов.
│    ├── selenium-server                            # Сервисный файл для запуска кластера Selenium Grid.
│    ├── start_grid.bat                             # Скрипт запуска кластера Selenium Grid на Windows.
│    └── start_grid.sh                              # Скрипт запуска кластера Selenium Grid на Unix/MacOS.
│
├── tests/                                          # Исполняемые тесты.
│    ├── TS01_main_page/                            # Тесты главной страницы way2automation.com.
│    ├── TS02_navigation/                           # Тесты навигации на главной странице way2automation.com.
│    ├── TS03_autorization/                         # Проверка авторизации на way2automation.com.
│    ├── TS04_parametrized_authorization/           # Параметризованные поверки авторизации на way2automation.com.
│    ├── TS05_failing_tests_for_screenshot/         # Падающие тесты для проверки создания скриншотов.
│    ├── TS06_auth_with_cookies/                    # Проверка авторизации с помощью cookies на sql-ex.ru.
│    ├── TS07_js_executor/                          # Тесты с использованием JavascriptExecutor.
│    └── test_cases.md                              # Тест-кейсы
│
├── utils/                                          # Вспомогательные модули.
│    ├── cookies_helper                             # Модуль для работы с cookies.
│    └── ...
│ 
├── .gitignore  
├── conftest.py                                     # Конфигурационный файл
├── pytest.ini                                      # Конфигурационный файл для фреймворка pytest.
├── README.md                                       # Информационный файл. Вы находитесь здесь:)
└── requirements.txt                                # Список используемых библиотек и плагинов.
```
---

## 2. Кроссбраузерный запуск

---

| Браузер / тип запуска       | Команда запуска тестов                                                                                                                             |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Chrome / локально           | ```pytest``` _(Chrome определен как браузер по умолчанию)_                                                                                         |
| Firefox / локально          | ```pytest --browser=firefox```                                                                                                                     |
| Edge / локально             | ```pytest --browser=edge```                                                                                                                        |
| Chrome / Selenium Grid      | Запустить кластер Grid, если не запущен ранее: ```./scripts/start_grid.bat```<br>```pytest --grid``` _(Chrome определен как браузер по умолчанию)_ |
| Firefox / Selenium Grid     | Запустить кластер Grid, если не запущен ранее: ```./scripts/start_grid.bat```<br>```pytest --browser=firefox --grid```                             |
| Edge / Selenium Grid        | Запустить кластер Grid, если не запущен ранее: ```./scripts/start_grid.bat```<br>```pytest --browser=edge --grid```                                |
| С указанием своего Grid URL | ```./scripts/start_grid.bat```<br>```pytest --browser=[browser] --grid --grid-url=http://your-grid-hub:4444/wd/hub```                              |