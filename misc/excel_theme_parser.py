import pandas as pd

from data import db_session
from data.themes import Theme
from data.themes_expressions import ThemeExpression


def excel_to_db(excel_file_path):
    session = db_session.create_session()
    excelFile = pd.ExcelFile(excel_file_path)
    for sheet_name in excelFile.sheet_names:
        df = pd.read_excel(excel_file_path, sheet_name=sheet_name)
        theme = Theme(
            name=sheet_name,
            image=str(df.iloc[0, 2]),
            description=str(df.iloc[1, 2])
        )
        session.add(theme)
        for i in range(len(df)):
            problem = str(df.iloc[i, 0])
            solution = str(df.iloc[i, 1])
            expression = ThemeExpression(
                theme_id=sheet_name,
                problem=problem,
                solution=solution
            )
            session.add(expression)
    session.commit()
