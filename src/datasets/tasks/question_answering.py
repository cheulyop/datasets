from dataclasses import dataclass
from typing import Dict

from ..features import Features, Sequence, Value
from .base import TaskTemplate


@dataclass
class QuestionAnswering(TaskTemplate):
    task = "question-answering"
    input_schema = Features({"question": Value("string"), "context": Value("string")})
    label_schema = Features(
        {
            "answers": Sequence(
                {
                    "text": Value("string"),
                    "answer_start": Value("int32"),
                }
            )
        }
    )
    question_column: str
    context_column: str
    answers_column: str

    def __init__(self, question_column="question", context_column="context", answers_column="answers"):
        self.question_column = question_column
        self.context_column = context_column
        self.answers_column = answers_column

    @property
    def column_mapping(self) -> Dict[str, str]:
        return {self.question_column: "question", self.context_column: "context", self.answers_column: "answers"}

    @classmethod
    def from_dict(cls, template_dict: dict) -> "QuestionAnswering":
        return cls(
            question_column=template_dict["question_column"],
            context_column=template_dict["context_column"],
            answers_column=template_dict["answers_column"],
        )

    def __hash__(self):
        return hash((self.task, self.question_column, self.context_column, self.answers_column))