## caso_3
import pandas as pd
import sqlite3

path_db = r'D:\Usuario Windows\Escritorio\ETL GibHub\04_sql_layer\mi_base.db'

# 1. Extract
df_0 = pd.read_excel('raw_wms_data.xlsx',
                   sheet_name='Data',
                   skiprows=1,
                   dtype=str,
                   usecols='C:AI'  # Select a trimmed column range
                   )

# Load only required columns
df = df_0[[
    'Fecha de expedición solicitada',
    'Nº orden', 
    'Propietario', 
    'Tipo',
    'Orden externa Nº1', 
    'Orden externa Nº2',
    'Número de carga'
]]

# Rename columns
df = df.rename(columns={
    'Nº orden': 'n_orden',
    'Orden externa Nº1': 'oe_N1',
    'Fecha de expedición solicitada': 'Fecha',
    'Orden externa Nº2': 'oe_N2',
    'Número de carga': 'ID'
})

# Additional cleaning
df['Fecha'] = df['Fecha'].astype(str).str[:10]  # Trim time part
df = df[df['oe_N2'] != 'ISO']                   # Remove ISO records
df = df[df['ID'].isna()]                        # Filter rows without ID


#== SQL processing section ==

with sqlite3.connect(path_db) as conn:

    # staging table
    df.to_sql('ordenes', conn, if_exists='replace', index=False)

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

    df_result = pd.read_sql(query, conn)

    # final table
    df_result.to_sql('result', conn, if_exists='replace', index=False)