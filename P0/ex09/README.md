# ft_package

Petit package Python qui compte le nombre d'occurrences d'un élément dans une liste.

## Installation

Depuis le dossier `ex09/`, construire le package :

```bash
python3 -m pip install --user build
python3 -m build
```

Puis installer l'un des deux fichiers générés dans `dist/` :

```bash
pip install ./dist/ft_package-0.0.1.tar.gz
# ou
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

Vérifier l'installation :

```bash
pip list                  # ft_package apparaît dans la liste
pip show -v ft_package    # affiche ses caractéristiques
```

## Utilisation

```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # 0
```

`count_in_list(lst, value)` renvoie le nombre de fois où `value` apparaît dans `lst`.

## Licence

MIT. Voir le fichier `LICENSE`.

---

# Notes d'apprentissage

## Définitions

- **Un module** : un fichier `.py` standard.
- **Un package** : un dossier qui regroupe des modules et contient un fichier `__init__.py`.

`__init__.py` indique à Python : « ce dossier est un package, on peut l'importer ».
Son code s'exécute au moment de `import ft_package`. C'est lui qui rend les fonctions
accessibles directement depuis le package.

### L'import relatif dans `__init__.py`

```python
from .count_in_list import count_in_list
```

- Le `.` signifie « le package courant », comme `./` dans un chemin de terminal.
- Sans le point, Python chercherait un module `count_in_list` au niveau général
  (comme `sys` ou `os`) et ne le trouverait pas une fois le package installé :
  `ModuleNotFoundError`.
- Cette ligne fait le pont : on peut écrire `from ft_package import count_in_list`
  au lieu de `from ft_package.count_in_list import count_in_list`.

## Structure du projet

```
ex09/
├── pyproject.toml       ← la carte d'identité du package
├── README.md            ← ce fichier
├── LICENSE              ← texte de la licence MIT
└── ft_package/          ← le package lui-même
    ├── __init__.py
    └── count_in_list.py
```

## pyproject.toml

Ce fichier comprend deux parties distinctes :

1. `[build-system]` : l'outil qui fabrique le package (hatchling, setuptools, flit…).
   Ils font tous la même chose : il suffit d'en choisir un.
2. `[project]` : la carte d'identité du package. Les informations déclarées ici sont
   celles qu'affiche `pip show`.

| Ligne de `pip show` | À déclarer dans `pyproject.toml` |
|---|---|
| `Name` | `name` dans `[project]` |
| `Version` | `version` dans `[project]` (0.0.1) |
| `Summary` | `description` dans `[project]` (les noms diffèrent) |
| `Author-email` | `authors` dans `[project]` (nom et email) |
| `License-Expression` | `license` dans `[project]` (`"MIT"`) |
| `Home-page` | `Homepage` dans la section `[project.urls]` |

- Seuls `name` et `version` sont obligatoires. Le reste est facultatif : `pip show`
  affiche ce qui est déclaré et laisse vide le reste (`Requires`, `Classifiers`…).
- `requires-python = ">=3.8"` déclare que le package demande Python 3.
  Sans ce champ, hatchling suppose une compatibilité Python 2 et 3, et la wheel
  s'appelle `py2.py3` au lieu de `py3`.

### Deux noms distincts

- Le `name` dans `pyproject.toml` est celui que connaît **pip**
  (`pip show ft_package`, `pip uninstall ft_package`).
- Le nom du dossier est celui que connaît **Python** (`from ft_package import ...`).

Ces deux noms auraient pu être différents. Exemple réel : on installe
`pip install scikit-learn`, mais on importe `import sklearn`.

### Différences avec la sortie de l'énoncé

L'énoncé a été écrit avec des outils plus anciens. Avec les versions actuelles :

- `Metadata-Version` vaut 2.5 au lieu de 2.1 : la norme des métadonnées a évolué.
- La licence s'affiche sur la ligne `License-Expression` au lieu de `License`,
  car elle est déclarée sous forme de nom standard (`"MIT"`).
- Quand un auteur a un nom et un email dans le même dictionnaire, ils sont regroupés
  sur la ligne `Author-email` (`Camansou <...>`), et `Author` reste vide.
- La homepage apparaît deux fois avec `pip show -v` : c'est la même URL, recopiée
  dans l'ancien champ `Home-page` et listée dans `Project-URLs`.

## Licence MIT

L'une des licences les plus permissives : tout le monde a le droit d'utiliser, de modifier
et de redistribuer le code, à condition de garder le nom de l'auteur et le texte de la licence.
Le code est fourni « tel quel », sans garantie.

- Dans `pyproject.toml` : `license = "MIT"` et `license-files = ["LICENSE"]`.
- Le fichier `LICENSE` contient le texte complet de la licence (seule la ligne
  `Copyright` est personnalisée).

## La construction

`python3 -m build` lit le `pyproject.toml` et fabrique dans `dist/` :

- **`.tar.gz` (sdist)** : une archive des sources. Pour l'installer, pip doit encore
  la « construire ».
- **`.whl` (wheel)** : le package déjà construit, prêt à être copié tel quel.
  C'est plus rapide.

Le nom de la wheel se lit en morceaux :
`ft_package-0.0.1-py3-none-any.whl` = nom, version, Python 3, pas de code compilé,
n'importe quel système.

`build` télécharge lui-même l'outil déclaré dans `[build-system]` (hatchling) :
pas besoin de l'installer à la main.

## L'installation : où va le package ?

`pip install` copie le package dans un dossier spécial de Python : **site-packages**.
Python cherche les imports dans ce dossier, on peut donc ensuite l'importer de partout.
La ligne `Location` de `pip show` indique ce dossier.

`pip show` lit le package **installé**, pas le dossier `dist/`. Reconstruire ne
suffit pas : il faut réinstaller pour voir les changements.

### Après une modification du `pyproject.toml`

Depuis le dossier `ex09/` :

```bash
rm -rf dist                  # supprimer l'ancienne version
python3 -m build             # reconstruire
pip uninstall ft_package     # désinstaller l'ancienne version
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```

On installe **l'un ou l'autre** fichier, pas les deux à la suite : le second
`pip install` répondrait « déjà installé ». Pour tester les deux, désinstaller entre les deux.
Sans `pip uninstall`, pip peut aussi ignorer la nouvelle version, car le numéro (0.0.1)
n'a pas changé.

### Pourquoi tester hors de `ex09/`

Dans `ex09/`, Python trouve le dossier `ft_package/` local : l'import marcherait même si
le package n'était pas installé. Depuis un autre dossier (`cd ~`), Python est obligé
d'utiliser la version installée. C'est le seul moyen de vérifier que l'installation fonctionne.

## Documentation

- [Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
