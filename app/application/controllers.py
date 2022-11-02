import random
from typing import Any
from app.application.models import TodoModel


class Controller:
    todo_instance: TodoModel = TodoModel()

    def insert(self, data: Any) -> None:
        self.todo_instance.insert_task(task=data)

    def remove(self, _id: int) -> None:
        self.todo_instance.remove_task(_id)

    def select(self):
        return self.todo_instance.select_all_tasks()

    def random_phrases(self):
        phrases = [
            "A riqueza não consiste em ter grandes posses, mas em ter poucas necessidades.",
            "Você tem poder sobre sua mente – não sobre eventos externos. Perceba isso e você encontrará a sua força.",
            "Sorte é o que acontece quando a preparação encontra a oportunidade",
            "Todos nós podemos errar, mas a perseverança no erro é a verdadeira loucura",
            "A felicidade de sua vida depende da qualidade de seus pensamentos",
            "Quem não se contenta com pouco, não se contenta com nada.",
            "O amigo é um segundo eu",
            "As dificuldades fortalecem a mente, assim como o trabalho o faz com o corpo",
            "Pense na beleza da vida. Observe as estrelas e veja-se correndo com elas."]
        return random.choice(phrases)
