from flask_restful import abort
import pandas as pd
import os

from data.topics import Topic
from data.tasks import Task


def excel_to_db(session, excel_file_path, sheet_name, description, filename):
    if filename is None:
        abort(404, message="File not found")
    df = None
    try:
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
    except Exception as e:
        print("Error: ", e)
        abort(404, message=f"Excel file [{filename}] is not found")
    theme = Topic(
        name=sheet_name,
        description=description,
        photo=filename
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
    os.remove(excel_file_path)
