from dataclasses import dataclass


@dataclass
class SearchQuery:
    """
        :param text_logic: Логика поиска. Возможные значения: `and`, `or`.
        :param text_field: Поле поиска. Возможные значения: `name`, `description`.
        :param text_period: Период поиска.
        Возможные значения: `experience`, `experience_company`, `experience_position`, `experience_description`
        :param text_company_size: Размер компании.
        :param age_from: Минимальная возрастная категория.
        :param age_to: Максимальная возрастная категория.
        :param area: ID региона или ID города.
        :param relocation: Возможность переезда.
        :param date_from: Дата, от которой нужно начать поиск.
        Значение указывается в формате ISO 8601 — YYYY-MM-DD или с точностью до секунды YYYY-MM-DDThh:mm:ss±hhmm.
        Нельзя передавать вместе с параметром
        :param date_to: Дата, до которой нужно искать.
        Значение указывается в формате ISO 8601 — YYYY-MM-DD или с точность до секунды YYYY-MM-DDThh:mm:ss±hhmm.
        Можно передавать только в паре с параметром date_from. Нельзя передавать вместе с параметром period
        :param employment: Тип занятости. Возможные значения: `full`, `part`, `project`, `volunteer`, `probation`
        :param experience: Опыт работы. Возможные значения: `noExperience`, `between1And3`, `between3And6`, `moreThan6`
        :param skill: Ключевые навыки. Указывается один или несколько идентификаторов ключевых навыков.
        Значения: `2716` - Системы тепло- и холодоснабжения, `3019` - Холодный цех, `3018` - Холодные продажи ???????
        :param gender: Пол соискателя. Возможные значения: `male`, `female`.
        :param label: Дополнительный фильтр. Возможные значения: `only_with_photo`, `only_with_salary`, `only_with_age`,
        `only_with_gender`, `only_with_vehicle`, `exclude_viewed_by_user_id`, `exclude_viewed_by_employer_id`,
        `only_in_responses`
        :param language: Знание языка. Можно указать несколько значений. Задается в формате language.level, где:
        language - язык: `ru`, `eng`. Подробный список получить через метод Directories.get_language_directory
        level - уровень: `a1`, `a2`, `b1`, `b2`, `c1`, `c2`, `l1`.
        Например: ita.c2
        :param currency: Валюта. `UZS`, `USD`, `UAH`, `RUR`, `KZT`, `KGS`, `GEL`, `EUR`, `BYR`, `AZN`.
        :param salary_from: Нижняя граница желаемой заработной платы (ЗП).
        :param salary_to: Верхняя граница желаемой заработной платы (ЗП).
        :param schedule: График работы. Возможные значения: `fullDay`, `shift`, `flexible`, `remote`,`flyInFlyOut`.
        :param order_by: Сортировка списка резюме.
        Возможные значения: `relevance`, `salary_asc`, `salary_desc`, `publication_time`
        :param citizenship: Страна гражданства соискателя. Можно получить из метода Directories.get_country_directory
        :param work_ticket: Страна, в которой у соискателя есть разрешение на работу.
        Можно получить из метода Directories.get_country_directory
        :param educational_institution: Учебные заведения соискателя. ??????
        :param search_in_responses: Если true, то поиск осуществляется только по резюме,
        которыми соискатели откликались на вакансии компании текущего пользователя,
        если false — поиск осуществляется по всем резюме.
        :param by_text_prefix: Если true, включается поиск по префиксу.
        Для каждого параметра text будут находиться не только полные совпадения слов,
        но еще и слова, начинающиеся с text
        :param driver_license_types: Категории водительских прав соискателя. Возможные значения: `A`, `B`, `C`, `D`,
        `E`, `BE`, `CE`, `DE`, `TM`, `TB`
        :param vacancy_id: Идентификатор вакансии для поиска похожих резюме.
        Необходимо передавать идентификатор активной вакансии работодателя или вакансии работодателя в архиве
        :param per_page: Количество элементов (по умолчанию — 20, максимальное значение — 100)
        :param professional_role: Профессиональная роль. Элемент справочника Directories.get_professional_role_directory
        :param folder: Один или несколько идентификаторов папок с отобранными резюме.
        Если данный параметр передан, поиск будет ограничен содержимым указанных папок.
        Можно передавать идентификаторы нескольких папок, например: `folder=111&folder=222&folder=333`
        :param include_all_folders: Признак, указывающий, нужно ли вести поиск по всем папкам с отобранными резюме.
        Если у менеджера есть доступ к избранным папкам, то поиск проходит по умолчанию в избранных папках.
        Если передать параметр false, то поиск не будет ограничен папками.
        Если в одном запросе будут переданы параметры folder и include_all_folders, вернется ошибка 400 Bad Request
        :param job_search_status: Статус работы соискателя. Возможные значения: `active_search`, `looking_for_offers`,
        `not_looking_for_job`, `has_job_offer`, `accepted_job_offer`.
        :param resume: Идентификатор резюме для поиска похожих резюме.
        :param filter_exp_industry: Обрабатывается совместно с параметром filter_exp_period.
        Идентификатор отрасли, в которой у соискателя должен присутствовать опыт работы. Получить список отраслей можно
        из метода Directories.get_industry_directory
        :param filter_exp_period: Период, за который у соискателя должен присутствовать
        опыт работы в отрасли, указанной в параметре filter_exp_industry.
        Возможные значения: `all_time`, `last_year`, `last_three_years`, `last_six_years`.
        :param with_job_search_status: Параметр для просмотра в резюме статуса поиска кандидата
        :param education_levels: Требуемый уровень образования соискателя.
        Возможные значения: `secondary`, `special_secondary`, `unfinished_higher`,
        `higher`, `bachelor`, `master`, `candidate`, `doctor`.
        :param district: Идентификатор района.
        :param saved_search_id: Идентификатор сохраненного автопоиска.
        :param search_by_vacancy_id: Идентификатор вакансии, среди откликов на которую необходимо искать резюме
        :param last_used_timestamp:Время последнего просмотра результатов автопоиска в формате временной метки.
        Используется совместно с параметром saved_search_id для поиска и подсчета новых резюме,
        подходящих под запрос и появившихся с момента последнего просмотра.
        :param last_used: Время последнего просмотра результатов автопоиска в формате даты и времени с временной зоной.
        Пример: 2015-11-12T18:06:04+0300.
        :param locale: Default: "RU" Example: locale=EN
        :param host: Default: "hh.ru"
        Enum: "hh.ru" "rabota.by" "hh1.az" "hh.uz" "hh.kz" "headhunter.ge" "headhunter.kg"
    """
    text_logic: str | None = None
    text_field: str | None = None
    text_period: int | None = None
    text_company_size: str | None = None
    age_from: str | None = None
    age_to: str | None = None
    area: str | None = None
    relocation: str | None = None
    date_from: str | None = None
    date_to: str | None = None
    employment: str | None = None
    experience: str | None = None
    skill: str | None = None
    gender: str | None = None
    label: str | None = None
    language: str | None = None
    currency: str | None = None
    salary_from: int | None = None
    salary_to: int | None = None
    schedule: str | None = None
    order_by: str | None = None
    citizenship: str | None = None
    work_ticket: str | None = None
    educational_institution: str | None = None
    search_in_responses: bool = False
    by_text_prefix: bool = False
    driver_license_types: str | None = None
    vacancy_id: str | None = None
    per_page: int = 20
    professional_role: str | None = None
    folder: list[str] | None = None
    include_all_folders: bool = False
    job_search_status: str | None = None
    resume: str | None = None
    filter_exp_industry: str | None = None
    filter_exp_period: str | None = None
    with_job_search_status: str | None = None
    education_levels: str | None = None
    district: str | None = None
    saved_search_id: str | None = None
    search_by_vacancy_id: str | None = None
    last_used_timestamp: str | None = None
    last_used: str | None = None
    locale: str | None = "RU"
    host: str | None = "hh.ru"
