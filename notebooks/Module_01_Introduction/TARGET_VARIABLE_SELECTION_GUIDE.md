# 🎯 Target Variable Selection Guide

**Module 01 - Foundational Concept**

Choosing your target variable is **the most fundamental decision** in any machine learning project. It defines what you're solving, how success is measured, and whether your model will be useful. This guide helps you make that critical choice correctly.

---

## 💡 What is a Target Variable?

**Target Variable** (also called: dependent variable, label, outcome, response variable, Y)

> The variable you want to predict. Everything else in your ML pipeline revolves around predicting this value accurately.

**In our bike project:** `bikes_available` - The number of bikes at a station we want to predict.

---

## 🔍 How to Identify Your Target Variable

### Step 1: Start with the Business Problem

**Ask the core question:** *"What do I need to predict to solve the business problem?"*

| Business Problem | The Question | Target Variable |
|------------------|--------------|-----------------|
| Prevent empty bike stations | How many bikes will be available? | `bikes_available` |
| Reduce customer churn | Will this customer leave? | `churned` (yes/no) |
| Price houses accurately | What should this house sell for? | `sale_price` |
| Detect spam emails | Is this email spam? | `is_spam` (0/1) |
| Forecast sales | How many units will we sell? | `units_sold` |
| Diagnose disease | Does patient have disease? | `has_disease` (yes/no) |

**❌ Common Mistake:** Starting with data instead of the problem

**Wrong approach:**
> "I have weather, time, and station data. What can I predict?"

**Right approach:**
> "I need to prevent empty stations. What prediction helps solve this?"

---

### Step 2: Ensure Business Value & Actionability

**The target must drive actionable decisions.**

#### ✅ Good Targets (Actionable)

| Target | Why It's Good | Action Enabled |
|--------|---------------|----------------|
| `bikes_available` in 1 hour | Operators have time to respond | Deploy rebalancing trucks |
| `customer_will_churn` next month | Time to intervene | Offer retention incentives |
| `machine_will_fail` in 7 days | Time to schedule maintenance | Preventive maintenance |
| `transaction_is_fraud` | Can prevent loss | Block transaction, investigate |

#### ❌ Bad Targets (Not Actionable)

| Target | Why It's Bad | Problem |
|--------|--------------|---------|
| `station_name` | Already known, never changes | No decision to make |
| `bikes_available` 5 minutes ago | Already happened, can't change | Historical data, no value |
| `weather_yesterday` | Already known | Can't act on past |
| `customer_age` | Known, doesn't change | Not a prediction problem |

**Test:** Ask "If I predict this accurately, what specific action will someone take?"

If you can't answer clearly → reconsider your target.

---

### Step 3: Temporal Validity - Predict the Unknown Future

**Golden Rule:** You can only predict things you **don't know now** but **will know later**.

#### ✅ Valid Temporal Targets

```
NOW (Prediction Time)          FUTURE (Evaluation Time)
      ↓                               ↓
┌─────────────────────┐    ┌──────────────────────┐
│ Don't know value    │ →  │ Will know true value │
│ Make prediction     │    │ Can validate         │
└─────────────────────┘    └──────────────────────┘
```

**Examples:**
- ✅ Bikes available in 30 minutes (don't know now, will know later)
- ✅ Will customer churn next quarter (unknown now, will know later)
- ✅ Tomorrow's temperature (unknown now, will know tomorrow)
- ✅ Will loan default (unknown now, will know in months/years)

#### ❌ Invalid Temporal Targets

```
NOW                              
  ↓                               
┌─────────────────────┐    
│ Already know value  │    ← Can't predict what you already know!
└─────────────────────┘    
```

**Examples:**
- ❌ Current temperature (just look at thermometer!)
- ❌ Historical sales from last year (already recorded!)
- ❌ Station GPS coordinates (fixed, never change!)

**Special case - Prediction horizon matters:**

| Horizon | Difficulty | Business Value |
|---------|------------|----------------|
| 5 minutes ahead | Easy | Low (too short to act) |
| 30-60 minutes | Moderate | **High (sweet spot!)** |
| 24 hours ahead | Hard | Moderate (uncertainty increases) |

**For bikes:** Predicting 30-60 minutes ahead gives operators time to rebalance.

---

### Step 4: Measurable & Observable

Your target must be:

#### 📏 **Measurable**
You can collect the actual value to validate predictions.

**✅ Good:**
- `bikes_available` - Counted by sensors (objective number)
- `transaction_amount` - Recorded in database (exact value)
- `customer_clicked_ad` - Event is logged (yes/no)

**❌ Bad:**
- `customer_happiness` - Subjective, hard to quantify consistently
- `product_quality` - Vague, no clear measurement
- `"good" employee` - Undefined criteria

**Fix:** Convert subjective targets into measurable proxies:
- `customer_happiness` → `customer_satisfaction_score` (1-5 survey)
- `product_quality` → `defect_rate` (measurable percentage)

#### 🎯 **Objective**
Multiple people measuring should get same result.

**✅ Objective:** Temperature sensor reading (32.5°C)  
**❌ Subjective:** "How hot is it?" (opinions vary)

#### 🔄 **Consistent**
Measured the same way over time.

**Problem:** Changing definitions invalidate models
- Year 1: Count bikes manually (error-prone)
- Year 2: Automated sensors (accurate)
- → Model trained on Year 1 data doesn't transfer!

**Solution:** Ensure consistent measurement methodology throughout data collection.

---

### Step 5: Avoid Data Leakage

**Data Leakage:** When your target (or features) contain information that wouldn't be available at prediction time.

#### 🚨 Common Leakage Scenarios

**1. Target derived from future information**

**❌ Bad Example:**
```python
# Using information from AFTER the event to predict the event
target = 'will_buy_product'
features = ['product_in_cart', 'completed_purchase']  # Leakage!
```

**Why it's bad:** `completed_purchase` happens AFTER `will_buy_product`. You're using the future to predict the present!

**✅ Fix:**
```python
target = 'will_buy_product'
features = ['browsing_time', 'items_viewed', 'previous_purchases']  # Known before purchase
```

---

**2. Target and feature are inverse relationships**

**❌ Bad Example (Our bike project):**
```python
target = 'bikes_available'
features = ['docks_available']  # Leakage!
```

**Why it's bad:** 
```
bikes_available + docks_available = total_capacity (constant)
```
If you know `docks_available`, you can perfectly calculate `bikes_available`! Model will look amazing but is useless.

**✅ Fix:**
```python
target = 'bikes_available'
features = ['hour', 'day_of_week', 'temperature', 'station_id']  # Independent features
```

---

**3. Using the outcome to predict itself**

**❌ Bad Example:**
```python
target = 'customer_lifetime_value'
features = ['total_purchases_to_date']  # Leakage!
```

**Why it's bad:** CLV includes `total_purchases_to_date` - it's circular!

---

#### ✅ How to Prevent Leakage

**Checklist:**
- [ ] Could I know this feature **before** the target occurs?
- [ ] Is this feature **derived from** the target?
- [ ] Would this feature be **available** in production at prediction time?
- [ ] Is this feature **perfectly correlated** with the target by definition?

**If any answer is "No" or "Yes" (for derived/perfect correlation) → Remove the feature!**

---

### Step 6: Independence Check

When considering multiple targets, ensure they're genuinely independent.

#### ✅ Independent Targets (Can Coexist)

```python
# Different aspects of the same system
target_1 = 'bikes_available'      # Supply side
target_2 = 'demand_next_hour'     # Demand side
```
These are **related but distinct** - you can predict both.

```python
# Different time horizons
target_1 = 'bikes_available_30min'
target_2 = 'bikes_available_2hour'
```
Different prediction problems - build separate models.

#### ❌ Dependent Targets (Problematic)

```python
# Mathematically related
target_1 = 'bikes_available'
target_2 = 'docks_available'
# If total_capacity = 20, then target_2 = 20 - target_1
```
**Redundant!** Predicting one automatically gives you the other.

```python
# Same thing, different units
target_1 = 'temperature_celsius'
target_2 = 'temperature_fahrenheit'
# F = (C × 9/5) + 32
```
**Redundant!** No new information.

```python
# Derived from each other
target_1 = 'revenue'
target_2 = 'revenue_per_customer'
# target_2 = target_1 / number_of_customers
```
**Redundant!** One is derived from the other.

---

## 🎯 Target Variable Selection Checklist

Before finalizing your target, verify:

| ✓ | Criterion | Your Answer |
|---|-----------|-------------|
| ☐ | **Business problem:** Does this solve a real need? | Should be: Yes |
| ☐ | **Actionable:** Can decisions be made based on predictions? | Should be: Yes |
| ☐ | **Unknown now:** Do we NOT know this value currently? | Should be: Yes |
| ☐ | **Known later:** Will we know the true value to validate? | Should be: Yes |
| ☐ | **Measurable:** Can we collect this objectively? | Should be: Yes |
| ☐ | **Consistent:** Measured the same way over time? | Should be: Yes |
| ☐ | **No leakage:** Independent of features & other targets? | Should be: Yes |
| ☐ | **Temporal validity:** Useful prediction time horizon? | Should be: Yes |

**If ANY answer is "No" → Reconsider your target variable!**

---

## 🚲 Case Study: Bike Availability Prediction

### ✅ Why `bikes_available` is the Perfect Target

| Criterion | How It Meets It |
|-----------|-----------------|
| **Business problem** | Solves "prevent empty stations" - clear operational need |
| **Actionable** | Operators deploy rebalancing trucks based on predictions |
| **Unknown now** | We're predicting future availability (30-60 min ahead) |
| **Known later** | Sensors will report actual availability for validation |
| **Measurable** | Sensors count bikes objectively, consistently |
| **Consistent** | Same measurement method across all stations, all times |
| **No leakage** | Not derived from features; features don't use future info |
| **Temporal validity** | 30-60 min gives time to act but not too much uncertainty |

---

### ❌ Why These Are BAD Targets for Bike Prediction

| Bad Target | Why It Fails |
|------------|--------------|
| `station_name` | ❌ Already known - no prediction needed |
| `station_id` | ❌ Fixed attribute - never changes |
| `latitude` / `longitude` | ❌ Station location is constant |
| `timestamp` | ❌ Known at prediction time |
| `docks_available` | ❌ **Data leakage:** `bikes + docks = capacity` (inverse relationship) |
| `temperature` | ❌ This is weather prediction, not bike prediction (wrong problem!) |
| `bikes_available` 5 min ago | ❌ Historical data - already happened |
| `total_capacity` | ❌ Fixed per station - no variation to predict |
| `bikes_available` in 24 hours | ❌ Too far ahead - too uncertain to act on |

---

### 🤔 What About Alternative Targets?

#### Option 1: Binary Classification Approach

**Target:** `station_will_be_empty` (yes/no)

**Pros:**
- Simpler problem (2 classes instead of continuous)
- Directly addresses "prevent empty stations" goal
- Easier to explain to non-technical stakeholders

**Cons:**
- Loses precision (don't know if 0, 1, or 5 bikes)
- Can't distinguish between "almost empty" and "plenty available"
- Less useful for rebalancing optimization (need to know quantities)

**When to use:** If you only care about "empty or not" decision.

---

#### Option 2: Multi-class Classification

**Target:** `availability_level` 
- Class 0: "Empty" (0 bikes)
- Class 1: "Low" (1-5 bikes)
- Class 2: "Medium" (6-15 bikes)
- Class 3: "High" (16+ bikes)

**Pros:**
- More granular than binary
- Still simpler than regression
- May be sufficient for business needs

**Cons:**
- Arbitrary bin boundaries (why 5? why 15?)
- Loses some precision
- Bin boundaries affect model behavior

**When to use:** If exact counts don't matter, just general availability level.

---

#### Option 3: Time Series Forecasting

**Target:** `bikes_available` at specific future times (multi-step)
- t+30min
- t+60min
- t+120min

**Pros:**
- Multiple horizons for different use cases
- Captures temporal dynamics explicitly
- Can show trajectory of availability

**Cons:**
- More complex to build and maintain
- Multiple models or multi-output model needed
- Error compounds at longer horizons

**When to use:** When you need predictions at multiple time points.

---

## 🎓 Common Mistakes & How to Avoid Them

### Mistake 1: Choosing What You CAN Predict Instead of What You SHOULD Predict

**Wrong:**
> "I have lots of data on customer demographics. Let me predict demographics!"

**Right:**
> "I need to reduce churn. Customer demographics are features to predict churn."

**Fix:** Start with the business problem, not the available data.

---

### Mistake 2: Predicting Intermediate Variables Instead of Final Goals

**Wrong:**
> Predict "customer viewed product page" (intermediate)

**Right:**
> Predict "customer made purchase" (final goal)

**Why it matters:** Intermediate metrics don't necessarily correlate with business outcomes.

---

### Mistake 3: Multiple Correlated Targets

**Wrong:**
```python
target_1 = 'monthly_revenue'
target_2 = 'quarterly_revenue'  # Just 3x target_1!
```

**Right:**
```python
target = 'monthly_revenue'  # One clear target
# Derive quarterly as: quarterly = monthly * 3
```

---

### Mistake 4: Using Proxies That Don't Match Goals

**Wrong:**
> Goal: Improve customer satisfaction  
> Target: `number_of_support_tickets`

**Problem:** More tickets could mean more engagement OR more problems. Ambiguous!

**Right:**
> Target: `customer_satisfaction_score` (from surveys)

---

## 📋 Quick Reference: Target Variable Decision Tree

```
┌─────────────────────────────────┐
│ What are you trying to solve?  │
└────────────┬────────────────────┘
             ↓
      ┌──────────────┐
      │ Business Goal│
      └──────┬───────┘
             ↓
   ┌─────────────────────┐
   │ What specific value │
   │ answers that goal?  │
   └─────────┬───────────┘
             ↓
        Your Target
             ↓
   ┌─────────────────────┐
   │ Run through         │
   │ Checklist (above)   │
   └─────────┬───────────┘
             ↓
      All checks pass?
       ↓            ↓
      YES          NO
       ↓            ↓
   Use this    Revise target
    target      ↓
       ↓       Go back to
   Success!  "Business Goal"
```

---

## 🔗 Related Resources

- [ML_MODEL_TYPES_REFERENCE.md](ML_MODEL_TYPES_REFERENCE.md) - Understand what type of target leads to which model type
- [PANDAS_QUICK_REFERENCE.md](PANDAS_QUICK_REFERENCE.md) - How to inspect and manipulate target variables
- Course notebooks - See target variables applied in practice

---

## 💡 Key Takeaways

1. **Start with the business problem, not the data**
   - What decision needs to be made?
   - What prediction enables that decision?

2. **Your target defines everything else**
   - Type of ML problem (regression/classification)
   - Success metrics
   - Feature engineering approach
   - Model selection

3. **A bad target makes a useless model**
   - Even perfect predictions are worthless if the target is wrong
   - Spend time getting this right!

4. **Validate temporal logic**
   - Can you know this at prediction time? (Should be NO)
   - Will you know the true value later? (Should be YES)

5. **Check for leakage constantly**
   - During feature engineering
   - During model evaluation
   - Before deployment

6. **One clear target is better than multiple unclear ones**
   - Focus and clarity beat complexity
   - Can always add more targets later if needed

---

**Remember:** Choosing the right target variable is not a data science problem - it's a business problem. Make sure you understand what you're solving before you start building! 🎯
