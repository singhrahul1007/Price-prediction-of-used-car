# 🧾 Issues in Dataset

## ✅ Completeness Issues

1. Columns like `name`, `company`, `year`, and `Price` do **not** have any missing values (**Good**).
2. **Missing values** are present in the following columns:
   - `kms_driven`
   - `fuel_type`

---

## 🧪 Quality Issues

### 🔢 Data Type Mismatches
- `year` is of type `object` (string) but should be **integer**.
- `price` is of type `object` (string) but should be **float**.
- `kms_driven` is of type `object` (string) but should be **integer** or **float**.

### 🗑️ Garbage or Irrelevant Entries
- In the `company` column: entries like:'I', 'i', 'selling', 'Sale', 'sell', 'Any', '7', '9', 'all', 'scratch', 'urgent'


### ❌ Invalid Values in `year` Column
- Examples of invalid values: '150k', 'TOUR', 'r 15', 'Zest', '/-Rs', '2 bs', 'arry', 'Eon', 'o...', 'ture',
'emi', 'car', 'able', 'no.', 'd...', 'SALE', 'digo', 'sell', 'd Ex', 'n...',
'e...', 'D...', 'Ac', 'go .', 'k...', 'o c4', 'zire', 'cent', 'Sumo',
'cab', 't xe', 'EV2', 'r...', 'zest'

### 💵 Price Column Issues
- Needs to be converted to **numeric**.
- Contains **commas** (`,`) in values.
- Some prices are **missing**.
- One row contains `'Ask For Price'` (non-numeric string).

### 🚗 `kms_driven` Column Issues
- Contains the word `'kms'` (e.g., `"54,000 kms"`).
- Needs conversion to **numeric**.

### ⛽ `fuel_type` Column
- Has **missing values**.
- No invalid values present (**Clean aside from nulls**).