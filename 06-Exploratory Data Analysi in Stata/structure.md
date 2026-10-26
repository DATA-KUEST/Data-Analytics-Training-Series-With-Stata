## 4. Module 1: Structure

```stata
describe
describe, short
codebook, compact
codebook height_cm sex
inspect weight_kg
list in 1/10
list in -5/-1
```

| Command | Gives you |
|---------|-----------|
| `describe` | Names, types, formats, value labels, variable labels |
| `codebook, compact` | One line per variable: number of unique values, missing, min, max, mean |
| `codebook var` | Full detail: type, range, units, unique values, missing, tabulation of codes |
| `inspect var` | A small text histogram plus counts of negative, zero, positive and missing values, and integers |
| `list in 1/10` | The first rows, to see what the data really look like |
| `list in -5/-1 | The last five rows to see what the data looks like |

What to look for:
- Variables that should be numeric but are strings (`str` in `describe`), such as `visit_date` and `state` in the ANC data
- Numeric categorical variables without value labels (all ANC categories; compare `child_nutrition`)
- Ranges that cannot be real (`height_cm` max 999)
- A variable with only one value, or the same value everywhere

```stata
use "data/child_nutrition.dta", clear
codebook, compact
```
You will see `height_cm` with maximum **999.0** and `sex` with maximum **9**: two problems found in ten seconds.

See also the [describe and labels guide](../lesson-03-cleaning-and-labelling/describe-and-labels-guide.md) for reading `describe` output in detail.
