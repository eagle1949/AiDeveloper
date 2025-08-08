import pandas as pd

def main():
    df = pd.read_csv("datasets/agnews_sample.csv")
    print("新闻数据示例：")
    print(df.head())

if __name__ == "__main__":
    main()
