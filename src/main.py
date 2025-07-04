from src.preprocessing import preprocessing
from src.eda import eda
from src.modeling import modeling

def main():
    eda()
    df_encoded, df_clean = preprocessing()
    modeling(df_encoded, df_clean)