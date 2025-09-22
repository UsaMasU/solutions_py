# Project Title
leadparser - скрипт осуществляющзий парсинг комуникационных телеграмм, полученных с помощью захвата сетевого трафика ПО wireshark.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [File Structure](#project-structure)
- [Repositories structure](#repositories-structure)
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

- Запуск скрипта с интерфейсом gui: `python leadparser.py`
- Запуск скрипта из терминала: `python leadparser.py -c`
- Запуск из VSCode: `Ctrl + F5`

## Configuration

Настройки скрипта хранятся в файле leadparser.ini:

```
[DEFAULT]
name = leadparser
version = EvoCom_Sovetsk_x.x.x
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
│   └── ui/
│        ├── __init__.py
│        ├── console.py         # консольный режим
│        └── tk.py              # gui обололчка
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
main                                            # основная рабочая ветка
|
├── docs                                        # документация по проекту
|
├── rel                                         # релизы версий 
|   │
│   ├── rel/vx.x.x                              # релиз версии x.x.x
│   └── rel/vx.x.x                              # релиз версии x.x.x
|
├── dev                                         # разработка
|   |
|   ├── dev/test/                               # тестирование перед мерджем с основной веткой
|   |   |
|   |   ├── dev/test/user1/test-x               # ползователь user 1
|   |   └── dev/test/user2/test-x               # ползователь user 2
|   |
|   ├── dev/rel/test/                           # тестирование версий перед мерджем с релизом
|   |   |
|   |   ├── dev/rel/test/vx.x.x/user1/test-x    # ползователь user 1
|   |   └── dev/rel/test/vx.x.x/user2/test-x    # ползователь user 2 
|   |    
|   └── dev/rel/                                # разработки версий 
|        │
|        ├── dev/rel/vx.x.x/user1/feat-x        # ползователь user 1 разработка
|        └── dev/rel/vx.x.x/user2/feat-x        # ползователь user 2 разработка
|
└── fix                                         # исправления
    |
    ├── fix/rel/test/                           # тестирование версий перед мерджем с релизом
    |   |
    |   ├── fix/rel/test/vx.x.x/user1/test-x    # ползователь user 1
    |   └── fix/rel/test/vx.x.x/user2/test-x    # ползователь user 2
    |    
    └── fix/rel/                                # исправления 
        │
        ├── fix/rel/vx.x.x/user1/fix-x          # ползователь user 1 исправления
        └── fix/rel/vx.x.x/user2/fix-x          # ползователь user 2 исправления
```
Придерживаемся следующих сокращений:
```
dev/ (development): разработка
user/ (user contibutor name): имя разработчика
vx.x.x/ (version x.x.x): версия
rel/ (release): релизы версий
feat/ (feature): для новых функций
fix/ (fix, hotfix, bugfix): для исправления ошибок
test/ (testing): для тестирования 
docs/ (documentation): для документации
```

## Contact Information

- [@Vladimir Semenov](http://git.logx.local/u/vsemenov)