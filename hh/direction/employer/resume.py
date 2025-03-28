from hh.core.paths import EmployerDirectionPath
from hh.direction.category import Category
from hh.direction.common.authorization import authorization
from hh.direction.employer.struct import SearchQuery


class Resume(Category):
    _path = EmployerDirectionPath.resumes.value
    _headers = dict()

    @authorization
    async def search(
            self,
            auth_headers: dict,
            text: str | None = None,
            page: int = 0,
            search_query: SearchQuery = SearchQuery()
    ):
        """
        Поиск резюме по заданным критериям.
        Роут из документации: https://api.hh.ru/openapi/redoc#tag/Poisk-rezyume/operation/search-for-resumes

        :param auth_headers: Заголовки авторизации, инъектится автоматически при помощи декоратора
        :param text: Поисковая фраза. Метод найдет резюме, в которых встречаются все слова заданной фразы.
        :param page: Номер страницы. По умолчанию 0.
        :param search_query: Параметры поиска.

        :return:
        """
        return await self.api_client.get(
            path=self._path,
            params=dict(text=text, page=page, **search_query.__dict__),
            headers=auth_headers
        )
