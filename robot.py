
books_dict = {}
def add_book():
    book_id = input("请输入书的id：")
    book_name = input("请输入书的名称：")
    book_position = input("请输入书的位置：")
    is_lend = False

    books_dict[book_id] = {"book_name": book_name,
                           "book_position": book_position,
                           "is_lend": is_lend}
    print(f"数据添加完成：{books_dict[book_id]}")
def del_book():
    book_id = input("请输入书的id：")
    book_info = books_dict[book_id]
    del books_dict[book_id]
    print(f"删除图书：{book_id}:{book_info}")

def select_book():
    print("1：查找详细的图书 2：查找已经借出的图书 3：查看所有的图书信息")
    sub_code = input("请您输入需要使用的功能：")

    if sub_code == "1":
        book_id = input("请输入书的id：")
        print(books_dict[book_id])

    elif sub_code == "2":
        for i in books_dict.items():
            if i[1]["is_lend"]:
                print(i)

    elif sub_code == "3":
        for i in books_dict.items():
            print(i)


def modify_book():
    """图书位置的修改"""
    book_id = input("请输入书的id：")
    book_position = input("请输入书存放新的位置：")
    books_dict[book_id]['book_position'] = book_position
    print(f"修改后的数据：{book_id}：{books_dict[book_id]}")

def give_back():
    book_id = input("请输入书的id：\n")
    books_dict[book_id]["is_lend"] = False

def lend_book():
    book_id = input("请输入书的id：\n")
    books_dict[book_id]["is_lend"] = True

while True:
    print("-" * 60)
    print("1：图书添加  2：图书删除 3：图书位置修改 \n "
          "4：图书借出  5：图书还回 6：图书信息查看  7：退出系统")
    func_code = input("请您输入需要是使用的功能：")
    print("-" * 60)


    if func_code == "1":
        add_book()
    elif func_code == "2":
        del_book()
    elif func_code == "3":
        modify_book()
    elif func_code == "4":
        lend_book()
    elif func_code == "5":
        give_back()
    elif func_code == "6":
        select_book()
    elif func_code == '7':
        break
    else:
        print("输入的选项id无效！")

