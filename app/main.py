class Person:
    people: dict[str, "Person"] = {}  # словарь всех людей

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        self.husband: "Person | None" = None
        self.wife: "Person | None" = None
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age})"


def create_person_list(people_data: list[dict]) -> list[Person]:
    # создаём всех людей
    [Person(person["name"], person["age"]) for person in people_data]

    # связываем пары
    for person in people_data:
        current_person = Person.people[person["name"]]
        if "husband" in person and person["husband"]:
            current_person.husband = Person.people.get(person["husband"])
        if "wife" in person and person["wife"]:
            current_person.wife = Person.people.get(person["wife"])

    return list(Person.people.values
