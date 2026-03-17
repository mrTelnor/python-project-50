### Hexlet tests and linter status
[![Actions Status](https://github.com/mrTelnor/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mrTelnor/python-project-50/actions)
[![Python CI](https://github.com/mrTelnor/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/mrTelnor/python-project-50/actions/workflows/python-ci.yml)

### Test Coverage
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=mrTelnor_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=mrTelnor_python-project-50)

---

# gendiff

**gendiff** — CLI-утилита и Python-библиотека для сравнения конфигурационных файлов  
в форматах **JSON** и **YAML**.

Показывает различия между файлами в удобном человекочитаемом формате и поддерживает несколько вариантов вывода:

- **Stylish** — человекочитаемый, древовидный формат с отметками +, - и пробелами для неизменённых ключей.
- **Plain** — текстовый формат для вывода изменений в виде описаний (Property 'a.b' was added/removed/updated).
- **JSON** — машиночитаемый формат, который легко использовать в скриптах и системах автоматизации.

Проект выполнен в рамках обучения на Hexlet.

---

## Demo

Ниже показан пример работы утилиты gendiff для трёх форматов вывода. Каждый формат подходит для разных задач: визуального анализа, логирования или интеграции с другими инструментами.

**Stylish** — древовидный формат, удобный для просмотра изменений человеком:

[![asciicast](https://asciinema.org/a/oFjXocf5cpAJOmka.svg)](https://asciinema.org/a/oFjXocf5cpAJOmka)

**Plain** — текстовый формат с описанием изменений, удобно использовать в CI/CD или логах:

[![asciicast](https://asciinema.org/a/YeEy8LcvJWAepMyY.svg)](https://asciinema.org/a/YeEy8LcvJWAepMyY)

**JSON** — машиночитаемый формат, который можно использовать в скриптах и для интеграции с другими системами:

[![asciicast](https://asciinema.org/a/7pe7GIaFH9Z47dka.svg)](https://asciinema.org/a/7pe7GIaFH9Z47dka)

---

## Возможности

- Сравнение файлов **JSON** и **YAML**
- Поддержка **вложенных структур**
- Сортировка ключей в алфавитном порядке
- Отображение различий в нескольких форматах:
  - **Stylish** — человекочитаемый древовидный формат с отметками +, - и пробелами для неизменённых ключей
  - **Plain** — текстовый формат с описанием изменений, например: Property 'a.b' was added/removed/updated (с указанием полного пути до свойства)
  - **JSON** — машиночитаемый формат для интеграции с другими системами
- Использование как **CLI-утилиты** и как **Python-библиотеки**
- Функциональный подход (без классов)

---

## Требования

- Python >= 3.10
- [uv](https://github.com/astral-sh/uv)

---

## Установка

Установка CLI-инструмента:

```bash
uv tool install .
```

После установки команда **gendiff** будет доступна в терминале.

---

## Использование

**CLI**

```bash
gendiff [-h] [-f {stylish,plain,json}] [-v] first_file second_file
```

- `first_file` — путь к первому файлу для сравнения
- `second_file` — путь ко второму файлу
- `-f`, `--format` — формат вывода:
  - `stylish` — человекочитаемый древовидный формат (по умолчанию)
  - `plain` — текстовый формат с описанием изменений
  - `json` — машиночитаемый формат JSON
- `-v`, `--version` — показать версию утилиты

Примеры:

```bash
gendiff file1.json file2.json           # вывод в формате stylish
gendiff file1.json file2.json -f plain
gendiff file1.json file2.json -f json
gendiff -v                              # показать версию
```

**Python API**

```python
from gendiff import generate_diff

diff = generate_diff('file1.json', 'file2.json', format_name='stylish')
print(diff)
```

Доступные значения `format_name`: `'stylish'` (по умолчанию), `'plain'`, `'json'`.

---

## Разработка

Установка зависимостей:

```bash
make install
```

Запуск линтера и тестов:

```bash
make check
```

Запуск тестов с отчётом о покрытии:

```bash
uv run pytest --cov=gendiff --cov-report=term-missing
```