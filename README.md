###### Version 3.2.7
## Lead-Parser
Скрипт осуществляющий парсинг комуникационных телеграмм, полученных с помощью захвата сетевого трафика ПО wireshark.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Structure](#project-structure)
- [Repositories structure](#repositories-structure)
- [Acknowledgments](#acknowledgments)
- [Contact Information](#contact-information)

## Installation

1. Установить Python: https://www.python.org/
2. Установить VSCode: https://code.visualstudio.com/
3. Установить Wireshark: https://www.wireshark.org/
4. Установить Npcap драйвер: https://npcap.com/#download
5. Запустить VSCode и установить расширения:
```
    Python
    Python Debugger
    Python Environments
    GitLab Workflow
    GitLens
``` 
6. Клонировать репозиторий:`git clone http://git.logx.local/leadparser/leadparser-sca-sovetsk.git`
7. Из VSCode открыть папку репозитория в терминале и установить python пакеты:
```
pip install -r requirements.txt
```
8.  Проверить работу leadparser: [запустить скрипт](#usage)
9. Другие захваты трафика здесь: https://disk.yandex.ru/d/bfqx7Makctg1pw

## Usage

- Запуск из VSCode: `Ctrl + F5`
- Запуск скрипта в окне: `python leadparser.py`
- Запуск скрипта в консоли: `python leadparser.py -c`
```
    команды консоли:
        -h, --help        This document.
        -v, --version     Show version number.
        -r, --reset       Clear the process with pcap_files in pcap_folder and start it from the beginning.
        -f, --flush_log   Clear application log.
        -t, --time_stamp  Add time stamp to result folder name.
        -c, --console     Run in console mode only.
        -d, --default     Back to default parameters.
        -patch, --patch   Change patch version: x.x.X
        -minor, --minor   Change minor version: x.X.x
        -major, --major   Change major version: X.x.x
```
## Configuration

Настройки скрипта хранятся в файле leadparser.ini:

```
[DEFAULT]
name = leadparser
project = EvoCom_Sovetsk
capture_type = pcapng
processes = 1
threads = 3

[WAREHOUSE]
#    warehouse configuration from file = warehouse_config.json
name = sovetsk

[PCAPNG]
#    folder with *.pcapng files.
pcap_folder = pcapng\sovetsk\08_08_2025
#    %file_name%.pcapng - processing with certain file.
#    * - processing with all files in the pcap_folder.
pcap_file = *
	

[GENERAL]
#    tasks - commands for processing.
#    collect - collect all information about process and store in json files and collect.log as well.
#    crane - tracking for crane from parameter crane (see below in crane tab).
#    shuttle - tracking for shuttle from parameter shuttle (see below in shuttle tab).
#    sscc - tracking by sscc from parameter sscc (see below in product tab).
#    ropa - tracking by ropa from parameter ropa (see below in product tab).
#    connect - tracking for connection sessions.
tasks = collect, conveyor, crane, shuttle, sscc, ropa, connect

[CONVEYOR]
#    conveyor_n - tracking conveyor (n-number, see collect.log or conveyor.json).
#    * - tracking all conveyors.
conveyor = *

[CRANE]
#    crane_n - tracking crane (n-number, see collect.log or cranes.json).
#    * - tracking  all cranes.
crane = *

[SHUTTLE]
#    shuttle_n - tracking crane (n-number, see collect.log or shuttles.json).
#    * - tracking  all shuttles.
shuttle = *

[PRODUCT]
#    sscc: xxxxxxxxxxxxxxxxxx - tracking product by sscc code (see collect.log or sscc.json).
#    ropa: xxxxxxxxxx - tracking product by ropa code (see collect.log or ropa.json).
#    * - tracking by all over
sscc = *
ropa = *
```

В том случае, если запуск осуществляется в консольном режиме, в файл настроек потребуется вносить имена папок (pcap_folder) и файлов (pcap_file), 
содержимое которых скрипт будет обрабатываеть при работе.
При работе скрипта в режиме gui, в интерфейсе доступны поля для ввода соответствующих имен папок и файлов.

## Project Structure

```
leadparser-sca-evocom/          
├── app/
│   ├── main/
│   │   ├── __init__.py
│   │   ├── common.py           # общие функции
│   │   ├── config.py           # конфигурация (загрузка/сохранение настроек скрипта) 
│   │   ├── log.py              # логирование - использует модуль loguru
│   │   ├── proc.py             # обработка процессов - каждому файлу захвата может быть назначен свой процесс 
│   │   └── thread.py           # обработка потоков - каждая операция с фалом захвата рабивается на пул потоков
|   |
│   ├── tlg_data/
│   │    ├── __init__.py 
│   │    ├── cupture.py         # функции парсинга и трекинга объектов полученных из телеграмм
│   │    └── evocom_sovetsk.py  # описание структур телеграмм обьекта
|   |
│   ├── ui/
│   |    ├── __init__.py
│   |    ├── console.py         # консольный режим
│   |    └── tk.py              # gui обололчка
|   |
|   └── version/
|        ├── __init__.py
│        └── version.py         # управление версиями
|
├── logs/                       # папка для результатов парсинга телеграмм
├── pcapng/                     # файлы захвата wireshark в формате pcapng
|
├── .gitignore
├── leadparser.ini              # текущие настройки скрипта
├── leadparser.log              # логи работы скрипта
├── leadparser.py               # файл старта скрипта
├── LICENSE 
├── README.md
├── requirements.txt
└── warehouse_config.json       # конфгурация обьекта склада. IP-адреса, название сетевых устройств.
```

## Repositories structure
При работе с репозиторием необходимо придержиавться следующей структуры и наименования веток:
```
main                            # основная рабочая ветка (обновление только через pull request)
|
├── doc                         # документация по проекту
|
├── test                        # ветка для тестирования
|   │
│   ├── test/user1/test-x
│   └── test/user2/test-x
|
├── dev                         # разработка новых функций
|   |
|   ├── dev/user1/feat-x
|   └── dev/user2/feat-x
|
└── fix                         # исправления ошибок
    │
    ├── fix/user1/fix-x
    └── fix/user2/fix-x
```

Придерживаемся следующих сокращений:
```
dev/ (development): разработка
user/ (user contributor name): имя разработчика
feat/ (feature): для новых функций
fix/ (fix, hotfix, bugfix): для исправления ошибок
test/ (testing): для тестирования 
doc/ (documentation): для документации
```

## Acknowledgments

Полезные ресурсы:
* [Wireshark guide](https://habr.com/ru/articles/735866/)
* [VSCode guide](https://habr.com/ru/articles/490754/)
* [Python docs](https://pylessons.readthedocs.io/ru/latest/contents.html)

## Contact Information

- [@Vladimir Semenov](http://git.logx.local/u/vsemenov)
