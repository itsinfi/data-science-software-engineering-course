import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def preprocessing():
    # Import Data sets
    df = pd.read_csv('data/toyota.csv')

    df.isnull().sum()

    # how many total missing values do we have?
    total_cells = np.prod(df.shape)
    total_missing = df.isnull().sum()

    # percent of data that is missing
    percent_missing = (total_missing/total_cells) * 100
    print(percent_missing)

    df.dropna()

    columns_with_na_dropped = df.dropna(axis=1)
    columns_with_na_dropped.head()

    # just how much data did we lose?
    print("Columns in original dataset: %d \n" % df.shape[1])
    print("Columns with na's dropped: %d" % columns_with_na_dropped.shape[1])

    df.fillna(0)

    df.duplicated().sum()

    # Duplikate anzeigen (alle Spalten vergleichen)
    duplikate = df[df.duplicated()]
    print("Einfache Duplikate:")
    print(duplikate)

    # Duplikate inklusive des ersten Auftretens anzeigen
    duplikate_mit_erstem = df[df.duplicated(keep=False)]
    print("\nAlle Duplikate (inkl. erstes Vorkommen):")
    print(duplikate_mit_erstem)

    df_cleaned = df.drop_duplicates()

    df.isnull().sum()

    df.duplicated().sum()

    df_cleaned = df.drop_duplicates()

    df_cleaned.duplicated().sum()

    plt.figure(figsize=(10,8))
    sns.boxplot(data=df_cleaned,orient='h')
    plt.savefig('Alle Duplikate.png')

    # Nur numerische Spalten auswählen
    num_cols = df.select_dtypes(include='number').columns

    # Kopie für Bereinigung
    df_clean = df.copy()

    # Zeilen-Indexe mit Ausreißern sammeln
    for col in num_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter anwenden – nur Werte innerhalb der Grenzen behalten
        df_clean = df_clean[(df_clean[col] >= lower_bound) & (df_clean[col] <= upper_bound)]

    print(df_clean)

    plt.figure(figsize=(10,8))
    sns.boxplot(data=df_clean,orient='h')
    plt.savefig('eh.png')

    from sklearn.preprocessing import LabelEncoder
    le = LabelEncoder()

    col=['model','transmission','fuelType']
    df_clean[col]=df_clean[col].apply(le.fit_transform)
    df_clean.head(n=5)

    #df['price_group'] = pd.qcut(df['price'], q=3, labels=['jung', 'mittel', 'alt'])
    df_clean['price_group'] = pd.qcut(df_clean['price'], q=3, labels=[1, 2, 3])

    print (df_clean['price_group'])

    df_clean.price_group.describe()

    df_encoded = pd.get_dummies(df_clean[['model', 'year', 'transmission', 'mileage', 'fuelType']])

    print(df_encoded)

    df_encoded.info()

    return df_encoded, df_clean
