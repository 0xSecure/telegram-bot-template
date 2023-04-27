from typing import Literal

    
class TranslatorRunner:
    def get(self, path: str, **kwargs) -> str: ...
    
    start: Start


class Start:
    @staticmethod
    def hello(*, username) -> Literal["""Привет, { $username }!"""]: ...

