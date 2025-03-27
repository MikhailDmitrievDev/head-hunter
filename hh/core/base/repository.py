from typing import Generic, TypeVar

E = TypeVar("E")


class Repository(Generic[E]):
    def __init__(self):
        self.entities: list[E] = []

    def add(self, entity: E) -> None:
        self.entities.append(entity)

    def get_all(self) -> list[E]:
        return self.entities

    def find_by_id(self, entity_id: int) -> E | None:
        for entity in self.entities:
            if hasattr(entity, "id") and entity.id == entity_id:
                return entity
        return None
