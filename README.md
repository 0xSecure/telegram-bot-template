# Simple bot-architecture

This is a simple bot architecture written with [aiogram 3.x](https://github.com/aiogram/aiogram) and [sqlalchemy 2.x](https://docs.sqlalchemy.org/en/20/orm/)

You can see an example of a simple [bot](https://github.com/0xSecure/telegram-bot-template) implementation on this architecture 

* Services for the layer between business logic and data retrieval logic
* Fluent localization for more advanced and pleasant localization of the bot into different languages
* There is no strong attachment to ORM, because the service approach is used
* Sentry for modern and practical catching any errors not received at the QA stage

## Requirements:
* Python 3.10 and newer

## Stub-generation
```python scripts/fluent_cli.py -track-ftl resources/locales/ru -stub bot/stub.pyi```
