# NarodTropBot

>Телеграмм бот, который позволяет заходить на сайты заблокированные на территории РФ с помощью внп-ссылки.
---


 ### **Инструкция по запуску бота** ###
>все команды выполняются через терминал
  1. Клонируем репозиторий на свой компьютер 
      - `git clone https://github.com/sunrekay/NarodTropBot.git `
  2. После установки следуют перейти внутрь локальной папки, клонированного ранее репозитория
      - `cd <название вашей папки>`
  3. Далее следуют запустить процесс сборки образа с тегом <u>*my-bbot*</u>
      - `docker build -t narod .`
  4. И следующим шагом запустить Dockerfile
      - `docker run -it narod `

## Как работает бот?
>После того как боту отправляется ссылка на заблокированный сайт, он проверяет свою бд на наличие похожих запросов. Если такой запрос уже был, то отправляет его результат пользователю. Если такого запроса не было, то с помощь библиотеки "selenium" заходит на специальный веб-сайт, который занимается впн-ссылками, и забирает оттуда впн-ссылку, сохраняет ее в бд-ссылок и в бд-итории пользователя.
