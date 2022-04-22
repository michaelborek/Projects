import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn import datasets
from sklearn import svm

irys = datasets.load_iris()

# Podziel dane o tęczówce oka na zestawy danych szkoleniowych i testowych, z których 40% jest przeznaczone do testowania.
X_trenuj, X_test, y_trenuj, y_test = train_test_split(irys.data, irys.target, test_size=0.4, random_state=0)

# Zbuduj model SVC do przewidywania klasyfikacji tęczówki oka na podstawie danych szkoleniowych
clf = svm.SVC(kernel='linear', C=1).fit(X_trenuj, y_trenuj)

# Teraz zmierz jego wydajność na podstawie danych testowych
clf.score(X_test, y_test)

# Podajemy cross_val_score model, cały zbiór danych i jego "prawdziwe" wartości oraz liczbę złożeń:
scores = cross_val_score(clf, irys.data, irys.target, cv=5)

# Wydrukuj dokładność dla każdego zagięcia:
print(scores)

# I średnią dokładność wszystkich 5 złożeń:
print(scores.mean())

clf = svm.SVC(kernel='poly', C=1)
wynik = cross_val_score(clf, irys.data, irys.target, cv=5)
print(wynik)
print(wynik.mean())

# Zbuduj model SVC do przewidywania klasyfikacji tęczówki oka na podstawie danych szkoleniowych
clf = svm.SVC(kernel='poly', C=1).fit(X_trenuj, y_trenuj)

# Teraz zmierz jego wydajność na podstawie danych testowych
clf.score(X_test, y_test)
