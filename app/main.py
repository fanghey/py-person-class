class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(data["name"], data["age"])
              for data in people]

    for per, human in enumerate(people):
        full = {person.name: person for person in result}
        if "wife" in human and human["wife"] is not None:
            result[per].wife = full[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            result[per].husband = full[human["husband"]]

    return result
