import pickle

def load_pickle(path):
    return pickle.load(open(path, "rb"))  # unsafe deserialization

load_pickle("payload.pkl")
