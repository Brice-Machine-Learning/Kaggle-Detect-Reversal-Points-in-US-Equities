# 🧠 Lessons Learned — Feature Engineering (Tier 1)

This section documents **practical lessons learned** during Tier 1 feature engineering for the
*Kaggle Detect Reversal Points in U.S. Equities* project.  
These notes are intentionally operational and hardware-aware.

---

## 1. Extremely Wide Data Changes the Game

- A dataset with **~68,500 columns** behaves very differently from tall/narrow tables.
- Operations that are theoretically cheap (sorting, window functions) become expensive when they require
  copying or materializing entire rows.
- Performance bottlenecks were driven more by **column width** than by row count.

**Takeaway:** Always reason about *row movement* vs *column-wise computation* when working with wide data.

---

## 2. Use the Simplest Tool That Touches the Fewest Columns

- DuckDB window functions are powerful, but on wide tables they:
  - materialize full rows
  - incur sorting and memory-copy overhead
- For Tier 1:
  - `pandas` vectorized operations were faster and safer
  - `groupby().shift()` touched only the required columns

**Takeaway:** Tool choice should be **operation-specific**, not pipeline-wide.

---

## 3. Window Functions Are Not Free on CPU-Only Hardware

- SQL-style window functions (`LAG`, rolling windows) are not inherently “cheap”
- On older, CPU-only machines, they can dominate runtime even for small row counts
- This is especially true when the table is wide

**Takeaway:** Reserve SQL window engines for cases where their benefits clearly outweigh their cost.

---

## 4. Checkpoint Early, Not After “Success”

- Long-running notebooks are fragile on constrained hardware
- Waiting until “everything works” before persisting results led to repeated recomputation
- Once the expensive sort completed, immediate checkpointing prevented further time loss

**Takeaway:**  
> *Checkpoint the moment you pay a computational cost — not after the next step.*

---

## 5. Dependency Changes Mid-Session Are Risky

- Installing `pyarrow` mid-session caused Arrow extension registration conflicts
- This required a kernel restart to fully resolve
- Restarting the kernel was costly due to long reload times

**Takeaway:**  
- Avoid introducing new binary dependencies mid-session when possible
- Prefer restart-safe formats (e.g., pickle) for interim checkpoints

---

## 6. Pickle Is Acceptable for Internal, Short-Term Artifacts

- While Parquet is preferred long-term, pickle provided:
  - zero dependency overhead
  - fast write/read for wide DataFrames
  - restart safety
- The pickle file is treated as an **internal checkpoint**, not a production artifact

**Takeaway:** Pragmatism beats format purity during exploratory phases.

---

## 7. Train-First Discipline Prevents Cascading Errors

- Feature engineering was intentionally restricted to the **training set only**
- Test data was deferred until:
  - feature logic was validated
  - runtime was proven acceptable
- This avoided duplicated failures and confusion

**Takeaway:** Never parallelize train/test feature engineering prematurely.

---

## 8. Hardware Constraints Are a Design Input, Not an Afterthought

- The available machine (2012 MacBook Pro, CPU-only) materially influenced design decisions
- Code that runs fine on modern hardware may be unacceptable here
- Engineering decisions were adapted accordingly without sacrificing correctness

**Takeaway:**  
> *Design for the hardware you actually have, not the hardware you wish you had.*

---

## Final Reflection

Tier 1 feature engineering succeeded not because of sophisticated algorithms, but because of:

- disciplined scope control
- careful tool selection
- aggressive checkpointing
- respect for physical constraints

These lessons will directly inform Tier 2 decisions, particularly around whether additional feature
complexity is justified by measurable performance gains.

---

*This document exists to prevent repeating avoidable mistakes — especially under time and hardware constraints.*
