from typing import Optional


class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.husband: Optional["Person"] = None
        self.wife: Optional["Person"] = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(people: list[dict]) -> list[Person]:
    # создаём людей (list comprehension)
    persons = [Person(p["name"], p["age"]) for p in people]

    # связываем husband / wife (тоже через list comprehension)
    [
        (
            setattr(Person.people[p["name"]], "husband", Person.people.get(p["husband"]))
            if p.get("husband")
            else None,
            setattr(Person.people[p["name"]], "wife", Person.people.get(p["wife"]))
            if p.get("wife")
            else None,
        )
        for p in people
    ]

    return persons
