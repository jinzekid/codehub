import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
                             QPushButton, QApplication)
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QFileDialog

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 这种静态的方法设置一个用于显示工具提示的字体。我们使用10px滑体字体。
        QToolTip.setFont(QFont('SansSerif', 10))

        """
        # 创建一个提示，我们称之为settooltip()方法。我们可以使用丰富的文本格式
        self.setToolTip('This is a <b>QWidget</b> widget')

        # 创建一个PushButton并为他设置一个tooltip
        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        # btn.sizeHint()显示默认尺寸
        btn.resize(btn.sizeHint())

        # 移动窗口的位置
        btn.move(50, 50)
        """



        # 设置一个选择文件按钮
        btn_chooseFiles = QPushButton('打开', self)
        btn_chooseFiles.setToolTip('请选择文件')
        btn_chooseFiles.clicked.connect(self.do_choose_files)
        btn_chooseFiles.resize(btn_chooseFiles.sizeHint())
        btn_chooseFiles.move(50, 50)


        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('实用小工具')
        self.show()


    def do_choose_files(self):
        """
        directory1 = \
            QFileDialog.getExistingDirectory(self,
                                            "选择文件夹",
                                            './')
        print(directory1)
        """
        """
        fileName1, filetype = \
            QFileDialog.getOpenFileName(self,
                                        "选取文件",
                                        "./",
                                        "All Files (*);;Text Files ("
                                             "*.txt)")  # 设置文件扩展名过滤,注意用双分号间隔
        print(fileName1, filetype)
        """
        files, ok1 = \
            QFileDialog.getOpenFileNames(self,
                                         "多文件选择",
                                         "./",
                                         "All Files (*);;Text Files (*.txt)")
        print(files, ok1)



        """
        fileName2, ok2 = \
            QFileDialog.getSaveFileName(self,
                                        "文件保存",
                                        "./",
                                        "All Files (*);;Text Files ("
                                             "*.txt)")
        """


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec_())
