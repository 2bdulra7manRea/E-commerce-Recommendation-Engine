import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Index(['ProductID', 'ProductName', 'ProductBrand', 'Gender', 'Price (INR)',
#        'NumImages', 'Description', 'PrimaryColor'],
#       dtype='object')


def processed_data():
    # Read products data from a CSV file
    data = pd.read_csv('dataset.csv')

    # Select relevant columns for processing
    train_data = data[['ProductID', 'ProductName', 'ProductBrand', 'Description','Gender']]

    # Combine training columns into a new 'tags' column
    train_data['tags'] = train_data['ProductBrand'] + train_data['Description'] +  train_data['Gender']

    # Drop unnecessary columns 
    train_data = train_data.drop(columns=['ProductBrand', 'Gender','Description'])

    return train_data


def calculate_similarity(vectors_data):
    # Calculate cosine similarity between vectors_data
    return cosine_similarity(vectors_data)


def convert_to_vectors(train_data, max_features=10000):
    # Convert 'tags' column to vectors using CountVectorizer
    cv = CountVectorizer(max_features=max_features, stop_words='english')
    vectors = cv.fit_transform(train_data)
    return vectors


def get_similar_index_items_by_index(index: int, similarity_data, limit: int):
    items = []
    # Sort the similarity data and retrieve the top 'limit' items
    distance = sorted(list(enumerate(similarity_data[index])), reverse=True)
    for i in distance[:limit]:
        items.append(i[0])
    return items


def fetch_item_from_data_by_index(index: int):
    # Fetch the item from the processed data by index
    train_data = processed_data()
    return train_data.loc[index]


def get_items_by_indics(indics):
    # Get a list of products corresponding to the provided indices
    return [fetch_item_from_data_by_index(i) for i in indics]


def perform(index, limit):
    # Perform the recommendation based on provided index and limit
    train_data = processed_data()

    # Convert 'tags' column to vectors and calculate similarity
    vectors = convert_to_vectors(train_data['tags'].values.astype("U"), 10000)
    similarity = calculate_similarity(vectors)

    # Get similar items based on the provided index and limit
    return get_similar_index_items_by_index(index, similarity, limit)
