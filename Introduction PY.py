from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

dane = load_breast_cancer()

# Organizacja danych
nazwy_etykiet = dane['target_names']
etykieta = dane['target']
nazwy_cech = dane['feature_names']
cechy = dane['data']

# Podgląd na dane
print(nazwy_etykiet)
print('Class label = ', etykieta[0])
print(nazwy_cech)
print(cechy[0])

# Dzielenie danych
train, test, train_labels, test_labels = train_test_split(cechy, etykieta, test_size=0.33, random_state=42)

# Inicjalizacja classifier
gnb = GaussianNB()

# Trening classifier
model = gnb.fit(train, train_labels)

# Przewidywanie
preds = gnb.predict(test)

print(preds)

# Ewaluacja
print(accuracy_score(test_labels, preds))