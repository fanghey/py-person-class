class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"

    @staticmethod
    def create_person_list(people: list) -> list:
        person_list = []

        for item in people:
            if isinstance(item, tuple):
                name, age = item
                person = Person(name, age)
                person_list.append(person)
            elif isinstance(item, str):
                person = Person(item, 0)
                person_list.append(person)

        return person_list
