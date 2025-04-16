from typing import Any

from core.authorization import authorization
from core.paths import EmployerDirectionPath
from direction.category import Category
from direction.employer.struct import SearchQuery


class Resume(Category):
    _path: str = EmployerDirectionPath.resumes.value
    _headers: dict[Any, Any] | None = None

    @authorization # type: ignore[misc]
    async def search(
            self,
            headers: dict[Any, Any],
            text: str | None = None,
            page: int = 0,
            search_query: SearchQuery = SearchQuery(),
    ) -> Any:
        """
        Поиск резюме по заданным критериям.
        Роут из документации: https://api.hh.ru/openapi/redoc#tag/Poisk-rezyume/operation/search-for-resumes

        :param text: Поисковая фраза. Метод найдет резюме, в которых встречаются все слова заданной фразы.
        :param page: Номер страницы. По умолчанию 0.
        :param headers: Дополнительные заголовки
        :param search_query: Параметры поиска.

        :return:
        """
        result: dict = await self.api_client.get(
            path=self._path,
            params=dict(text=text, page=page, **search_query.__dict__),
            headers=headers
        )
        return result
