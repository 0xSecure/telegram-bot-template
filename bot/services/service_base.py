from sqlalchemy.ext.asyncio import AsyncSession


class ServiceBase:

    def __init__(self, session: AsyncSession):
        self.session = session
