# debug_imports.py
import sys

print("sys.path:")
for p in sys.path[:5]:
    print(" ", p)

print("\nTrying imports...")

try:
    import app.database

    print("✅ import app.database OK")
    print("Base from app.database ->", getattr(app.database, "Base", None))
except Exception as e:
    print("❌ app.database import error:", e)

try:
    import app.models

    print("✅ import app.models OK")
    print("User class mro ->", app.models.User.__mro__)
except Exception as e:
    print("❌ app.models import error:", e)
