import pandas as pd

from data import db_session
from data.topics import Theme
from data.topic_expressions import ThemeExpression


def excel_to_db(excel_file_path):
    session = db_session.create_session()
    excelFile = pd.ExcelFile(excel_file_path)
    for sheet_name in excelFile.sheet_names:
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        theme = Theme(
            name=sheet_name,
            image=str(df.iloc[0, 3]),
            description=str(df.iloc[1, 3])
        )
        session.add(theme)
        for i in range(len(df)):
            problem = str(df.iloc[i, 0])
            solution = str(df.iloc[i, 1])
            complexity = int(df.iloc[i, 2])
            expression = ThemeExpression(
                theme_id=sheet_name,
                problem=problem,
                solution=solution,
                complexity=complexity
            )
            session.add(expression)
    session.commit()
