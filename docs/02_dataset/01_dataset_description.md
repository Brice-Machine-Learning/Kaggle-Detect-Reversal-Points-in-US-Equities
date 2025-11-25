
# 📊 Dataset Description

## Overview

This dataset is a time series classification collection containing anonymized financial data from six instruments, designed to detect structural price-pattern categories (H, L, None).

## Dataset Statistics

- **Total Samples:** 2,760
- **Features:** 68,504 (excluding metadata and target)
- **Date Range:** 2023-04-03 to 2025-01-31
- **Unique Tickers:** 6

## Target Variable — `class_label`

- **H:** High patterns (82 samples, 3.0%)
- **L:** Low patterns (81 samples, 2.9%)
- **None:** No discernible pattern (2,597 samples, 94.1%)

### Class Conversion Mapping

- HH, LH → **H**
- HL, LL → **L**
- Others/NaN → **None**

## Problem Definition

This is a 3-class classification problem for identifying price-pattern structure:

- **H** = Higher High / Lower High patterns  
- **L** = Higher Low / Lower Low patterns  
- **None** = No structural pattern  

## Files Description

### `train.csv`

- 1,932 rows (≈70%)
- Includes all features + `class_label`

### `test.csv`

- 828 rows (≈30%)
- All features except `class_label`
- Includes `id` for predictions

### `sample_submission.csv`

Template with columns: `id`, `class_label`

### `solution.csv`

Ground truth + `Usage` column  

- Public (30%)  
- Private (70%)

## Column Descriptions

### Metadata

- `id`: Unique identifier (test only)
- `ticker_id`: Anonymous instrument ID (001–006)
- `t`: Timestamp

### Feature Columns

- 68,504 engineered features
- Sensitive price data removed
- Many features normalized/standardized

### Target

- `class_label`: H, L, None (train only)

## Data Characteristics

- Each ticker has 460 samples
- Numeric: 5 columns  
- Categorical: 3 columns  

## Evaluation Metric

- **Accuracy**

## Submission Format Example

```text
id,class_label
0,H
1,L
2,None
...
```

## Notes on `ticker_id`

Each ticker represents a different financial instrument. Consider:

- Within-ticker temporal structure  
- Cross-ticker shared behaviors  

## Preprocessing Notes

- Fully anonymized
- Chronological within each ticker
- Sensitive information removed
- Clean + preprocessed

## Tips

- Use time-aware validation  
- Consider ticker-specific features  
- Handle class imbalance  
- Explore ensemble models  
- Engineer rolling/lagged features  
- Avoid leakage  

## Modeling Approaches

- Global model  
- Ticker-specific models  
- Hybrid hierarchical approaches  
- Transfer learning across tickers  
