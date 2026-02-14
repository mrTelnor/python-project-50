### Hexlet tests and linter status:
[![Actions Status](https://github.com/mrTelnor/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mrTelnor/python-project-50/actions)

### Test Coverage
[![Coverage Status](https://sonarcloud.io/api/project_badges/measure?project=hexlet-boilerplates_python-package&metric=coverage)](https://sonarcloud.io/summary/new_code?id=hexlet-boilerplates_python-package)

---

# gendiff

**gendiff** — CLI-утилита и Python-библиотека для сравнения двух JSON-файлов.  
Показывает различия между конфигурационными файлами в удобном формате.

Проект выполнен в рамках обучения на Hexlet.

---

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
