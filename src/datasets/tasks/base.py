import abc
from typing import Dict

from ..features import Features


class TaskTemplate(abc.ABC):
    task: str
    input_schema: Features
    label_schema: Features

    @property
    def features(self) -> Features:
        return Features(**self.input_schema, **self.label_schema)

    @property
    @abc.abstractmethod
    def column_mapping(self) -> Dict[str, str]:
        return NotImplemented

    @classmethod
    @abc.abstractmethod
    def from_dict(cls, template_dict: dict) -> "TaskTemplate":
        return NotImplemented