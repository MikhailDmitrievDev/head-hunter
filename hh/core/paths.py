import enum


class EmployerDirectionPath(enum.Enum):
    resumes = "/resumes"


class CommonDirectionPath(enum.Enum):
    vacancies = "/vacancies"
    auth = "/token"
