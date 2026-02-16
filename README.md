### Hexlet tests and linter status:
[![Actions Status](https://github.com/mrTelnor/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mrTelnor/python-project-50/actions)

### Test Coverage
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mrTelnor_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mrTelnor_python-project-50)

---

# gendiff

**gendiff** — CLI-утилита и Python-библиотека для сравнения двух JSON и YAML файлов.  
Показывает различия между конфигурационными файлами в удобном формате.

Проект выполнен в рамках обучения на Hexlet.

---

## Demo

[![asciicast](https://asciinema.org/a/ujZRDoTObLKZLRDF.svg)](https://asciinema.org/a/ujZRDoTObLKZLRDF)

## Возможности

- Сравнение двух плоских JSON-файлов
- Сортировка ключей в алфавитном порядке
- Отображение:
  - удалённых ключей (`-`)
  - добавленных ключей (`+`)
  - изменённых значений
  - неизменённых значений
- Возможность использования как CLI и как библиотеки
- Иммутабельный функциональный подход (без классов)

---

## Установка

Установка как CLI-инструмента:

```bash
uv tool install .
