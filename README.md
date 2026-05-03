Evolución de un proceso manual en Excel hacia un pipeline ETL automatizado en Python. 
Los datos pasan desde archivos Excel a un flujo estructurado con Pandas, 
se almacenan en SQLite y se exportan de forma reproducible, 
reduciendo manipulación manual y errores.

--1. Etapa inicial: Excel manual

En la primera versión del flujo, el tratamiento de datos se realizaba directamente en 
Excel utilizando filtros, fórmulas y funciones como BUSCARX.

Manipulación directa del archivo exportado desde el WMS
Limpieza y filtrado manual en hojas de cálculo
Generación del resultado final sin automatización

Este enfoque funcionaba, pero dependía completamente de intervención humana, 
lo que lo hacía poco escalable y difícil de mantener.

--2. Transición: ETL híbrido (Excel + Python + SQL)

En una segunda etapa, se incorporó Python para automatizar parte del procesamiento, 
manteniendo como entrada una hoja previamente filtrada en Excel.

Uso de pandas para transformación ligera
Introducción de SQLite como capa intermedia
SQL para reglas de negocio y agrupaciones
Exportación automatizada a Excel

Aquí comienza la separación entre preparación de datos y lógica de negocio.

--3. Estado actual: ETL automatizado desde origen (WMS)

La versión más actual elimina la dependencia del Excel preprocesado y 
trabaja directamente sobre el archivo original del sistema.

Ingesta desde datos crudos del WMS
Limpieza y normalización en pandas
Transformación y reglas de negocio en SQL
Generación de dataset final reproducible

Este enfoque permite trazabilidad completa y elimina pasos manuales en la cadena de procesamiento.

--4. Capa de exportación desacoplada

Finalmente, la exportación se mantiene como un proceso independiente:

Lectura del resultado desde SQLite
Exportación a Excel para consumo en herramientas externas (ej. Power Automate Desktop)
Sin lógica adicional en esta capa

Esto permite separar claramente:

procesamiento de datos
y consumo de información
