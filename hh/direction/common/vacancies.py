from hh.core.settings import CommonDirectionPath


class CommonVacancies:
    """
    When you make a vacancy search, you can need to obtain information on vacancy distribution by a search criteria.
    For example, how many vacancies have a specified salary, or how many vacancies have
    a salary greater than specified one. To obtain this data with the regular method, you should make
    a separate request for each criteria needed.
    """

    path: str = CommonDirectionPath.vacancies.value

    async def get_vacancies(self):
        pass

    async def get_related_vacancies(self):
        pass

    async def get_similar_vacancies(self):
        pass
