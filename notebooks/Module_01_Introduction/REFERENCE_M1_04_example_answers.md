# Example Analytical Answers - M1_04 Reflections

**Purpose**: Model good analytical thinking for data exploration reflections in M1_04_sample_data_exploration.ipynb

**How to Use**: Complete your own reflection first, then compare your thinking with these examples to calibrate your analytical depth.

**Quick Navigation:**
- [Time Series Visualization](#time-series-viz)
- [Hourly Patterns](#hourly-patterns)
- [Weather Relationship](#weather-relationship)
- [Weekday vs Weekend](#weekday-weekend)
- [Correlation Heatmap](#correlation-heatmap)

---

## Time Series Visualization {#time-series-viz}

```markdown
<details>
<summary>📘 <strong>Example Student Answer</strong> (click to expand)</summary>

**Patterns I noticed:** Bike availability shows clear temporal cycles across different stations. Station A shows morning dips around 8-9 AM and evening dips around 5-7 PM - classic commuter pattern with people taking bikes TO work in morning and FROM work in evening. Station B stays relatively high throughout, suggesting it's more residential with net outbound commutes. Station C hits zero bikes multiple times during rush hour - this is the exact business problem we're trying to solve!

**What surprised me:** I expected weather to have a stronger visible effect in the time series, but the hourly patterns completely dominate. Also surprised by how frequently stations reach exactly zero bikes - happens 5-10 times just in this small sample, which must frustrate users regularly. The patterns are much more predictable than I expected - not random at all.

**Implications for modeling:** The strong temporal patterns suggest `hour` and `day_of_week` features will be critical predictors. The fact that different stations behave so differently means `station_id` or location features will be important too. Weather effects seem secondary to time patterns. The zero-bike events suggest we need to pay special attention to predicting low availability scenarios - this is where business value is highest.

</details>
```

---

## Hourly Patterns {#hourly-patterns}

```markdown
<details>
<summary>📘 <strong>Example Student Answer</strong> (click to expand)</summary>

**Hourly patterns observed:** Clear U-shape with lowest availability during typical commute hours (8-9 AM shows ~8 bikes average, 5-6 PM shows ~7 bikes) and highest availability mid-day (11 AM-2 PM shows ~12-13 bikes). This matches my expectations for commuter behavior - bikes get taken during rush hours and returned/rebalanced during off-peak.

**Matches expectations?** Yes and no. Expected morning/evening dips, but surprised the evening dip is slightly lower than morning. Maybe people are less time-constrained going home? Or maybe rebalancing happens more in afternoon? Also surprised how consistent the pattern is - not much noise or variation hour-to-hour.

**Implications:** `hour` will definitely be one of the top 2-3 predictors. The non-linear pattern (U-shape, not straight line) suggests tree-based models (Random Forest, XGBoost) will work better than simple linear regression. Should consider creating categorical features like `is_rush_hour` or `is_midday` to capture these distinct periods. Might also need `hour × is_weekend` interaction since weekend patterns are probably totally different (no commute).

</details>
```

---

## Weather Relationship {#weather-relationship}

```markdown
<details>
<summary>📘 <strong>Example Student Answer</strong> (click to expand)</summary>

**Correlation observed:** The correlation coefficient shows **0.15** (weak positive correlation). This means warmer temperature is slightly associated with more bikes being available, but the relationship is not strong.

**Interpretation:** Weak correlation suggests temperature alone isn't a major driver of availability. However, this makes sense when I think about it - warmer weather probably increases cycling (more demand), which actually REDUCES availability as bikes get taken. But warmer weather might also encourage longer trips, bringing bikes back to different stations. The relationship is probably more complex than a simple linear correlation can capture.

**Modeling implications:** Temperature should still be included as a feature (might matter in interactions like `temp × hour`), but I shouldn't expect it to be a top predictor by itself. The weak correlation also suggests I might need to explore non-linear relationships - maybe there's an optimal temperature range where cycling peaks? Could try binning temperature into categories (cold/mild/warm) or adding polynomial features (`temp²`). Most importantly, this confirms that temporal features (hour, day) will likely be much more important than weather for this prediction problem.

</details>
```

---

## Weekday vs Weekend {#weekday-weekend}

```markdown
<details>
<summary>📘 <strong>Example Student Answer</strong> (click to expand)</summary>

**Difference observed:** Weekdays show average of ~10.5 bikes available, weekends show ~11.8 bikes - about 1.3 bike difference. The box plots show weekends have slightly higher median and less variability (shorter box). Both have some outliers but weekdays have more extreme low values.

**Is this surprising?** Not really - makes sense that weekends would have higher availability since there's no commute rush draining bikes at specific times. The lower variability on weekends also makes sense - more consistent leisure usage throughout the day vs. sharp commute peaks on weekdays.

**Modeling implications:** The difference is moderate (1-2 bikes), so `is_weekend` is useful but probably not the strongest predictor alone. More importantly, weekdays and weekends likely have completely different HOURLY patterns - weekday 8 AM (rush hour, low availability) vs. weekend 8 AM (people sleeping, high availability). This means I should definitely create an interaction feature: `hour × is_weekend`. This will let the model learn different temporal patterns for each day type. Tree-based models will naturally split on this, but for linear models I'd need to engineer this interaction explicitly.

</details>
```

---

## Correlation Heatmap {#correlation-heatmap}

<details>
<summary>📘 <strong>Example Student Answer</strong> (click to expand)</summary>

**Strongest correlations with bikes_available:**
- `hour`: -0.35 (moderate negative) - More bikes available during off-peak hours
- `is_weekend`: +0.18 (weak positive) - Slightly more bikes on weekends
- `temperature`: +0.15 (weak positive) - Slightly more bikes when warmer
- `precipitation`, `windspeed`: Near zero - Weather has minimal linear relationship

**Surprising correlations:** I'm surprised `hour` isn't even stronger given how clear the patterns were in the bar chart - suggests the relationship is complex/non-linear rather than simple linear. Also surprised weather variables show such weak correlations - I expected `precipitation` to have stronger negative correlation (rain = more bikes available). This might mean people don't cycle much in this climate regardless of rain, or the relationship is more threshold-based (any rain = bad) than linear.

**Multicollinearity concerns:** No major issues! `temperature` and other weather variables have low intercorrelation (all <0.3), and time features are independent. This is good - means each feature provides unique information.

**Modeling decisions:**
1. **Feature selection**: Keep `hour`, `day_of_week`, `is_weekend` (temporal features dominate). Include weather but with lower expectations.
2. **Model choice**: Weak linear correlations + non-linear patterns visible in charts → Tree-based models (Random Forest, XGBoost) will likely outperform linear regression.
3. **Feature engineering**: Need to capture non-linear relationships - consider binning, interactions (`hour × is_weekend`), or polynomial features.
4. **Next steps**: Investigate why correlations are weaker than expected - might need lag features (bikes_available 1 hour ago) or rolling averages to capture temporal dependencies better.

</details>

---

## Usage Guidelines

**For Students:**
1. Complete your own reflection first (authentic learning)
2. Expand to see examples (self-check understanding)
3. Compare approaches (learn from differences)
4. Use as templates for future analysis (scaffold learning)

**For Tutors:**
These examples provide:
- Concrete standards for "good" analytical thinking
- Domain reasoning connecting observations to business context
- Technical implications for modeling decisions
- Self-contained comparisons without constraining student exploration
