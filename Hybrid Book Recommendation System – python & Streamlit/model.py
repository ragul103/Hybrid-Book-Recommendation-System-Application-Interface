import pandas as pd
import pickle
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

with open(BASE_DIR / "user_item.pkl", "rb") as f:
    user_item = pickle.load(f)

with open(BASE_DIR / "user_sim_df.pkl", "rb") as f:
    user_sim_df = pickle.load(f)

with open(BASE_DIR / "item_sim_df.pkl", "rb") as f:
    item_sim_df = pickle.load(f)

final_df = pd.read_pickle(BASE_DIR / "final_df.pkl")


def similar_users(user_id, top_n=5):

    similarities = user_sim_df[user_id].copy()

    similarities.loc[user_id] = 0

    return similarities.sort_values(
        ascending=False
    ).head(top_n)


def similar_books(book_name, top_n=3):

    similarities = item_sim_df[book_name].copy()

    similarities.loc[book_name] = 0

    return similarities.sort_values(
        ascending=False
    ).head(top_n)


def country_recommend(user_id, top_n=5):

    user_data = final_df[
        final_df["User-ID"] == user_id
    ]

    if user_data.empty:
        return []

    user_country = user_data[
        "Country"
    ].iloc[0]

    country_books = (
        final_df[
            final_df["Country"] == user_country
        ]
        ["Book-Title"]
        .value_counts()
        .head(top_n)
        .index
        .tolist()
    )

    return country_books


def author_recommend(user_id, top_n=5):

    user_data = final_df[
        final_df["User-ID"] == user_id
    ]

    if user_data.empty:
        return []

    user_authors = (
        user_data[
            "Book-Author"
        ]
        .dropna()
        .unique()
    )

    author_books = (
        final_df[
            final_df["Book-Author"].isin(
                user_authors
            )
        ]
        ["Book-Title"]
        .value_counts()
        .head(top_n)
        .index
        .tolist()
    )

    return author_books


def recommend_books(user_id, top_n=10):

    user_id = int(user_id)

    if user_id not in user_item.index:
        return ["User not found"]

    sim_users = similar_users(
        user_id,
        top_n=5
    ).index

    user_books = set()

    for u in sim_users:

        books = user_item.loc[u]

        user_books.update(
            books[
                books > 0
            ].index
        )

    user_rated = user_item.loc[user_id]

    user_rated = user_rated[
        user_rated > 0
    ].index

    item_books = set()

    for book in user_rated:

        if book in item_sim_df.columns:

            item_books.update(
                similar_books(
                    book,
                    top_n=3
                ).index
            )

    country_books = set(
        country_recommend(
            user_id,
            top_n=5
        )
    )

    author_books = set(
        author_recommend(
            user_id,
            top_n=5
        )
    )

    all_books = []

    all_books += list(user_books) * 4
    all_books += list(item_books) * 5
    all_books += list(country_books) * 1
    all_books += list(author_books) * 2

    book_scores = Counter(all_books)

    for book in user_rated:
        book_scores.pop(
            book,
            None
        )

    recommended = [
        book
        for book, score
        in book_scores.most_common(top_n)
    ]

    return recommended