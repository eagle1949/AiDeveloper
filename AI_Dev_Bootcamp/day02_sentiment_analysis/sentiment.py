import pandas as pd

def main():
    df = pd.read_csv("datasets/imdb_sample.csv")
    print("前5条数据：")
    print(df.head())
    pos = df[df.sentiment == "positive"]
    neg = df[df.sentiment == "negative"]
    print(f"正面评论数: {len(pos)}，负面评论数: {len(neg)}")

if __name__ == "__main__":
    main()
