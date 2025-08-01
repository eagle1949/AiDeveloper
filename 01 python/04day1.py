import sys, json, os

filename = 'record.json'


def load_record():
    if not os.path.exists(filename):
        return {}
    with open(filename, 'r') as f:
        return json.load(f)


def save_record(data):
    with open(filename, 'w') as f:
        json.dump(data, f)
    print("记录已保存.")


# 命令行处理
def main():
    if len(sys.argv) < 2:
        print("请提供命令行参数.")
        return

    command = sys.argv[1]
    record = load_record()

    if command == 'add':
        if len(sys.argv) < 3:
            print("请提供要添加的记录.")
            return
        key = sys.argv[2]
        value = ' '.join(sys.argv[3:])
        record[key] = value
        save_record(record)

    elif command == 'list':
        for key, value in record.items():
            print(f"{key}: {value}")

    else:
        print("未知命令.")

if __name__ == '__main__':
    main()