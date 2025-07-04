import numpy as np

def modeling(df_encoded, df_clean):
    from sklearn.tree import DecisionTreeRegressor
    #from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree

    y = df_clean.price_group
    features = ['model', 'year', 'transmission', 'mileage', 'fuelType']
    X = df_encoded[features]

    model = DecisionTreeRegressor(max_leaf_nodes=32, random_state=1)
    model.fit(X, y)

    model.predict(X)

    model.score(X, y)

    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 8))
    plot_tree(model, filled=True, feature_names=features , class_names=df_clean.price_group)
    #plot_tree(model, filled=True, feature_names=features, class_names=df_clean.price)
    plt.title("Decision tree trained on used car features")
    plt.savefig('data/Decision tree trained on used car features.png')

    df_encoded.describe().T

    df_clean.describe().T

    print("Making predictions for the following 5 cars:")
    print(X.head())
    print("The predictions are")
    print(model.predict(X.head()))

    from sklearn.tree import DecisionTreeRegressor
    #from sklearn.tree import DecisionTreeClassifier
    from sklearn import tree

    y = df_clean.price
    features = ['model', 'year', 'transmission', 'mileage', 'fuelType']
    X = df_encoded[features]

    model = DecisionTreeRegressor(max_leaf_nodes=32, random_state=1)
    model.fit(X, y)

    model.predict(X)

    model.score(X, y)

    from sklearn.tree import plot_tree
    import matplotlib.pyplot as plt

    plt.figure(figsize=(12, 8))
    plot_tree(model, filled=True, feature_names=features , class_names=df_clean.price)
    #plot_tree(model, filled=True, feature_names=features, class_names=df_clean.price)
    plt.title("Decision tree trained on used car features")
    plt.savefig('Decision tree trained on used car features.png')

    print("Making predictions for the following 5 cars:")
    print(X.head())
    print("The predictions are")
    print(model.predict(X.head()))

    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score, classification_report

    # Load the dataset

    features = ['fuelType', 'model', 'year']#['model', 'year', 'transmission', 'mileage', 'fuelType']
    X = df_encoded[features]
    y = df_clean.price

    # Split into train and test sets (80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train the model
    clf = DecisionTreeClassifier(max_depth=10, random_state=42)
    clf.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = clf.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)

    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    # Evaluation
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, y_pred)

    # Ergebnisse anzeigen
    print(f"📊 MAE:  {mae:.2f}")
    print(f"📉 MSE:  {mse:.2f}")
    print(f"📉 RMSE: {rmse:.2f}")
    print(f"🧮 R²:   {r2:.2f}")

    import matplotlib.pyplot as plt

    # Streudiagramm erstellen
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.6, edgecolors="k")
    plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], 'r--', lw=2, label='Ideal')  # Linie y = x
    plt.xlabel("Echter Wert")
    plt.ylabel("Vorhergesagt")
    plt.title("Streudiagramm: Echte vs. Vorhergesagte Werte")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('data/Streudiagramm Echte vs. Vorhergesagte Werte.png')

    return model

