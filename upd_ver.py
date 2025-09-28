#!/usr/bin/env python3
"""
Простой скрипт для обновления версии приложения
Использование: python update_version.py [major|minor|patch]
"""

import re
import sys
import os


def update_version(version_type):
    # Читаем текущую версию
    with open('version.py', 'r') as f:
        content = f.read()
    
    # Ищем версию
    match = re.search(r'__version__ = "(\d+)\.(\d+)\.(\d+)"', content)
    if not match:
        print("Ошибка: Не могу найти версию в version.py")
        return
    
    major, minor, patch = map(int, match.groups())
    
    # Обновляем версию
    if version_type == 'major':
        major += 1
        minor = 0
        patch = 0
    elif version_type == 'minor':
        minor += 1
        patch = 0
    elif version_type == 'patch':
        patch += 1
    else:
        print("Ошибка: Используй major, minor или patch")
        return
    
    new_version = f'{major}.{minor}.{patch}'
    
    # Записываем новую версию
    new_content = re.sub(
        r'__version__ = "\d+\.\d+\.\d+"',
        f'__version__ = "{new_version}"',
        content
    )
    
    with open('version.py', 'w') as f:
        f.write(new_content)
    
    print(f"✅ Версия обновлена: {match.group(1)}.{match.group(2)}.{match.group(3)} → {new_version}")

    # 2. Обновляем README.md
    try:
        with open('README.md', 'r+', encoding='utf-8') as f:
            content = f.read()

            # Заменяем версию в README
            content = re.sub(
                r'### Version \s*\d+\.\d+\.\d+',
                f'### Version {new_version}',
                content
            )

            # Добавляем дату обновления
            if '### Version' not in content:
                #content = content.replace('## Version ', f'### Version {new_version}\n')
                content = f"### Version {new_version}\n{content}"
            
            f.seek(0)
            f.write(content)
            f.truncate()

            print("✅ README.md успешно обновлен!")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


def upd_ver(version_type):
    filename = 'README.md'
    new_version = "0.0.1"
    try:
        if not os.path.exists(filename):
            f = open(filename, 'w', encoding='utf-8')
            content = f"### Version {new_version}\n"
            f.write(content)
            f.close()
            print(f"✅ Создан файл: {filename}:\n{content}")
            return

        with open(filename, 'r+', encoding='utf-8') as f:
            content = f.read()
            # Ищем версию
            match = re.search(r'### Version\s+(\d+)\.(\d+)\.(\d+)', content)
            if not match:
                print("Ошибка: Не могу найти версию")
                content = f"### Version {new_version}\n{content}"
            else:
                major, minor, patch = map(int, match.groups())
                # Обновляем версию
                if version_type == 'major':
                    major += 1
                    minor = 0
                    patch = 0
                elif version_type == 'minor':
                    minor += 1
                    patch = 0
                elif version_type == 'patch':
                    patch += 1
                else:
                    print("Ошибка: Используй major, minor или patch")
                    return
                
                new_version = f'{major}.{minor}.{patch}'

                # Заменяем версию в README
                content = re.sub(
                    r'### Version\s*\d+\.\d+\.\d+',
                    f'### Version {new_version}',
                    content
                )
            
            f.seek(0)
            f.write(content)
            f.truncate()

            print(f"✅ Версия в файле {filename} обновлена до: {new_version}")
    
    except Exception as e:
        print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python update_version.py [major|minor|patch]")
        sys.exit(1)
    
    #update_version(sys.argv[1])
    upd_ver(sys.argv[1])