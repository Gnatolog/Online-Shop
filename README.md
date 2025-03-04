# Онлайн магазин
![интернет магазин](https://alterainvest.ru/upload/iblock/61e/61e61fcf487d2e07681e433456c2cfb5.jpg)
___
# Описание
### Интернет магазин с реализацией необходимого функционала для успешной работы
___
# Цель проекта
### Веб приложение позволяет использовать промокоды для предоставления скидки их владельцам, а также расширенную работу с корзиной покупок.
___
# Какую проблему решает веб приложение
### Реализовывает полноценный интернет магазин с богатым функционалом
___
# Технологический стек
* Язык программирования: Python
* Фреймворк: Django
* Отладка приложения: Django Debug ToolBar
* Интеграция Redis c Django: django-redisboard
* Кеширования: Redis
* База данных: PostgreSQL
* Frontend: HTML,CSS, JS,
* Дизайн: Pixso, AdobePhotoshop
* Брокер сообщений: RabbitMQ
* Контейнерезация: Docker, Docker-compose
* Раздача статических файлов: NGINX
* Работник: Celery
___
# Архитектура веб приложения
* Архитектура асинхронных заданий построена на базе взаимодействия Django RabbitMQ и Celery
* Архитектура всего веб приложения соответсвует патерну проектирование MVT
___ 
# Функциональность веб приложения 
### Для пользователя реализованы следующие функции:
    * возможность регистрации в магазине
    * возможность входа в свой аккаунт
    * возможность фильтровать товар по категории
    * возможность поиска товара по названию
    * возможность вводить промокод при добавление товара
    * возможность добавлять товар в корзину
    * из корзины возможность вернуться к покупкам
    * в корзине возможность удалять товар
    * в корзине возможность менять количество товара
### Для администрирования приложения реализован следующиий функционал:
    * возможность создание категории товаров
    * возможность внесения товаров в каталог
    * возможность просматривать очередь заказов
    * возможность удаления пользователей
    * возможность рассылки сообщений пользователям
    * рассылка квитанций об оплате в pdf формате
    * возможность устанавливать размер скидки
    * возможность учитывать размер скидки при добавление в корзину
    * возможность получать скидку при введение промокода
    * возможность создавать промокоды со сроком действия
    * выводить пользователю товары схожие с купленными
    * выводить пользователю что покупают с этим товаром
    * возможность группировать пользователей
    * группы с различными павами доступа













