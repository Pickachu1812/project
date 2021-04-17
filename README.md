Для запуска сервиса требуется ПО:
- Docker версии не ниже 19.0
- Docker-compose версии не ниже 1.25.0
- Утилита make для запуска команд через Makefile


Порядок установки:
1) Склонировать репозиторий командой: git clone https://github.com/Pickachu1812/project.git
2) Зайти в папку project
3) Запустить развертывание командой: sudo make deploy

Во время исполнекния команды будут созданы папки для размещения БД.
Также будут восстановлена из дампа таблица test с текстом.


Другие доступные команды:
- make stop:  Остановка контейнеров сервиса
- make start: Запуск уже собранных контейнеров сервиса после остановки
- make dump_db: Сделать дамп БД в файл database.dump
- make restore_db: Восстановить БД из файла database.dump
- make psql: Подключиться к контенеру с БД и запустить psql


Логгирование сервиса производится в syslog с тегами nginx,django,postgres для контейнеров фронтенда, бэкенда и БД соответственно.
