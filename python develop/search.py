"""
简易记事本
功能：读取txt、保存文本、关键词搜索
"""

def read_txt(filename):
    """1.读取本地txt文件"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return f"【提示】文件 {filename} 不存在！"


def save_txt(filename, text):
    """2.写入保存文本到txt"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"✅ 已经保存到 {filename}")


def search_keyword(filename, keyword):
    """3.关键词检索，输出匹配的行号和内容"""
    print(f"\n-----搜索关键词：{keyword}-----")
    try:
        count = 0
        with open(filename, "r", encoding="utf-8") as f:
            # enumerate拿到行号，从1开始计数
            for line_num, line in enumerate(f, start=1):
                if keyword.lower() in line.lower():
                    print(f"第{line_num}行：{line.strip()}")
                    count += 1
        if count == 0:
            print("没有找到匹配内容")
        else:
            print(f"一共找到 {count} 处匹配\n")
    except FileNotFoundError:
        print("【错误】文件不存在，无法搜索！")


def main():
    file_name = "note.txt"
    while True:
        print("====简易记事本菜单====")
        print("1 读取文件")
        print("2 写入保存文本")
        print("3 关键词检索")
        print("0 退出程序")
        op = input("请输入功能数字：")

        if op == "1":
            res = read_txt(file_name)
            print("\n文件内容：")
            print(res)
            print("-"*30)

        elif op == "2":
            print("请输入要保存的全部内容（输入#end结束输入）：")
            lines = []
            while True:
                line = input()
                if line == "#end":
                    break
                lines.append(line)
            all_text = "\n".join(lines)
            save_txt(file_name, all_text)

        elif op == "3":
            key = input("输入要搜索的关键词：")
            search_keyword(file_name, key)

        elif op == "0":
            print("程序结束")
            break
        else:
            print("输入无效，请重新选择！\n")


if __name__ == "__main__":
    main()