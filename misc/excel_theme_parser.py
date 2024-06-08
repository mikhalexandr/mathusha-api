import pandas as pd

from data import db_session
from data.topics import Topic
from data.tasks import Task


def excel_to_db(excel_file_path, sheet_name):
    session = db_session.create_session()
    df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    theme = Topic(
        name=sheet_name,
        photo=str(df.iloc[0, 3]),
        description=str(df.iloc[1, 3])
    )
    session.add(theme)
    for i in range(len(df)):
        problem = str(df.iloc[i, 0])
        solution = str(df.iloc[i, 1])
        complexity = int(df.iloc[i, 2])
        task = Task(
            topic_id=sheet_name,
            problem=problem,
            solution=solution,
            complexity=complexity
        )
        session.add(task)
    session.commit()
