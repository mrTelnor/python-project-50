### Hexlet tests and linter status
[![Actions Status](https://github.com/mrTelnor/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mrTelnor/python-project-50/actions)

### Test Coverage
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mrTelnor_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mrTelnor_python-project-50)

---

# gendiff

**gendiff** — CLI-утилита и Python-библиотека для сравнения конфигурационных файлов  
в форматах **JSON** и **YAML**.

Показывает различия между файлами в удобном человекочитаемом формате.

Проект выполнен в рамках обучения на **Hexlet**.

---

## Demo

[![asciicast](https://asciinema.org/a/5a4pgApoYFIsjEcI.svg)](https://asciinema.org/a/5a4pgApoYFIsjEcI)

---

## Возможности

- Сравнение файлов **JSON** и **YAML**
- Поддержка **вложенных структур**
- Сортировка ключей в алфавитном порядке
- Отображение:
  - удалённых ключей (`-`)
  - добавленных ключей (`+`)
  - изменённых значений
  - неизменённых значений
- Использование как **CLI-утилиты** и как **Python-библиотеки**
- Функциональный подход (без классов)

---

## Установка

Установка CLI-инструмента:

```bash
uv tool install .