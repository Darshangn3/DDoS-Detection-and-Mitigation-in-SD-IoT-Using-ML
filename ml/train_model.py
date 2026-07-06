import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# ==============================
# LOAD DATA
# ==============================
df = pd.read_csv("dataset.csv")

print("Columns found:", df.columns.tolist())

# ==============================
# SELECT FEATURES (SAFE)
# ==============================
FEATURE_COLUMNS = [
    "pkt_count",
    "byte_count",
    "duration",
    "pkt_rate",
    "syn_count"
]

# Ensure all required columns exist
for col in FEATURE_COLUMNS:
    if col not in df.columns:
        raise ValueError(f"Missing required column: {col}")

X = df[FEATURE_COLUMNS]
y = df["label"]

# ==============================
# FORCE NUMERIC
# ==============================
X = X.apply(pd.to_numeric, errors="coerce")
X = X.fillna(0)

# ==============================
# TRAIN / TEST SPLIT
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

# ==============================
# TRAIN RANDOM FOREST
# ==============================
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

# ==============================
# EVALUATION
# ==============================
y_pred = model.predict(X_test)
print("\n=== CLASSIFICATION REPORT ===")
print(classification_report(y_test, y_pred))

# ==============================
# SAVE MODEL
# ==============================
joblib.dump(model, "ddos_model.pkl")
print("\n Model saved as ddos_model.pkl")
