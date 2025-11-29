# 🧠 Lessons Learned – Baseline Pipeline Debugging (Wide-Feature Kaggle Dataset)

This document summarizes the key issues encountered and the insights gained while building the baseline model for the *Kaggle Reversal Points in US Equities* competition. The dataset’s unusual structure (68k+ columns, only ~2k rows) and the fast-moving notebook exploration revealed several important lessons about data validation, dimensionality reduction, and model configuration.

## 🚨 1. A Single Dirty Label Caused the Entire Pipeline to Collapse

### Root Cause
The `class_label` target column contained an unexpected value:

```
[None, 'HL', 'HH', 'LH', 'LL']
```

That `None` value forced:

- `LabelEncoder` to create **five classes**, not four  
- LightGBM to treat the problem as **regression** instead of multiclass  
- The model to output floats that were silently cast to integers  
- Predictions collapsing into a constant `4`  
- `inverse_transform()` returning `<null>`  
- Submission CSV being invalid  
- Debugging steps becoming extremely confusing  

### Lesson
👉 **Always validate the target column BEFORE encoding it.**

Suggested check:

```python
print(train_df['class_label'].unique())
print(train_df['class_label'].isna().sum())
```

---

## 🚨 2. LightGBM’s “Multiclass” Mode Can Silently Fail

Even though `model.get_params()` displayed:

```
'objective': 'multiclass', 'num_class': 4
```

LightGBM internally reverted to **regression mode** because the encoded target had 5 unique numeric values due to `None`.

### Lesson
👉 **LightGBM will silently ignore multiclass settings if the target labels don’t match the expected class count.**

Always confirm:

```python
np.unique(y_enc)
```

Expected:

```
[0 1 2 3]
```

---

## 🚨 3. Column Alignment Must Be Verified Explicitly

Although the first 5 columns matched between `X` and `X_test`, dirty metadata handling can cause mismatches deeper in the schema.

### Lesson
👉 **Verify full alignment, not just the head.**

Recommended check:

```python
missing_in_test = X.columns.difference(X_test.columns)
missing_in_train = X_test.columns.difference(X.columns)
```

---

## 🚨 4. SVD + NaNs = Degenerate Components

If any column contains NaNs (due to misalignment or dirty values), TruncatedSVD can:

- collapse components into constants  
- return undefined values  
- cause the model to output constant predictions  

### Lesson
👉 **Fill NaNs BEFORE applying SVD.**

```python
X = X.fillna(0)
X_test = X_test.fillna(0)
```

---

## 🚨 5. Notebook State Can Hide Bugs

Running cells out of order can:

- reuse stale SVD objects  
- reuse old encoders  
- keep a regression-mode model in memory  
- produce misleading debug output  

### Lesson
👉 **Restart the kernel when behavior makes no sense.**

---

## 🚨 6. Wide Datasets Behave Differently

With 68k+ features and <2k samples, this is an extremely “wide” dataset. Wide datasets magnify:

- NaN issues  
- alignment errors  
- memory pressure  
- instability in dimensionality reduction  
- constant-prediction failure modes  

### Lesson
👉 **Wide datasets require extra care in preprocessing and validation.**

---

## 🚨 7. Validate Each Stage Independently

Effective debugging sequence:

1. Check target labels → found `None`
2. Check encoded labels → discovered 5 classes
3. Check predictions → constant `4`
4. Check for NaNs
5. Inspect SVD variance
6. Confirm model params vs actual behavior

### Lesson
👉 **Validate data before troubleshooting the model.**  
> 99% of failures originate in the data, not the model.

---

# 🏁 Final Summary

Wide datasets + dirty labels = catastrophic failure modes.

Fixing the single `None` label restores:

- Proper multi-class LightGBM behavior  
- Valid integer predictions  
- Correct inverse-transform  
- Valid submission CSV

The pipeline becomes stable once the data is clean.
