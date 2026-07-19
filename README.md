# 📚 Hybrid Book Recommendation System

An end-to-end **Hybrid Book Recommendation System** that generates personalized book suggestions based on user preferences and historical interactions.

The system combines **User–User Collaborative Filtering, Item–Item Similarity, Country-Based Recommendations, and Author-Based Recommendations** to generate relevant book suggestions.

An interactive web application was developed using **Streamlit**, allowing users to enter a User ID, select the number of recommendations, and view personalized book recommendations with book cover images.

---

## 🖥️ Application Preview

![Hybrid Book Recommendation System Interface](User_InterFace.png)

## 📚 Personalized Recommendation Results

![Book Recommendation Results](Recommendation_Result.png)

The interactive Streamlit application allows users to enter a **User ID**, select the number of recommendations, and generate personalized book suggestions via a simple, user-friendly interface.

---

## 🎯 Project Objective

The objective of this project is to develop an end-to-end recommendation system capable of suggesting relevant books based on user preferences and historical rating patterns.

The project covers the complete workflow:

**Data Cleaning → Exploratory Data Analysis → Recommendation Modeling → Hybrid Recommendation Engine → Streamlit Application**

The recommendation system combines multiple recommendation strategies instead of relying on a single technique.

---

## ✨ Key Features

- 📊 Data Cleaning and Preprocessing
- 🔍 Exploratory Data Analysis (EDA)
- 👥 User–User Collaborative Filtering
- 📖 Item–Item Similarity
- 📐 Cosine Similarity
- 🌍 Country-Based Recommendations
- ✍️ Author-Based Recommendations
- 🧠 Hybrid Recommendation Strategy
- ⭐ Weighted Recommendation Ranking
- 🚫 Removal of Previously Rated Books
- 📚 Top-N Personalized Recommendations
- 🖥️ Interactive Streamlit Application
- 🖼️ Book Cover Visualization

---

# 🧠 Recommendation System Approach

The recommendation engine combines four recommendation techniques:

1. User–User Collaborative Filtering
2. Item–Item Similarity
3. Country-Based Recommendations
4. Author-Based Recommendations

The results from these techniques are combined to generate the final personalized recommendations.

---

## 👥 1. User–User Collaborative Filtering

User–User Collaborative Filtering identifies users who have similar book-rating behavior.

A **User-Item Matrix** is created where:

- Rows represent users
- Columns represent books
- Values represent book ratings

Example:

```text
                 Book A    Book B    Book C    Book D

User 1              8         0         7         0
User 2              9         0         8         5
User 3              0         7         0         9
```

The similarity between users is calculated using **Cosine Similarity**.

Users with similar rating patterns are identified, and books preferred by similar users are considered as recommendation candidates.

### Process

```text
Target User
     ↓
User-Item Matrix
     ↓
Cosine Similarity
     ↓
Find Similar Users
     ↓
Collect Books Rated by Similar Users
     ↓
Recommendation Candidates
```

---

## 📖 2. Item–Item Similarity

Item–Item Similarity identifies books that have similar user-rating patterns.

Instead of comparing users, this method compares books based on how users have rated them.

For example:

```text
User likes Book A
       ↓
Find books similar to Book A
       ↓
Book B
Book C
Book D
       ↓
Add as recommendation candidates
```

Cosine similarity is used to calculate similarity between books.

Books similar to those previously rated by the target user are included as recommendation candidates.

---

## 🌍 3. Country-Based Recommendations

Country-Based Recommendation uses the user's location information as an additional recommendation signal.

The system identifies the user's country and finds relevant books associated with users from the same country.

### Process

```text
User ID
   ↓
Identify User Country
   ↓
Find Books Associated with Same Country
   ↓
Select Relevant Books
   ↓
Recommendation Candidates
```

This introduces contextual information into the recommendation system.

---

## ✍️ 4. Author-Based Recommendations

Author-Based Recommendation considers authors associated with books the user has previously interacted with.

The system identifies relevant authors from the user's historical interactions and finds additional books related to those authors.

### Process

```text
User Reading History
       ↓
Identify Relevant Authors
       ↓
Find Books from Those Authors
       ↓
Recommendation Candidates
```

---

# 🔀 Hybrid Recommendation Strategy

The final recommendation engine combines all four recommendation approaches.

```text
                         USER ID
                            │
            ┌───────────────┼───────────────┐
            │               │               │
            ▼               ▼               ▼
       User–User        Item–Item       User Profile
       Similarity       Similarity           │
            │               │          ┌─────┴─────┐
            │               │          ▼           ▼
            │               │       Country      Author
            │               │          │           │
            └───────────────┴──────────┴───────────┘
                            │
                            ▼
                  Candidate Recommendations
                            │
                            ▼
                     Weighted Ranking
                            │
                            ▼
                 Remove Previously Rated
                            │
                            ▼
                  Top-N Recommendations
```

The recommendation sources are combined using a **weighted ranking strategy**.

This allows stronger recommendation signals to have greater influence on the final ranking.

---

## ⭐ Weighted Recommendation Logic

Different recommendation techniques contribute recommendation candidates.

The candidates are combined and ranked according to their assigned importance.

Conceptually:

```text
User–User Recommendations
          +
Item–Item Recommendations
          +
Country Recommendations
          +
Author Recommendations
          ↓
    Weighted Combination
          ↓
      Book Ranking
          ↓
 Remove Already Rated Books
          ↓
 Top-N Unique Recommendations
```

If the same book appears through multiple recommendation techniques, it can receive stronger ranking support.

Previously rated books are removed before producing the final recommendations.

---

# ⚙️ Complete Project Workflow

```text
Raw Dataset
      ↓
Data Cleaning
      ↓
Missing Value Handling
      ↓
Duplicate Handling
      ↓
Data Preprocessing
      ↓
Dataset Integration
      ↓
Exploratory Data Analysis
      ↓
User-Item Matrix Creation
      ↓
Cosine Similarity Calculation
      ↓
┌───────────────────────────────┐
│ User–User Recommendations     │
│ Item–Item Recommendations     │
│ Country-Based Recommendations │
│ Author-Based Recommendations  │
└───────────────────────────────┘
      ↓
Hybrid Recommendation Engine
      ↓
Weighted Ranking
      ↓
Remove Previously Rated Books
      ↓
Top-N Personalized Recommendations
      ↓
Streamlit Web Application
```

---

# 📊 Exploratory Data Analysis

Exploratory Data Analysis was performed to understand the structure, quality, and patterns present in the dataset before building the recommendation system.

The analysis included:

- Rating distribution analysis
- User interaction analysis
- Book popularity analysis
- Author analysis
- Country-level analysis
- User-book interaction patterns
- Missing value analysis
- Duplicate value analysis
- Explicit and implicit rating analysis

EDA helped identify important patterns in user behavior and prepare the dataset for recommendation modeling.

---

# 📂 Dataset

The project uses book recommendation data containing information about users, books, and ratings.

## 👤 Users Data

Contains information such as:

```text
User-ID
Location
Age
```

---

## 📚 Books Data

Contains information such as:

```text
ISBN
Book-Title
Book-Author
Year-Of-Publication
Publisher
Image-URL-S
Image-URL-M
Image-URL-L
```

---

## ⭐ Ratings Data

Contains:

```text
User-ID
ISBN
Book-Rating
```

The datasets are cleaned and merged using common identifiers such as **User-ID** and **ISBN**.

---

# 📐 Cosine Similarity

Cosine Similarity is used to measure similarity between users and between books.

It measures how similar two vectors are based on the angle between them.

A higher cosine similarity score indicates greater similarity.

In this project, cosine similarity is used for:

```text
User ↔ User Similarity

and

Book ↔ Book Similarity
```

This forms the foundation of the collaborative filtering component of the recommendation system.

---

# 🖥️ Streamlit Web Application

The recommendation system is integrated into an interactive web application developed using **Streamlit**.

The application allows users to:

1. Enter a valid **User ID**
2. Select the number of recommendations
3. Click **Generate Recommendations**
4. Receive personalized book suggestions
5. View book cover images
6. View recommended book titles

The interface provides a simple way to interact with the recommendation engine without directly running Python code.

---

# 📚 Personalized Recommendation Results

After entering a valid User ID, the hybrid recommendation engine analyzes available user preferences and generates personalized recommendations.

![Personalized Book Recommendation Results](screenshots/recommendation-results.png)

The final recommendations are displayed with:

- 📖 Book titles
- 🖼️ Book cover images
- 👤 User-specific recommendations

This provides a more visual and user-friendly recommendation experience.

---

# 🛠️ Technologies Used

| Category | Technology |
|---|---|
| Programming Language | Python |
| Data Manipulation | Pandas |
| Numerical Computing | NumPy |
| Machine Learning | Scikit-learn |
| Recommendation Technique | Collaborative Filtering |
| Similarity Measure | Cosine Similarity |
| Data Visualization | Matplotlib, Seaborn |
| Web Application | Streamlit |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

---

# 📁 Project Structure

```text
Hybrid-Book-Recommendation-System/
│
├── README.md
│
├── app.py
│
├── model.py
│
├── requirements.txt
│
├── .gitignore
│
├── notebooks/
│   └── Book_Recommendation_System.ipynb
│
├── screenshots/
│   ├── application-interface.png
│   └── recommendation-results.png
│
└── data/
    └── README.md
```

> Large datasets and generated model artifacts may be excluded from the GitHub repository due to file-size limitations.

---

# 🚀 How to Run the Project

## Step 1 — Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

---

## Step 2 — Navigate to the Project Folder

```bash
cd Hybrid-Book-Recommendation-System
```

---

## Step 3 — Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your web browser.

---

# 📦 Requirements

The main Python libraries used in this project are:

```text
pandas
numpy
scikit-learn
matplotlib
seaborn
streamlit
```

Example installation:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn streamlit
```

---

# 🧪 Example Usage

### Input

```text
User ID: 276822

Number of Recommendations: 5
```

### Process

```text
User ID
   ↓
Analyze User Preferences
   ↓
User–User Similarity
   +
Item–Item Similarity
   +
Country-Based Recommendations
   +
Author-Based Recommendations
   ↓
Weighted Ranking
   ↓
Remove Previously Rated Books
   ↓
Final Personalized Recommendations
```

### Output

The application displays recommended books with their corresponding book cover images and titles.

---

# 📈 Recommendation Techniques

| Technique | Purpose |
|---|---|
| User–User Collaborative Filtering | Finds users with similar rating behavior |
| Item–Item Similarity | Finds books with similar interaction patterns |
| Country-Based Recommendation | Adds location-related recommendation signals |
| Author-Based Recommendation | Recommends books related to relevant authors |
| Weighted Ranking | Combines multiple recommendation signals |
| Hybrid Recommendation | Generates the final personalized recommendations |

---

# 💡 Challenges Addressed

## 1. Sparse User-Item Data

Recommendation datasets often contain many users who have interacted with only a small percentage of available books.

A User-Item Matrix was used to represent user-book interactions for similarity-based recommendation.

---

## 2. Duplicate Recommendations

Multiple recommendation techniques may recommend the same book.

Recommendation candidates are combined and processed to produce a final ranked recommendation list.

---

## 3. Previously Rated Books

Books already rated by the target user are removed from the final recommendations.

This helps prevent recommending books that the user has already interacted with.

---

## 4. Large Similarity Matrices

User and item similarity calculations can require significant memory when working with large datasets.

For deployment, precomputed data or recommendation artifacts can be used to avoid unnecessarily recalculating expensive operations whenever the application starts.

---

# 🔮 Future Improvements

The recommendation system can be further enhanced by implementing:

- Matrix Factorization
- Singular Value Decomposition (SVD)
- Content-Based Filtering
- Book genre-based recommendations
- Book description similarity using NLP
- Recommendation evaluation metrics
- Precision@K and Recall@K
- Cold-start handling for new users
- Search recommendations by book title
- User authentication
- Database integration
- Cloud deployment
- Deep-learning-based recommendation models

---

# 🎯 Project Outcome

This project demonstrates the development of an end-to-end recommendation system covering:

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Recommendation Modeling
      ↓
Collaborative Filtering
      ↓
Hybrid Recommendation Engine
      ↓
Personalized Recommendations
      ↓
Streamlit Application
```

Through this project, I gained practical experience in:

- Python programming
- Data cleaning and preprocessing
- Exploratory Data Analysis
- Pandas and NumPy
- Recommendation systems
- Collaborative filtering
- User–User similarity
- Item–Item similarity
- Cosine similarity
- Hybrid recommendation techniques
- Streamlit application development
- End-to-end Data Science project development

---

# 👨‍💻 Author

**R. Ragul**

B.Tech – Information Technology

Interested in:

**Data Analytics | Data Science | Machine Learning**

---

## ⭐ Support

If you find this project useful or interesting, consider giving the repository a **⭐ Star**.

Thank you for visiting the project!
