# Archivo: etl/pipeline.py

"""Mini pipelien ETL: CSV --> limpieza --> postgreSQL"""

import csv
imposr psycopg2
from datetime import datetime
import time
import os