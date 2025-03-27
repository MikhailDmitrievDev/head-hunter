from typing import TypeVar, Generic

R = TypeVar("R", bound="Repository")


class Controller(Generic[R]):

    def __init__(self, repository: R):
        self.repository = repository
