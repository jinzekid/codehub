#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python
import os 
LIB_INFO = 'lib_info.dat'

#----------------------------工具类---------------------------------#
def is_quit(s):
    if s in ['q', 'Q']:
        return True
    return False

# 列表转换字符串
def get_str_with_list(str_join, arr):
    if len(arr) == 0:
        return ''
    return str_join.join(str(e) for e in arr)

# 字符串转换列表
def get_list_with_str(str_arr, str_join):
    ret_list = str_arr.split(str_join)
    if len(ret_list) == 1 and ret_list[0] == '':
        return []
    return ret_list 

# 图书数据库的初始化
def init_book_database():
    if not os.path.exists(LIB_INFO):
        open(LIB_INFO, 'w').close()

# 清空图书数据
def clear_book_database():
    with open(LIB_INFO, 'w', encoding='utf-8') as f:
        f.truncate()

# 保存图书到图书数据库
def save_book_to_database(book):
    with open(LIB_INFO, 'a', encoding='utf-8') as f:
        print('save book >>>:%s' %len(book.list_patrons_wait_borrow))
        f.write(book.title + ' ' + book.author + ' ' + str(book.is_borrowed_status()) + ' ' + get_str_with_list('+', book.list_patrons_wait_borrow))
        f.write('\n')
        print('>>>图书保存成功<<<')

# 加载数据库中的所有图书
def load_books_from_database():
    list_books = []
    with open(LIB_INFO, 'r', encoding='utf-8') as f:
        for str_line_book_info in f:
            if str_line_book_info == '\n':
                continue   
            str_line_book_info = str_line_book_info.strip()
            print('listbookinfo:' + str_line_book_info)
            list_book_info = str_line_book_info.split(' ')
            cur_patron = int(list_book_info[2])
            if int(list_book_info[2]) == 0:
                cur_patron = None 

            # 对等待借阅人的id字符串进行分割
            if len(list_book_info) == 3:
                list_patrons_wait_borrow = []
            else:
                list_patrons_wait_borrow = get_list_with_str(list_book_info[3], '+')

            print('list_>>>:%s'  %list_patrons_wait_borrow)
            obj_book = Book(list_book_info[0],
                    list_book_info[1],
                    cur_patron,
                    list_patrons_wait_borrow)

            list_books.append(obj_book)

    return list_books


#----------------------------图书类---------------------------------#
class Book(object):

    def __init__(self, title='', author='', current_patron=None, list_wait_borrow=[]):
        self.title = title
        self.author = author
        self.list_patrons_wait_borrow = list_wait_borrow
        self.current_patron = current_patron

    # 借阅状态
    def is_borrowed_status(self):
        if self.current_patron is not None:
            return 1 
        return 0

    def is_borrowed(self):
        if self.is_borrowed_status() == 1:
            return '正被借阅' 

        return '无人借阅'

    # 等待借阅人数
    def number_wait_borrow(self):
        return str(len(self.list_patrons_wait_borrow))

    # 改变图书借阅状态
    def change_book_borrowed_status(self, str_patron_name = None):
        self.current_patron = str_patron_name
        print('图书当前借阅状态已经改变, 借阅人是:%s' %str_patron_name)

    def __str__(self):
        return ('书本信息: 书名:' + self.title + ', 作者:' + self.author + 
                    ', 当前借阅状态:' + self.is_borrowed() +', 当前还有等待借阅(人):' + self.number_wait_borrow())


#----------------------------读者类---------------------------------#
class Patron(object):

    def __init__(self, patron_id, name, list_borrow_books=[]):
        self.name = name 
        self.id = patron_id 
        self.list_borrow_books = list_borrow_books 

    def return_book(str_book_id):

        pass 

    def borrow_book(str_book_id):
        pass 


#----------------------------图书馆类---------------------------------#
class Library(object):
    
    def __init__(self):
        self.list_books = load_books_from_database()

    def add_book(self, book):
        if book == None:
            print("Book can't be none!")
            return 

        self.list_books.append(book)
        # 保存图书信息
        save_book_to_database(book)

    # 更新图书信息, 效率不高
    def update_book(self, book):
        clear_book_database()
        for book in self.list_books:
            print('----%s----' %book)
            save_book_to_database(book)

    def show_books(self):
        print('>>>图书馆图书信息<<<')
        for book in self.list_books:
            print('书名:' + book.title + ', 作者:' + book.author + 
                    ', 当前借阅状态:' +  book.is_borrowed() +', 当前还有等待借阅(人):' + book.number_wait_borrow())
            print('-------------------')
        print('>>>--------------<<<')

    def create_book(self):
        one_book = Book()
        # 输入书名
        while True:
            str_book_title = input('请输入书名:')
            if str_book_title == '':
                print('>>>书名不能为空<<<')
                continue 
            else:
                one_book.title = str_book_title
                break

        # 输入作者
        while True:
            str_book_author = input('请输入作者名:')
            if str_book_author == '':
                print('>>>作者不能为空<<<')
                continue 
            else:
                one_book.author = str_book_author
                break

        return one_book

    def change_book_status(self, str_book_name, str_user_name):
        for book in self.list_books:
            if book.title.upper() == str_book_name.upper():
                if book.is_borrowed_status() == 1: # 如果图书已经被借阅就需要提示用户
                    pass 
                else:
                    book.change_book_borrowed_status(str_user_name)

                # 需要保存修改后的状态
                self.update_book(book)
                break 

        pass 


#----------------------------图书馆类---------------------------------#
def main():

    init_book_database()

    # 生成图书馆
    print('>>>正在生成图书馆<<<')
    lib = Library()
    print('>>>创建成功<<<')

    print('>>>欢迎来到最全图书馆<<<')
    print('请根据提示操作:')

    user_id = ''

    while True:
        print('1.如果你是图书管理员(请按a)\n2.如果你是读者(请按b)(q或Q退出)')
        # 等待用户输入
        str_user = input('>>>:')

        if is_quit(str_user):
            break

        # 如果是图书管理员，就需要输入密码:
        if str_user == 'a':
            while True:
                print('请输入管理员密码(q或Q退出)')
                str_pwd = input('>>>:')

                # 退出管理员
                if is_quit(str_pwd):
                    break

                if str_pwd == '123': # 密码正确, 出现欢迎语
                    user_id = 'admin'
                    break
                else:
                    print('密码错误:(')
        else:
            user_id = 'user'


        if user_id == 'admin':
            print('欢迎进入图书馆里系统...')
            while True:
                print('1.添加图书(a) 2.阅览图书信息(b)(q或Q退出)')
                str_input= input('>>>:')

                if is_quit(str_input):
                    break

                if str_input == 'a': # 添加图书
                    one_book = lib.create_book()
                    lib.add_book(one_book)

                    print('继续(c)...')
                    str_input = input('>>>:')

                    if str_input != 'c':
                        lib.show_books()
                        print('------------------------------------------')
                        continue    
                elif str_input == 'b': # 浏览图书列表
                    lib.show_books()
        else:
            # 读者
            # 需要输入已经注册的读者姓名, 才可以借阅图书
            while True:
                print('请输入用户名:(q或Q退出)')
                str_username = input('>>>:')

                if is_quit(str_username):
                    break

                if str_username != 'jason':
                    print('>>>用户名错误!')
                    continue 



                print('欢迎进入图书馆里系统...')
                while True:
                    print('1.阅览图书信息(a)(q或Q退出)')
                    str_cmd = input('>>>:')
                    
                    if is_quit(str_cmd):break
                    
                    if str_cmd == 'a':lib.show_books()
                    
                    while True:
                        print('请选择需要借阅图书的书名:(q或Q退出)')
                        str_book_name = input('>>>:')

                        if is_quit(str_book_name):
                            break 

                        print('是否借阅此书?(y或n)')
                        str_cmd_yesorno = input('>>>:')
                        if str_cmd_yesorno == 'y':
                            print('借阅成功...')
                            # 修改图书状态
                            lib.change_book_status(str_book_name, str_username)
                            break 





if __name__ == '__main__':
    main()


