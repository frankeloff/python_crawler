# Sitemap-Crawler
## Многопоточный скрипт, который делает карту сайта и загружает её в базу данных
### Быстрый старт
- Используйте `.env` файл. Вы можете скопировать `.env.example`
- Используйте `python3 -m venv ./.venv && source ./.venv/bin/activate && pip install -r requirements.txt` 
- Запустите команду `docker compose up -d --build`


| URL сайта                | Время обработки (HH:mm:ss) | Кол-во найденных ссылок | Имя файла с результатом (в expamles)   |
|--------------------------|--------------------------|---------------------------|----------------------------------------|
| http://crawler-test.com/ | 0:00:20                  | 415                       | sitemap_crawler-test.com               |
| https://www.google.com/  | 0:33:26                  | 18030                     | sitemap_www.google.com                 |
| https://www.python.org/  | 0:57:48                  | 34447                     | sitemap_www.python.org                 |
