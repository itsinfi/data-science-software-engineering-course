# from src.preprocessing import preprocessing
# from src.eda import eda
# from src.modeling import modeling
from src.predict import predict
import joblib

def main(vars):
    # eda()
    # df_encoded, df_clean = preprocessing()
    # model = modeling(df_encoded, df_clean)

    # joblib.dump(model, 'model/model.pkl')

    predict(model=joblib.load('model/model.pkl'), vars=vars)

