import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def eda():
    uc = pd.read_csv('data/toyota.csv')

    print(uc.head())
    print(uc.info())
    print(uc.columns)
    print(uc.describe())
    # print(uc.shape())

    # skalenniveau_bestimmen(uc)

    print(uc.isnull().sum())

    # Beispiel anwenden
    print('model', skalenniveau_bestimmen(uc['model']))  # Nominal
    print('year', skalenniveau_bestimmen(uc['year']))  # Verhältnisskala
    print('price', skalenniveau_bestimmen(uc['price']))  # Ordinal
    print('transmission', skalenniveau_bestimmen(uc['transmission']))  # Verhältnisskala
    print('mileage', skalenniveau_bestimmen(uc['mileage']))  # Verhältnisskala
    print('fuelType', skalenniveau_bestimmen(uc['fuelType']))  # Verhältnisskala
    print('tax', skalenniveau_bestimmen(uc['tax']))  # Verhältnisskala
    print('mpg', skalenniveau_bestimmen(uc['mpg']))  # Verhältnisskala
    print('engineSize', skalenniveau_bestimmen(uc['engineSize']))  # Verhältnisskala

    uc["engineSize"]=uc["engineSize"].replace(0,np.nan)
    uc["tax"]=uc["tax"].replace(0,np.nan)
    uc.dropna( inplace = True)
    uc.duplicated().sum()
    uc.drop_duplicates(inplace=True)


    plt.figure(figsize=(12, 6))
    sns.barplot(x='model', y='price', data=uc[:10000], errorbar=None)
    plt.title('Average Price by Model')
    plt.xlabel('Model')
    plt.ylabel('Average Price')
    plt.xticks(rotation=90)  
    plt.savefig('data/Average Price by Model.png')

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='price', y='transmission', data=uc[:1000],orient='h')
    plt.title('Box Plot of Price by Transmission Type')
    plt.xlabel('Transmission')
    plt.ylabel('Price')
    plt.xticks(rotation=90) 
    plt.savefig('data/Box Plot of Price by Transmission Type.png')

    plt.figure(figsize=(10, 6))
    sns.countplot(x='fuelType', data=uc)
    plt.title('Count of Cars by FuelType')
    plt.xlabel('FuelType')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.savefig('data/Count of Cars by FuelType.png')

    uc.columns

    plt.figure(figsize=(10, 6))
    sns.countplot(x='transmission', data=uc)
    plt.title('Count of Cars by Transmission Type')
    plt.xlabel('Transmission')
    plt.ylabel('Count')
    plt.xticks(rotation=90)
    plt.savefig('data/Count of Cars by Transmission Type.png')

    # Streudiagramm mit seaborn erstellen
    sns.scatterplot(data=uc, x='model', y='price', color='skyblue')

    # Titel hinzufügen
    plt.title('Streudiagramm: model vs. price')

    # Diagramm anzeigen
    plt.savefig('data/Streudiagramm model vs. price.png')

    # Boxplot erstellen mit hue anstelle von palette
    sns.boxplot(x='model', y='price', data=uc, hue='model', palette='Set2', legend=False)

    # Titel hinzufügen
    plt.title('Preis nach Modell')

    # Diagramm anzeigen
    plt.savefig('data/Preis nach Modell.png')

    # Histogramm estellen

    uc['price'].plot(kind='hist', bins=5, color='skyblue', edgecolor='black')

    # Titel und Achsenbezeichner hinzufügen
    plt.title('Verteilung des Preises')
    plt.xlabel('Price')
    plt.ylabel('Häufigkeit')

    # Diagramm anzeigen
    plt.savefig('data/Verteilung des Preises.png')

    # Korrelationsmatrix für price und mileage berechnen
    correlation_matrix = uc[['price', 'mileage']].corr()

    # Heatmap der Korrelationsmatrix erstellen
    plt.figure(figsize=(6, 5))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)

    # Titel hinzufügen
    plt.title('Korrelationsmatrix: Preis vs. Kilometerstand')

    # Diagramm anzeigen
    plt.savefig('data/Korrelationsmatrix - Preis vs. Kilometerstand.png')

    # Pairplot für price und mileage
    sns.pairplot(uc[['price', 'mileage', 'tax']])

    # Diagramm anzeigen
    plt.savefig('data/Pairplot für price und mileage.png')

    fig =  plt.figure(figsize = (15,6))
    fig.patch.set_facecolor('#f5f6f6')


                                                    
    gs = fig.add_gridspec(2,3)
    gs.update(wspace=0.2,hspace= 0.2)

    ax0 = fig.add_subplot(gs[0,0])
    ax1 = fig.add_subplot(gs[0,1])
    ax2 = fig.add_subplot(gs[0,2])
    ax3 = fig.add_subplot(gs[1,0])
    ax4 = fig.add_subplot(gs[1,1])
    ax5 = fig.add_subplot(gs[1,2])

    axes=[ax0,ax1,ax2,ax3,ax4,ax5]
    for ax in axes:
        ax.set_facecolor('#f5f6f6')
        ax.tick_params(axis='x',
                    labelsize = 12, which = 'major',
                    direction = 'out',pad = 2,
                    length = 1.5)
        ax.tick_params(axis='y', colors= 'black')
        ax.axes.get_yaxis().set_visible(False)
        
        for loc in ['left', 'right', 'top', 'bottom']:
            ax.spines[loc].set_visible(False)


            
    cols = uc.select_dtypes(exclude = 'object').columns

    sns.kdeplot(x = uc[cols[0]],color="green",fill=True,ax = ax0)
    sns.kdeplot(x = uc[cols[1]],color="red",fill=True,ax = ax1)
    sns.kdeplot(x = uc[cols[2]],color="blue",fill=True,ax = ax2)
    sns.kdeplot(x = uc[cols[3]],color="black",fill=True,ax = ax3)
    sns.kdeplot(x = uc[cols[4]],color="pink",fill=True,ax = ax4)
    sns.kdeplot(x = uc[cols[5]],color="green",fill=True,ax = ax5)

    fig.text(0.2,0.98,"Univariate Analysis on Numerical Columns:",**{'font':'serif', 'size':18,'weight':'bold'}, alpha = 1)
    fig.text(0.1,0.90,"  As we can see there is so much otliers present in the numerical columns:",**{'font':'serif', 'size':12,'weight':'bold'}, alpha = 1)
    fig.savefig('data/Univariate Analysis on Numerical Columns.png')

def skalenniveau_bestimmen(uc):
    if uc.dtype == 'object':  # Kategorische Daten
        # Falls es nur wenige eindeutige Werte gibt, könnte es Nominal oder Ordinal sein.
        unique_values = uc.nunique()
        if unique_values <= 10:
            return "Nominal (kategorisch)"
        else:
            return "Ordinal (Reihenfolge vorhanden)"
    
    elif pd.api.types.is_numeric_dtype(uc):
        if (uc.min() == 0) and (uc.max() > 0):  # Echte Null vorhanden (Verhältnisskala)
            return "Verhältnisskala"
        else:  # Intervalldaten
            return "Intervallskala"
    
    return "Unklar"