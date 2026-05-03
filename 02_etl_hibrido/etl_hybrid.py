## caso_2
import pandas as pd
import sqlite3

path_db = r'D:\Usuario Windows\Escritorio\ETL GibHub\04_sql_layer\mi_base.db'

# 1. Extract
df = pd.read_excel(
    'Matriz ID.xlsx',
    sheet_name='Filtrar',
    dtype=str,
    usecols='B:L'
)

# 2. Transform
df['Fecha'] = df['Fecha'].astype(str).str[:10]
df = df[df['oe_N2'] != 'ISO']
df = df[df['ID'].isna()]

# 3. Load staging
conn = sqlite3.connect(path_db)
df.to_sql('ordenes', conn, if_exists='replace', index=False)

# 4. Transform in SQL (final dataset)
query = """
SELECT Fecha, 
    Propietario,
    oe_N1 AS Destino_final, 
    Tipo, 
    n_orden AS ArrayOrdenes
FROM ordenes
WHERE Propietario = '0313'

UNION ALL

SELECT Fecha, 
    Propietario, 
    oe_N2 AS Destino_final, 
    Tipo,
    GROUP_CONCAT(n_orden, ' o ') AS ArrayOrdenes
FROM ordenes
WHERE Propietario <> '0313'
GROUP BY oe_N2, Propietario, Tipo
"""

with sqlite3.connect(path_db) as conn:

    df_result = pd.read_sql(query, conn)

    df_result.to_sql('result', conn, if_exists='replace', index=False)
