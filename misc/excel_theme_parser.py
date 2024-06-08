from flask_restful import abort
import pandas as pd
import random
import os

from data.topics import Topic
from data.tasks import Task


def generate_color():
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


def excel_to_db(session, excel_file_path, sheet_name, eng_name, description, eng_description, filename, id_):
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
        eng_name=eng_name,
        description=description,
        eng_description=eng_description,
        photo=filename,
        color=generate_color()
    )
    session.add(theme)
    for i in range(len(df)):
        problem = str(df.iloc[i, 0])
        solution = str(df.iloc[i, 1])
        complexity = int(df.iloc[i, 2])
        task = Task(
            topic_id=id_,
            problem=problem,
            solution=solution,
            complexity=complexity
        )
        session.add(task)
    session.commit()
    os.remove(excel_file_path)
