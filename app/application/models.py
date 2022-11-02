import datetime
from app.application import database, app
from typing import Any


class TodoModel(database.Model):
    __tablename__ = 'todo'

    id = database.Column(database.Integer(), primary_key=True)
    task = database.Column(database.String(length=1000), nullable=False)

    def __repr__(self) -> str:
        return f"{self.task}"

    @staticmethod
    def create_table() -> None:
        database.create_all()

    @staticmethod
    def insert_task(**kwargs) -> None:
        item = TodoModel(task=kwargs['task'])
        database.session.add(item)
        database.session.commit()

    @staticmethod
    def select_all_tasks() -> Any:
        for tsk in database.session.query(TodoModel).all():
            yield tsk

    @staticmethod
    def remove_task(_id: int) -> None:
        database.session.execute(f"DELETE FROM todo WHERE id = {_id};")
        database.session.commit()


if __name__ == '__main__':
    with app.app_context():
        #TodoModel.create_table()
        for n in TodoModel.select_all_tasks():
            print(n)
