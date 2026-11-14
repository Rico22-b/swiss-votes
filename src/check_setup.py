"""Checks that all libraries of the project can be imported."""
import importlib

LIBRARIES = [
    "pandas", "requests", "matplotlib", "seaborn", "sklearn",
    "statsmodels", "scipy", "geopandas", "sqlalchemy", "psycopg2", "sqlite3",
]

failed = []
for name in LIBRARIES:
    try:
        module = importlib.import_module(name)
        version = getattr(module, "__version__", "ok")
        print(f"{name:<12} {version}")
    except ImportError as error:
        failed.append(name)
        print(f"{name:<12} MISSING ({error})")

print()
print("All libraries available." if not failed else f"Missing: {', '.join(failed)}")
