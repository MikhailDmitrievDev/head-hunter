from hh.core.base.direction import BaseDirection
from hh.direction.employer.resume import Resume
from hh.direction.employer.vacancy.management import VacancyManagement


class EmployerDirection(BaseDirection):
    vacancy_management = VacancyManagement()
    resume = Resume()

