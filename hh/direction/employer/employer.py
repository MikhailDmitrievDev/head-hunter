from core.base.direction import BaseDirection
from direction.employer.resume import Resume
from direction.employer.vacancy.management import VacancyManagement


class EmployerDirection(BaseDirection):
    vacancy_management = VacancyManagement()
    resume = Resume()

