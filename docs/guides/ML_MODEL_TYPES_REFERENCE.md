# 🤖 Machine Learning Model Types Reference

**Module 01 - Quick Reference Guide**

A comprehensive overview of ML model types, their applications, and how to choose the right approach for your problem.

---

## 🎯 Quick Decision Guide

**Ask these questions to choose your model type:**

| Your Question | Model Type to Use |
|--------------|-------------------|
| Predicting a number (price, temperature, count)? | **Regression** |
| Predicting a category (spam/not spam, cat/dog)? | **Classification** |
| Want to find natural groups in data? | **Clustering** |
| Have no labels? | **Unsupervised Learning** |
| Predicting future values based on history? | **Time Series Forecasting** |
| Finding unusual/abnormal patterns? | **Anomaly Detection** |
| Learning through trial and error? | **Reinforcement Learning** |
| Ordering items by relevance/importance? | **Ranking** |

---

## 📚 Main Categories of Machine Learning

### 1️⃣ Supervised Learning (Most Common)

**You have labeled data** - Examples with known correct answers

#### 🔢 REGRESSION - Predict Continuous Numbers

**What it is:** Predict a numerical value (continuous output)

**Output:** Number (1.5, 100.3, -5.2, 1000, etc.)

**Common Applications:**
- **Finance:** Stock prices, property values, loan amounts
- **Business:** Sales forecasting, revenue prediction, customer lifetime value
- **Healthcare:** Patient risk scores, treatment duration
- **Transportation:** Trip duration, **bike availability**, traffic flow
- **Energy:** Power consumption, demand forecasting
- **Weather:** Temperature prediction, rainfall amounts
- **E-commerce:** Product pricing, demand estimation

**Popular Models:**
- Linear Regression
- Ridge/Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting (XGBoost, LightGBM)
- Support Vector Regression (SVR)
- Neural Networks

**When to Use:** When your target variable is a continuous number that can take any value within a range.

---

#### 🏷️ CLASSIFICATION - Predict Categories

**What it is:** Predict which category/class something belongs to (discrete output)

**Output:** Category label (0/1, "spam", "cat", "positive", etc.)

##### **Binary Classification** (2 classes)

**Applications:**
- **Finance:** Fraud detection (fraud/legitimate), loan default (yes/no)
- **Marketing:** Customer churn (will leave/will stay), email spam detection
- **Healthcare:** Disease diagnosis (positive/negative), treatment response (effective/not effective)
- **Manufacturing:** Defect detection (defective/good)
- **Security:** Intrusion detection (attack/normal), content moderation (appropriate/inappropriate)

**Popular Models:**
- Logistic Regression
- Decision Trees
- Random Forest Classifier
- Gradient Boosting Classifiers
- Support Vector Machines (SVM)
- Neural Networks
- Naive Bayes

##### **Multi-class Classification** (3+ classes)

**Applications:**
- **Computer Vision:** Image recognition (cat/dog/bird/car), OCR (digit recognition 0-9)
- **NLP:** Sentiment analysis (positive/neutral/negative), topic classification
- **E-commerce:** Product categorization (electronics/clothing/food/toys)
- **Healthcare:** Disease type identification (multiple conditions)
- **Customer Service:** Support ticket routing (billing/technical/account)

**Popular Models:**
- Softmax Regression
- Random Forest Classifier
- Gradient Boosting
- Neural Networks (Softmax output layer)
- K-Nearest Neighbors (KNN)

**When to Use:** When your output is a discrete category or label.

---

### 2️⃣ Unsupervised Learning

**You have unlabeled data** - No "correct answers" provided

#### 🎯 CLUSTERING - Find Natural Groups

**What it is:** Group similar data points together without predefined labels

**Output:** Group/cluster assignments (e.g., "Customer is in segment 2")

**Applications:**
- **Marketing:** Customer segmentation (identify different customer personas)
- **Biology:** Gene expression analysis, species classification
- **Image Processing:** Image segmentation, compression
- **Document Analysis:** Topic modeling, document organization
- **Anomaly Detection:** Outlier identification (points that don't fit any cluster)
- **Recommendation Systems:** Grouping similar users or items
- **Social Networks:** Community detection
- **Retail:** Product grouping, store layout optimization

**Popular Models:**
- K-Means Clustering
- Hierarchical Clustering
- DBSCAN (Density-Based Spatial Clustering)
- Gaussian Mixture Models (GMM)
- Mean Shift
- BIRCH

**When to Use:** When you want to discover natural groupings in your data without pre-defined categories.

---

#### 📉 DIMENSIONALITY REDUCTION - Simplify Data

**What it is:** Reduce number of features while preserving important information

**Output:** Transformed features (fewer dimensions, e.g., 100 features → 10 principal components)

**Applications:**
- **Visualization:** Plot high-dimensional data in 2D/3D
- **Feature Engineering:** Create compressed, informative features
- **Noise Reduction:** Remove irrelevant/redundant information
- **Speed Up Training:** Fewer features = faster models
- **Preprocessing:** For downstream ML tasks
- **Image Compression:** Reduce image size while maintaining quality
- **Text Analysis:** Reduce vocabulary size (Latent Semantic Analysis)

**Popular Models:**
- **PCA** (Principal Component Analysis) - Linear transformation
- **t-SNE** - Non-linear, great for visualization
- **UMAP** - Non-linear, faster than t-SNE
- **Autoencoders** - Neural network-based compression
- **LDA** (Linear Discriminant Analysis) - Supervised dimensionality reduction
- **SVD** (Singular Value Decomposition)

**When to Use:** When you have too many features, want to visualize high-dimensional data, or need to speed up training.

---

#### 🔗 ASSOCIATION RULES - Discover Patterns

**What it is:** Find interesting relationships and patterns in datasets

**Output:** Rules (e.g., "IF customer buys milk THEN they buy bread (80% confidence)")

**Applications:**
- **Retail:** Market basket analysis ("people who bought X also bought Y")
- **E-commerce:** Product recommendations, cross-selling
- **Web Usage Mining:** Identify browsing patterns
- **Healthcare:** Discover symptom-disease associations
- **Fraud Detection:** Identify suspicious transaction patterns

**Popular Algorithms:**
- Apriori
- FP-Growth (Frequent Pattern Growth)
- ECLAT (Equivalence Class Transformation)

**Metrics:**
- **Support:** How often items appear together
- **Confidence:** Likelihood of Y given X
- **Lift:** How much more likely Y is when X is present

**When to Use:** When you want to discover "what goes with what" in transactional or event data.

---

### 3️⃣ Semi-Supervised Learning

**What it is:** Combines small amount of labeled data with large amount of unlabeled data

**When to Use:**
- Labeling is expensive or time-consuming
- You have lots of unlabeled data but limited labeled examples
- Manual annotation requires expert knowledge

**Applications:**
- **Medical Imaging:** Few labeled scans (expensive expert annotation), many unlabeled
- **Speech Recognition:** Limited transcribed audio, abundant unlabeled recordings
- **Web Content Classification:** Few labeled pages, millions of unlabeled
- **Protein Structure Prediction:** Limited experimentally verified structures

**Approaches:**
- Self-training
- Co-training
- Graph-based methods
- Generative models

---

### 4️⃣ Reinforcement Learning

**What it is:** Agent learns by interacting with environment and receiving rewards/penalties

**Key Concepts:**
- **Agent:** The learner/decision maker
- **Environment:** What the agent interacts with
- **State:** Current situation
- **Action:** What the agent can do
- **Reward:** Feedback (positive or negative)
- **Policy:** Strategy for choosing actions

**Applications:**
- **Gaming:** AlphaGo, Chess engines, video game AI
- **Robotics:** Robot learning to walk, manipulate objects, navigate
- **Autonomous Vehicles:** Self-driving cars, drones
- **Finance:** Trading strategies, portfolio optimization
- **Resource Management:** Traffic light control, power grid optimization
- **Personalization:** Recommendation systems, ad placement
- **Manufacturing:** Production scheduling, quality control

**Popular Approaches:**
- Q-Learning
- Deep Q-Networks (DQN)
- Policy Gradients
- Actor-Critic Methods
- Proximal Policy Optimization (PPO)
- Monte Carlo Tree Search (MCTS)

**When to Use:** When you have a sequential decision-making problem where actions have long-term consequences.

---

### 5️⃣ Specialized Types

#### 📅 TIME SERIES FORECASTING

**What it is:** Predict future values based on historical time-ordered data

**Unique Characteristics:**
- Data points have temporal ordering (order matters!)
- May have trends, seasonality, cycles
- Recent past usually more relevant than distant past

**Applications:**
- **Finance:** Stock prices, currency exchange rates
- **Weather:** Temperature, precipitation forecasting
- **Business:** Sales forecasting, demand prediction
- **Energy:** Load forecasting, renewable energy production
- **Transportation:** Traffic prediction, **future bike availability**
- **Healthcare:** Disease outbreak prediction, patient monitoring

**Popular Models:**
- **Classical:** ARIMA, SARIMA, Exponential Smoothing
- **Modern:** Prophet (Facebook), LSTM, GRU
- **Hybrid:** N-BEATS, DeepAR

**Key Concepts:**
- **Stationarity:** Constant statistical properties over time
- **Autocorrelation:** How current value relates to past values
- **Seasonality:** Recurring patterns (daily, weekly, yearly)
- **Trend:** Long-term increase or decrease

**When to Use:** When temporal order matters and you want to predict future values.

---

#### 🚨 ANOMALY DETECTION

**What it is:** Identify unusual, rare, or suspicious observations that differ from normal patterns

**Output:** Anomaly score or binary classification (normal/anomalous)

**Applications:**
- **Cybersecurity:** Intrusion detection, malware identification
- **Finance:** Fraud detection, suspicious transactions
- **Manufacturing:** Defect detection, equipment failure prediction
- **Healthcare:** Disease outbreak detection, abnormal vitals
- **Network Monitoring:** Unusual traffic patterns, system failures
- **IoT:** Sensor malfunction detection

**Popular Models:**
- Isolation Forest
- One-Class SVM
- Local Outlier Factor (LOF)
- Autoencoders (Neural Networks)
- Statistical methods (Z-score, IQR)
- DBSCAN (density-based)

**When to Use:** When you're looking for rare, unusual, or suspicious patterns rather than predicting specific values.

---

#### 🏆 RANKING

**What it is:** Order items by relevance, importance, or predicted quality

**Output:** Ordered list or relevance scores

**Applications:**
- **Search Engines:** Rank search results by relevance
- **Recommendation Systems:** Rank products, movies, content
- **Information Retrieval:** Document ranking
- **E-commerce:** Product search results
- **Social Media:** Content feed ordering

**Popular Models:**
- LambdaMART
- RankNet
- ListNet
- Learning to Rank (LTR) algorithms

**Evaluation Metrics:**
- NDCG (Normalized Discounted Cumulative Gain)
- MAP (Mean Average Precision)
- MRR (Mean Reciprocal Rank)

**When to Use:** When order matters more than absolute predictions.

---

## 🚲 For Our Bike Availability Project

### Why We Use Regression

Our project uses **Regression** because:
- ✅ Target is continuous (bikes available: 0, 1, 2, ..., 20)
- ✅ Want exact number predictions (not just "high" or "low")
- ✅ Business needs specific counts for operational decisions

### Alternative Approaches We Could Consider

#### 1. **Classification Approach**
Convert to categories:
- "Empty" (0 bikes)
- "Low" (1-5 bikes)
- "Medium" (6-15 bikes)  
- "High" (16+ bikes)

**Pros:** Simpler, might be sufficient for business needs  
**Cons:** Loses precision, can't predict exact numbers

---

#### 2. **Time Series Forecasting**
Predict future availability using temporal patterns:
- LSTM/GRU for capturing long-term dependencies
- Prophet for handling seasonality
- ARIMA for classical time series modeling

**Use Case:** "What will availability be 1 hour from now?"  
**Could be a Module 05 extension!**

---

#### 3. **Anomaly Detection**
Find unusual availability patterns:
- Detect stations with abnormal emptying rates
- Identify unexpected demand spikes
- Flag system malfunctions

**Use Case:** Alert operators to unusual situations

---

#### 4. **Clustering**
Group similar stations:
- Find stations with similar usage patterns
- Identify station "types" (commuter hubs, tourist areas, residential)
- Build specialized models per cluster

**Use Case:** Targeted rebalancing strategies per station type

---

## 📊 Real-World Industry Examples

| Industry | Problem | Model Type | Specific Example |
|----------|---------|------------|------------------|
| **E-commerce** | How much will customer spend? | Regression | Cart value prediction |
| **E-commerce** | Will customer purchase? | Binary Classification | Conversion prediction |
| **E-commerce** | Which product category? | Multi-class Classification | Auto-categorization |
| **E-commerce** | Recommend products | Ranking/Collaborative Filtering | "You might also like..." |
| **Healthcare** | Patient risk score | Regression | ICU mortality risk |
| **Healthcare** | Disease present? | Binary Classification | Cancer detection |
| **Healthcare** | Which disease type? | Multi-class Classification | Diagnosis from symptoms |
| **Healthcare** | Patient groups | Clustering | Treatment response groups |
| **Finance** | Loan default amount | Regression | Expected loss |
| **Finance** | Will loan default? | Binary Classification | Credit risk assessment |
| **Finance** | Fraud detection | Anomaly Detection | Unusual transactions |
| **Finance** | Trading strategy | Reinforcement Learning | Algorithmic trading |
| **Manufacturing** | Machine failure time | Regression | Predictive maintenance |
| **Manufacturing** | Defect present? | Binary/Anomaly Detection | Quality control |
| **Manufacturing** | Defect type | Multi-class Classification | Root cause analysis |
| **Marketing** | Customer lifetime value | Regression | CLV prediction |
| **Marketing** | Will customer churn? | Binary Classification | Retention modeling |
| **Marketing** | Customer segments | Clustering | Persona identification |
| **Marketing** | Email spam? | Binary Classification | Spam filtering |
| **Transportation** | Trip duration | Regression | **Similar to our project!** |
| **Transportation** | Traffic prediction | Time Series | Congestion forecasting |
| **Retail** | Next week sales | Time Series Forecasting | Inventory optimization |
| **Retail** | Product recommendations | Ranking/Collaborative Filtering | Personalization |
| **Security** | Network intrusion? | Anomaly Detection | IDS systems |
| **NLP** | Sentiment | Multi-class Classification | Positive/Neutral/Negative |
| **Computer Vision** | Object in image? | Multi-class Classification | Image tagging |
| **Robotics** | Learn to walk | Reinforcement Learning | Motion control |

---

## 🎓 Key Takeaways

1. **Your output determines the type:**
   - Number → Regression
   - Category → Classification
   - Groups → Clustering
   - Sequence of decisions → Reinforcement Learning

2. **Label availability matters:**
   - Have labels → Supervised (Regression/Classification)
   - No labels → Unsupervised (Clustering/Dimensionality Reduction)
   - Few labels → Semi-supervised

3. **Context matters:**
   - Temporal order important → Time Series
   - Finding outliers → Anomaly Detection
   - Ordering by relevance → Ranking

4. **You can combine approaches:**
   - Clustering first, then regression per cluster
   - Anomaly detection for preprocessing, then classification
   - Time series features fed into regression model

5. **Start simple:**
   - Begin with standard supervised learning (regression/classification)
   - Add complexity only if needed
   - Understand your problem deeply before choosing exotic methods

---

## 🔗 Additional Resources

- **Scikit-learn Documentation:** https://scikit-learn.org/stable/
- **Machine Learning Crash Course (Google):** https://developers.google.com/machine-learning/crash-course
- **Stanford CS229:** http://cs229.stanford.edu/
- **Deep Learning Book:** https://www.deeplearningbook.org/

---

**Remember:** The right model type depends on your problem, data, and business goals. Always start by clearly defining what you're trying to predict! 🎯
