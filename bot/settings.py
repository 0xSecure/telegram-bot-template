import pydantic


class Settings(pydantic.BaseSettings):
    redis_dsn: str | None = None
    sentry_dsn: str | None = None
    database_dsn: str
    bot_token: str
