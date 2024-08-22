from dataclasses import dataclass

@dataclass
class PlayerCharacter:
    name: str
    system: str
    attributes: dict
    class_obj: Any = None

    def from_dict(self, data):
        return self(name=data.get('name', None),
                    system=data.get('system', None),
                    attributes=data.get('attributes', None),
                    class_obj=data.get('class_obj', None)
                    )

    def to_dict(self):
        return {
            'name': self.name,
            'system': self.system,
            'attributes': self.attributes,
            'class_obj': self.class_obj
        }


    def __str__(self):
        return f'{self.name} ({self.system})'


    def __repr__(self):
        return f'PlayerCharacter({self.name}, {self.system}, {self.attributes})'


    def __post_init__(self):
        match self.system:
            case 'dnd5e':
                self.class_obj = DnD5eCharacter(self.attributes)
            case _:
                raise ValueError(f'Unsupported system: {self.system}')
