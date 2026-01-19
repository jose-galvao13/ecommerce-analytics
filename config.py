import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_RAW = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROCESSED = os.path.join(BASE_DIR, 'data', 'processed')
DATA_SQL = os.path.join(BASE_DIR, 'data', 'sql')
OUTPUTS_PLOTS = os.path.join(BASE_DIR, 'outputs', 'plots')
OUTPUTS_REPORTS = os.path.join(BASE_DIR, 'outputs', 'reports')

# Criar pastas se não existirem
for path in [DATA_RAW, DATA_PROCESSED, DATA_SQL, OUTPUTS_PLOTS, OUTPUTS_REPORTS]:
    os.makedirs(path, exist_ok=True)

# Database Config
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_password',
    'database': 'ecommerce_analytics'
}

# Análise Config
OUTLIER_THRESHOLD = 3  # IQR multiplier
RFM_QUANTILES = 5
MIN_BASKET_SUPPORT = 10