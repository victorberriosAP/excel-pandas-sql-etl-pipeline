## Exportar desde db a excel
import pandas as pd
import sqlite3

path_db = r'D:\Usuario Windows\Escritorio\ETL GibHub\04_sql_layer\mi_base.db'
path_result = r'D:\Usuario Windows\Escritorio\ETL GibHub\06_result_excel\resultado_final.xlsx'

# Read final result table from SQLite database
with sqlite3.connect(path_db) as conn:
    df_result = pd.read_sql("SELECT * FROM result", conn)

# Export DataFrame to Excel file (without index column)
df_result.to_excel(path_result, index=False)