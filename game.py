import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QGridLayout, QMainWindow
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize


class Multi(QMainWindow):
	def __init__(self):
		super().__init__()
		self.initUI()
		self.user_record_count = QLabel('0', self)
		self.records_table_users_array = {}


	def initUI(self):
		self.autorization()
		self.login_user = ''

		# Настройки QWidget. Отрисовка окна
		self.setGeometry(140, 50, 400, 500) # (margin-left, margin-top, width, height)
		self.show()

	def autorization(self):
		self.logWindow = QWidget(self)
		self.setCentralWidget(self.logWindow)
		self.setWindowTitle('Угадай фильм - Авторизация')

		self.title_log = QLabel('Авторизация', self.logWindow)
		self.title_log.setStyleSheet('QLabel {font-size: 20px}')
		self.title_log.move(140, 130)

		# Поля ввода
		self.loginLabel_log = QLabel('Введите логин :', self.logWindow)
		self.loginInput_log = QLineEdit(self.logWindow)
		self.loginLabel_log.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.loginInput_log.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.loginLabel_log.resize(152, 30)
		self.loginInput_log.resize(190, 30)
		self.loginLabel_log.move(29, 172)
		self.loginInput_log.move(181, 172)

		self.passwordText_log = QLabel('Введите пароль :', self.logWindow)
		self.passwordInput_log = QLineEdit(self.logWindow)
		self.passwordText_log.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.passwordInput_log.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.passwordText_log.resize(152, 30)
		self.passwordInput_log.resize(190, 30)
		self.passwordText_log.move(29, 210)
		self.passwordInput_log.move(181, 210)

		# Результат (Ошибки)
		self.resultText_log = QLabel('', self.logWindow)
		self.resultText_log.setStyleSheet('QLabel {color: #FF0000; font-size: 14px;}')
		self.resultText_log.resize(400, 20)

		# Кнопка Вход
		self.btn_log = QPushButton('Войти в игру', self.logWindow)
		self.btn_log.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.btn_log.clicked.connect(self.form_log) # событие при нажатии
		self.btn_log.resize(160, 38)
		self.btn_log.move(120, 310)

		# Текст с кнопкой для Регистрации
		self.info_regLabel_1_log = QLabel('Если у Вас нет личного кабинета, то', self.logWindow)
		self.info_regLabel_2_log = QLabel('Вам необходимо', self.logWindow)
		self.info_regBtn_log = QPushButton('Зарегистрироваться', self.logWindow)
		self.info_regLabel_1_log.setStyleSheet('''QLabel {font-size: 13px;}''')
		self.info_regLabel_2_log.setStyleSheet('''QLabel {font-size: 13px;}''')
		self.info_regBtn_log.setStyleSheet('''QPushButton {padding-bottom: 0px; background-color: none; font-size: 13px; border: 0; border-bottom: 1px solid black;}
			QPushButton:hover {border-bottom: 1px solid transparent;}''')
		self.info_regBtn_log.clicked.connect(self.registration)
		self.info_regLabel_1_log.move(92, 370)
		self.info_regLabel_2_log.move(88, 388)
		self.info_regBtn_log.move(189, 388)


	def registration(self):
		self.regWindow = QWidget(self)
		self.setCentralWidget(self.regWindow)
		self.setWindowTitle('Угадай фильм - Регистрация')


		## Registration
		self.title_reg = QLabel('Регистрация', self.regWindow)
		self.title_reg.setStyleSheet('QLabel {font-size: 20px}')
		self.title_reg.move(143, 130)

		self.loginLabel_reg = QLabel('Придумайте логин* :', self.regWindow)
		self.loginInput_reg = QLineEdit(self.regWindow)
		self.loginLabel_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.loginInput_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.loginLabel_reg.resize(152, 30)
		self.loginInput_reg.resize(190, 30)
		self.loginLabel_reg.move(29, 172)
		self.loginInput_reg.move(181, 172)

		self.passwordText_reg = QLabel('Введите пароль* :', self.regWindow)
		self.passwordInput_reg = QLineEdit(self.regWindow)
		self.passwordText_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.passwordInput_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.passwordText_reg.resize(152, 30)
		self.passwordInput_reg.resize(190, 30)
		self.passwordText_reg.move(29, 210)
		self.passwordInput_reg.move(181, 210)

		self.password2Text_reg = QLabel('Подтвердите пароль* :', self.regWindow)
		self.password2Input_reg = QLineEdit(self.regWindow)
		self.password2Text_reg.setStyleSheet('QLabel {padding: -2px 5px; color: #FFFFFF; font-size: 13px; border-left: 1.5px solid #6491A3; border-top: 1.5px solid #6491A3; border-top-left-radius: 4px; border-bottom-left-radius: 4px; background-color: #8AAFBF;}')
		self.password2Input_reg.setStyleSheet('QLineEdit {padding: -2px 5px; font-size: 14px; border-top: 1.5px solid #979797; border-top-right-radius: 4px; border-bottom-right-radius: 4px; background-color: #C7C7C7;}')
		self.password2Text_reg.resize(152, 30)
		self.password2Input_reg.resize(190, 30)
		self.password2Text_reg.move(29, 248)
		self.password2Input_reg.move(181, 248)

		# Результат (Ошибки)
		self.resultText_reg = QLabel('', self.regWindow)
		self.resultText_reg.setStyleSheet('QLabel {color: #FF0000; font-size: 14px;}')
		self.resultText_reg.resize(400, 20)

		# Кнопка регистрации
		self.btn_reg = QPushButton('Зарегистрироваться', self.regWindow)
		self.btn_reg.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.btn_reg.clicked.connect(self.form_reg) # событие при нажатии
		self.btn_reg.resize(160, 38)
		self.btn_reg.move(120, 348)

		# Текст с кнопкой для Регистрации
		self.info_regLabel_1_log = QLabel('Если у Вас есть личный кабинет, то', self.regWindow)
		self.info_regLabel_2_log = QLabel('Вам необходимо', self.regWindow)
		self.info_logBtn_reg = QPushButton('Войти', self.regWindow)
		self.info_regLabel_1_log.setStyleSheet('QLabel {font-size: 13px;}')
		self.info_regLabel_2_log.setStyleSheet('QLabel {font-size: 13px;}')
		self.info_logBtn_reg.setStyleSheet('''QPushButton {padding-bottom: 0px; background-color: none; font-size: 13px; border: 0; border-bottom: 1px solid black;}
			QPushButton:hover {border-bottom: 1px solid transparent;}''')
		self.info_logBtn_reg.clicked.connect(self.autorization)
		self.info_regLabel_1_log.move(94, 408)
		self.info_regLabel_2_log.move(132, 426)
		self.info_logBtn_reg.move(234, 426)


	def img_cinema(self):
		# self.cinema_img = QLabel(self.logWindow)
		# self.cinema_pix_img = QtGui.QPixmap("img/img.jpg")
		self.cinema_img.setPixmap(self.cinema_pix_img)
		self.cinema_img.resize(360, 270)
		self.cinema_img.move(20, 75)


	def menu_game(self):
		self.menu_gameWindow = QWidget(self)
		self.setCentralWidget(self.menu_gameWindow)
		self.setWindowTitle('Меню')

		self.start_game = QPushButton('Начать игру', self.menu_gameWindow)
		self.results_players = QPushButton('Рекорды', self.menu_gameWindow)
		self.info_game = QPushButton('Инструкция', self.menu_gameWindow)
		self.close_game = QPushButton('Выйти из игры', self.menu_gameWindow)

		self.start_game.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.results_players.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.info_game.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.close_game.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')

		self.start_game.clicked.connect(self.game)
		self.results_players.clicked.connect(self.records_table_users)
		# self.info_games.clicked.connect(self.records_table_users)
		self.close_game.clicked.connect(self.close_game_btn)

		self.start_game.resize(300, 38)
		self.results_players.resize(300, 38)
		self.info_game.resize(300, 38)
		self.close_game.resize(300, 38)

		self.start_game.move(50, 155)
		self.results_players.move(50, 200)
		self.info_game.move(50, 245)
		self.close_game.move(50, 290)

		self.user_record_count.setText('0') # Онулирование счета


	def btns_style(self):
		self.btn_1.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #CA0526; border-top: 1.5px solid #CA0526; background-color: #F30625; }''')
		self.btn_2.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #CA0526; border-top: 1.5px solid #CA0526; background-color: #F30625; }''')
		self.btn_3.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #CA0526; border-top: 1.5px solid #CA0526; background-color: #F30625; }''')
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #CA0526; border-top: 1.5px solid #CA0526; background-color: #F30625; }''')

		self.game_name_slide.setStyleSheet('''QLabel {font-size: 24px;}''')
		self.txt_private_btn.setStyleSheet('''QLabel {font-size: 16px;}''')
		self.game_name_slide.move(70, 22)
		self.txt_private_btn.move(88, 366)

		self.btn_1.resize(177, 34)
		self.btn_2.resize(177, 34)
		self.btn_3.resize(177, 34)
		self.btn_4.resize(177, 34)

		self.btn_1.move(20, 403)
		self.btn_2.move(20, 444)
		self.btn_3.move(203, 403)
		self.btn_4.move(203, 444)


	def game(self):
		'''Slide 1'''
		self.cinema_1_Window = QWidget(self)
		self.setCentralWidget(self.cinema_1_Window)
		self.setWindowTitle('Игра началась')

		# Картинка
		self.cinema_img = QLabel(self.cinema_1_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/1+1.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_1_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_1_Window)

		# Кнопки
		self.btn_1 = QPushButton('Не говори никому', self.cinema_1_Window)
		self.btn_2 = QPushButton('1+1', self.cinema_1_Window)
		self.btn_3 = QPushButton('Шутки в сторону', self.cinema_1_Window)
		self.btn_4 = QPushButton('Поездка в Америку', self.cinema_1_Window)

		self.btn_2.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_2)
		self.btn_2.clicked.connect(self.game_slide_2)
		self.btn_3.clicked.connect(self.game_slide_2)
		self.btn_4.clicked.connect(self.game_slide_2)

		self.btns_style()
		self.btn_2.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')


	def game_slide_2(self):
		'''Slide 2'''
		self.cinema_2_Window = QWidget(self)
		self.setCentralWidget(self.cinema_2_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_2_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/mars.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_2_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_2_Window)

		# Кнопки
		self.btn_1 = QPushButton('Марсианин', self.cinema_2_Window)
		self.btn_2 = QPushButton('Обливион', self.cinema_2_Window)
		self.btn_3 = QPushButton('Интерстеллар', self.cinema_2_Window)
		self.btn_4 = QPushButton('Чужой', self.cinema_2_Window)

		self.btn_1.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_3)
		self.btn_2.clicked.connect(self.game_slide_3)
		self.btn_3.clicked.connect(self.game_slide_3)
		self.btn_4.clicked.connect(self.game_slide_3)

		self.btns_style()
		self.btn_1.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_3(self):
		'''Slide 3'''
		self.cinema_3_Window = QWidget(self)
		self.setCentralWidget(self.cinema_3_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_3_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/pobeg.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_3_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_3_Window)

		# Кнопки
		self.btn_1 = QPushButton('Побег', self.cinema_3_Window)
		self.btn_2 = QPushButton('Зеленая миля', self.cinema_3_Window)
		self.btn_3 = QPushButton('Побез из шоушенка', self.cinema_3_Window)
		self.btn_4 = QPushButton('Босиком по мостовой', self.cinema_3_Window)

		self.btn_3.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_4)
		self.btn_2.clicked.connect(self.game_slide_4)
		self.btn_3.clicked.connect(self.game_slide_4)
		self.btn_4.clicked.connect(self.game_slide_4)

		self.btns_style()
		self.btn_3.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_4(self):
		'''Slide 4'''
		self.cinema_4_Window = QWidget(self)
		self.setCentralWidget(self.cinema_4_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_4_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/ostrov.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_4_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_4_Window)

		# Кнопки
		self.btn_1 = QPushButton('Остров проклятых', self.cinema_4_Window)
		self.btn_2 = QPushButton('Начало', self.cinema_4_Window)
		self.btn_3 = QPushButton('Великий Тэйтсби', self.cinema_4_Window)
		self.btn_4 = QPushButton('Поймай меня, если...', self.cinema_4_Window)

		self.btn_4.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_5)
		self.btn_2.clicked.connect(self.game_slide_5)
		self.btn_3.clicked.connect(self.game_slide_5)
		self.btn_4.clicked.connect(self.game_slide_5)

		self.btns_style()
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_5(self):
		'''Slide 5'''
		self.cinema_5_Window = QWidget(self)
		self.setCentralWidget(self.cinema_5_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_5_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/leon.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_5_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_5_Window)

		# Кнопки
		self.btn_1 = QPushButton('Васабы', self.cinema_5_Window)
		self.btn_2 = QPushButton('Невезучие', self.cinema_5_Window)
		self.btn_3 = QPushButton('Исходный код', self.cinema_5_Window)
		self.btn_4 = QPushButton('Леон', self.cinema_5_Window)

		self.btn_4.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_6)
		self.btn_2.clicked.connect(self.game_slide_6)
		self.btn_3.clicked.connect(self.game_slide_6)
		self.btn_4.clicked.connect(self.game_slide_6)

		self.btns_style()
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_6(self):
		'''Slide 6'''
		self.cinema_6_Window = QWidget(self)
		self.setCentralWidget(self.cinema_6_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_6_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/chelentano.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_6_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_6_Window)

		# Кнопки
		self.btn_1 = QPushButton('Блеф', self.cinema_6_Window)
		self.btn_2 = QPushButton('Укрощение строптивого', self.cinema_6_Window)
		self.btn_3 = QPushButton('Безумно влюбленный', self.cinema_6_Window)
		self.btn_4 = QPushButton('Бархатные ручки', self.cinema_6_Window)

		self.btn_2.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_7)
		self.btn_2.clicked.connect(self.game_slide_7)
		self.btn_3.clicked.connect(self.game_slide_7)
		self.btn_4.clicked.connect(self.game_slide_7)

		self.btns_style()
		self.btn_2.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_7(self):
		'''Slide 7'''
		self.cinema_7_Window = QWidget(self)
		self.setCentralWidget(self.cinema_7_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_7_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/grand.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_7_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_7_Window)

		# Кнопки
		self.btn_1 = QPushButton('Хлоя', self.cinema_7_Window)
		self.btn_2 = QPushButton('Милые кости', self.cinema_7_Window)
		self.btn_3 = QPushButton('Гранд отель Будапешт', self.cinema_7_Window)
		self.btn_4 = QPushButton('Гостья', self.cinema_7_Window)

		self.btn_3.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_8)
		self.btn_2.clicked.connect(self.game_slide_8)
		self.btn_3.clicked.connect(self.game_slide_8)
		self.btn_4.clicked.connect(self.game_slide_8)

		self.btns_style()
		self.btn_3.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_8(self):
		'''Slide 8'''
		self.cinema_8_Window = QWidget(self)
		self.setCentralWidget(self.cinema_8_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_8_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/zvezda.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_8_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_8_Window)

		# Кнопки
		self.btn_1 = QPushButton('Одинь день', self.cinema_8_Window)
		self.btn_2 = QPushButton('Бумажные города', self.cinema_8_Window)
		self.btn_3 = QPushButton('Дивергент', self.cinema_8_Window)
		self.btn_4 = QPushButton('Виноваты звезды', self.cinema_8_Window)

		self.btn_4.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_9)
		self.btn_2.clicked.connect(self.game_slide_9)
		self.btn_3.clicked.connect(self.game_slide_9)
		self.btn_4.clicked.connect(self.game_slide_9)

		self.btns_style()
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_9(self):
		'''Slide 9'''
		self.cinema_9_Window = QWidget(self)
		self.setCentralWidget(self.cinema_9_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_9_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/clark.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_9_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_9_Window)

		# Кнопки
		self.btn_1 = QPushButton('До встечи с тобой', self.cinema_9_Window)
		self.btn_2 = QPushButton('Если я останусь', self.cinema_9_Window)
		self.btn_3 = QPushButton('Призрак оперы', self.cinema_9_Window)
		self.btn_4 = QPushButton('Игра престолов', self.cinema_9_Window)

		self.btn_4.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_10)
		self.btn_2.clicked.connect(self.game_slide_10)
		self.btn_3.clicked.connect(self.game_slide_10)
		self.btn_4.clicked.connect(self.game_slide_10)

		self.btns_style()
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_10(self):
		'''Slide 10'''
		self.cinema_10_Window = QWidget(self)
		self.setCentralWidget(self.cinema_10_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_10_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/stagher.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_10_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_10_Window)

		# Кнопки
		self.btn_1 = QPushButton('Стажер', self.cinema_10_Window)
		self.btn_2 = QPushButton('Джой', self.cinema_10_Window)
		self.btn_3 = QPushButton('Знакомство с Факерами', self.cinema_10_Window)
		self.btn_4 = QPushButton('Дедушка легкого пов...', self.cinema_10_Window)

		self.btn_1.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_11)
		self.btn_2.clicked.connect(self.game_slide_11)
		self.btn_3.clicked.connect(self.game_slide_11)
		self.btn_4.clicked.connect(self.game_slide_11)

		self.btns_style()
		self.btn_1.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_11(self):
		'''Slide 11'''
		self.cinema_11_Window = QWidget(self)
		self.setCentralWidget(self.cinema_11_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_11_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/kod.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_11_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_11_Window)

		# Кнопки
		self.btn_1 = QPushButton('Ангелы и демоны', self.cinema_11_Window)
		self.btn_2 = QPushButton('Код да Винчи', self.cinema_11_Window)
		self.btn_3 = QPushButton('Инферно', self.cinema_11_Window)
		self.btn_4 = QPushButton('Страж тьмы', self.cinema_11_Window)

		self.btn_2.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_12)
		self.btn_2.clicked.connect(self.game_slide_12)
		self.btn_3.clicked.connect(self.game_slide_12)
		self.btn_4.clicked.connect(self.game_slide_12)

		self.btns_style()
		self.btn_2.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_12(self):
		'''Slide 12'''
		self.cinema_12_Window = QWidget(self)
		self.setCentralWidget(self.cinema_12_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_12_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/Help.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_12_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_12_Window)

		# Кнопки
		self.btn_1 = QPushButton('Прислуга', self.cinema_12_Window)
		self.btn_2 = QPushButton('12 лет рабства', self.cinema_12_Window)
		self.btn_3 = QPushButton('Иррациональный чел...', self.cinema_12_Window)
		self.btn_4 = QPushButton('Ла-ла-ленд', self.cinema_12_Window)

		self.btn_1.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_13)
		self.btn_2.clicked.connect(self.game_slide_13)
		self.btn_3.clicked.connect(self.game_slide_13)
		self.btn_4.clicked.connect(self.game_slide_13)

		self.btns_style()
		self.btn_1.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_13(self):
		'''Slide 13'''
		self.cinema_13_Window = QWidget(self)
		self.setCentralWidget(self.cinema_13_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_13_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/frodo.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_13_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_13_Window)

		# Кнопки
		self.btn_1 = QPushButton('Властелин колец', self.cinema_13_Window)
		self.btn_2 = QPushButton('Хоббит', self.cinema_13_Window)
		self.btn_3 = QPushButton('Маньяк', self.cinema_13_Window)
		self.btn_4 = QPushButton('Факультет', self.cinema_13_Window)

		self.btn_1.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_14)
		self.btn_2.clicked.connect(self.game_slide_14)
		self.btn_3.clicked.connect(self.game_slide_14)
		self.btn_4.clicked.connect(self.game_slide_14)

		self.btns_style()
		self.btn_1.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_14(self):
		'''Slide 14'''
		self.cinema_14_Window = QWidget(self)
		self.setCentralWidget(self.cinema_14_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_14_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/legenda.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_14_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_14_Window)

		# Кнопки
		self.btn_1 = QPushButton('Хэнкок', self.cinema_14_Window)
		self.btn_2 = QPushButton('Я-легенда', self.cinema_14_Window)
		self.btn_3 = QPushButton('Люди в черном', self.cinema_14_Window)
		self.btn_4 = QPushButton('Я, робот', self.cinema_14_Window)

		self.btn_2.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.game_slide_15)
		self.btn_2.clicked.connect(self.game_slide_15)
		self.btn_3.clicked.connect(self.game_slide_15)
		self.btn_4.clicked.connect(self.game_slide_15)

		self.btns_style()
		self.btn_2.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

	def game_slide_15(self):
		'''Slide 15'''
		self.cinema_15_Window = QWidget(self)
		self.setCentralWidget(self.cinema_15_Window)

		# Картинка
		self.cinema_img = QLabel(self.cinema_15_Window)
		self.cinema_pix_img = QtGui.QPixmap("img/prometey.jpg")
		self.img_cinema()

		self.game_name_slide = QLabel('Угадай фильм по кадру', self.cinema_15_Window)
		self.txt_private_btn = QLabel('Выберите правильный вариант', self.cinema_15_Window)

		# Кнопки
		self.btn_1 = QPushButton('Чужой', self.cinema_15_Window)
		self.btn_2 = QPushButton('Чужой:Завет', self.cinema_15_Window)
		self.btn_3 = QPushButton('Живое', self.cinema_15_Window)
		self.btn_4 = QPushButton('Прометей', self.cinema_15_Window)


		# Кнопки для последнего слайда
		self.btn_4.clicked.connect(self.counter)
		self.btn_1.clicked.connect(self.complete_test)
		self.btn_2.clicked.connect(self.complete_test)
		self.btn_3.clicked.connect(self.complete_test)
		self.btn_4.clicked.connect(self.complete_test)

		self.btns_style()
		self.btn_4.setStyleSheet('''QPushButton {padding-top: -2px; color: #FFFFFF; font-size: 15px; border: 0; border-left: 1.5px solid #3A2D53; border-top: 1.5px solid #3A2D53; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {border-left: 1.5px solid #00A035; border-top: 1.5px solid #00A637#00A035; background-color: #00C140; }''')

		# Полупразрачный фон Модального окна
		self.end_img = QLabel(self.cinema_15_Window)
		self.end_pix_img = QtGui.QPixmap("img/end_window.png")
		self.end_img.setPixmap(self.end_pix_img)
		self.end_img.resize(3600, 2800)
		self.end_img.move(-999, -999)

		# Модальное Окно со Счетом (Завершить)
		if (self.user_record_count.text() < str(10)):
			if (self.user_record_count.text() == str(0)):
				self.res = QLabel('Ваш счет составляет ' + self.user_record_count.text() + ' баллов', self.cinema_15_Window)
				self.res.move(74, 206)
				self.res.setStyleSheet('''QLabel {font-size: 18px;}''')
			elif (self.user_record_count.text() == str(1)):
				self.res = QLabel('Ваш счет составляет ' + self.user_record_count.text() + ' балл', self.cinema_15_Window)
				self.res.setStyleSheet('''QLabel {font-size: 18px;}''')
				self.res.move(83, 206)
			elif (self.user_record_count.text() <= str(4)):
				self.res = QLabel('Ваш счет составляет ' + self.user_record_count.text() + ' балла', self.cinema_15_Window)
				self.res.setStyleSheet('''QLabel {font-size: 18px;}''')
				self.res.move(82, 206)
		elif (self.user_record_count.text() >= str(5) and self.user_record_count.text() <= str(9)):
			self.res = QLabel('Ваш счет составляет ' + self.user_record_count.text() + ' баллов', self.cinema_15_Window)
			self.res.setStyleSheet('''QLabel {font-size: 18px;}''')
			self.res.move(74, 206)
		elif (self.user_record_count.text() >= str(10)):
			self.res = QLabel('Ваш счет составляет ' + self.user_record_count.text() + ' баллов', self.cinema_15_Window)
			self.res.setStyleSheet('''QLabel {font-size: 18px;}''')
			self.res.move(70, 206)

		self.btn_complete = QPushButton('Завершить тест', self.cinema_15_Window)
		self.btn_complete.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.btn_complete.clicked.connect(self.add_record_of_list)
		self.btn_complete.resize(177, 38)
		self.btn_complete.move(113, 240)


	def records_table_users(self):
		'''Таблица рекордов игроков'''
		self.table_records_Window = QWidget(self)
		self.setCentralWidget(self.table_records_Window)
		self.setWindowTitle('Рекорды')

		self.table_records_name = QLabel('Рекорды ТОП-10', self.table_records_Window)
		self.table_records_name.setStyleSheet('''QLabel {font-size: 24px;}''')
		self.table_records_name.move(106, 22)


		self.back_to_menu = QPushButton('Назад в меню', self.table_records_Window)
		self.close_game = QPushButton('Выйти из игры', self.table_records_Window)
		self.back_to_menu.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.close_game.setStyleSheet('''QPushButton {color: #FFFFFF; font-size: 14px; border-radius: 4px; background-color: #5A4E72;}
			QPushButton:hover {background-color: #473468;}
			QPushButton:pressed {background-color: #35264D;}''')
		self.back_to_menu.clicked.connect(self.menu_game)
		self.close_game.clicked.connect(self.close_game_btn)

		self.back_to_menu.resize(177, 34)
		self.close_game.resize(177, 34)

		self.back_to_menu.move(20, 444)
		self.close_game.move(203, 444)


		self.player_id = QLabel('Место', self.table_records_Window)
		self.player_1_id = QLabel('1', self.table_records_Window)
		self.player_2_id = QLabel('2', self.table_records_Window)
		self.player_3_id = QLabel('3', self.table_records_Window)
		self.player_4_id = QLabel('4', self.table_records_Window)
		self.player_5_id = QLabel('5', self.table_records_Window)
		self.player_6_id = QLabel('6', self.table_records_Window)
		self.player_7_id = QLabel('7', self.table_records_Window)
		self.player_8_id = QLabel('8', self.table_records_Window)
		self.player_9_id = QLabel('9', self.table_records_Window)
		self.player_10_id = QLabel('10', self.table_records_Window)
		self.player_name = QLabel('Логин', self.table_records_Window)
		self.player_1_name = QLabel('', self.table_records_Window)
		self.player_2_name = QLabel('', self.table_records_Window)
		self.player_3_name = QLabel('', self.table_records_Window)
		self.player_4_name = QLabel('', self.table_records_Window)
		self.player_5_name = QLabel('', self.table_records_Window)
		self.player_6_name = QLabel('', self.table_records_Window)
		self.player_7_name = QLabel('', self.table_records_Window)
		self.player_8_name = QLabel('', self.table_records_Window)
		self.player_9_name = QLabel('', self.table_records_Window)
		self.player_10_name = QLabel('', self.table_records_Window)
		self.player_value = QLabel('Счет', self.table_records_Window)
		self.player_1_value = QLabel('', self.table_records_Window)
		self.player_2_value = QLabel('', self.table_records_Window)
		self.player_3_value = QLabel('', self.table_records_Window)
		self.player_4_value = QLabel('', self.table_records_Window)
		self.player_5_value = QLabel('', self.table_records_Window)
		self.player_6_value = QLabel('', self.table_records_Window)
		self.player_7_value = QLabel('', self.table_records_Window)
		self.player_8_value = QLabel('', self.table_records_Window)
		self.player_9_value = QLabel('', self.table_records_Window)
		self.player_10_value = QLabel('', self.table_records_Window)

		self.player_id.setStyleSheet('QLabel {color: #FFFFFF; padding: 2px; font-size: 14px; border-top-left-radius: 4px; border: 1px solid #000000; background-color: #8AAFBF;}')
		self.player_1_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_2_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_3_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_4_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_5_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_6_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_7_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_8_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_9_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_10_id.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border-bottom-left-radius: 4px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_name.setStyleSheet('QLabel {color: #FFFFFF; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #8AAFBF;}')
		self.player_1_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_2_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_3_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_4_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_5_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_6_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_7_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_8_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_9_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_10_name.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_value.setStyleSheet('QLabel {color: #FFFFFF; padding: 2px; font-size: 14px; border-top-right-radius: 4px; border: 1px solid #000000; background-color: #8AAFBF;}')
		self.player_1_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_2_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_3_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_4_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_5_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_6_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_7_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_8_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_9_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border: 1px solid #000000; background-color: #C7C7C7;}')
		self.player_10_value.setStyleSheet('QLabel {height: 40px; padding: 2px; font-size: 14px; border-bottom-right-radius: 4px; border: 1px solid #000000; background-color: #C7C7C7;}')

		self.player_id.resize(62, 30)
		self.player_1_id.resize(62, 30)
		self.player_2_id.resize(62, 30)
		self.player_3_id.resize(62, 30)
		self.player_4_id.resize(62, 30)
		self.player_5_id.resize(62, 30)
		self.player_6_id.resize(62, 30)
		self.player_7_id.resize(62, 30)
		self.player_8_id.resize(62, 30)
		self.player_9_id.resize(62, 30)
		self.player_10_id.resize(62, 30)
		self.player_name.resize(150, 30)
		self.player_1_name.resize(150, 30)
		self.player_2_name.resize(150, 30)
		self.player_3_name.resize(150, 30)
		self.player_4_name.resize(150, 30)
		self.player_5_name.resize(150, 30)
		self.player_6_name.resize(150, 30)
		self.player_7_name.resize(150, 30)
		self.player_8_name.resize(150, 30)
		self.player_9_name.resize(150, 30)
		self.player_10_name.resize(150, 30)
		self.player_value.resize(62, 30)
		self.player_1_value.resize(62, 30)
		self.player_2_value.resize(62, 30)
		self.player_3_value.resize(62, 30)
		self.player_4_value.resize(62, 30)
		self.player_5_value.resize(62, 30)
		self.player_6_value.resize(62, 30)
		self.player_7_value.resize(62, 30)
		self.player_8_value.resize(62, 30)
		self.player_9_value.resize(62, 30)
		self.player_10_value.resize(62, 30)

		self.player_id.move(63, 75)
		self.player_1_id.move(63, 104)
		self.player_2_id.move(63, 131)
		self.player_3_id.move(63, 160)
		self.player_4_id.move(63, 189)
		self.player_5_id.move(63, 218)
		self.player_6_id.move(63, 247)
		self.player_7_id.move(63, 276)
		self.player_8_id.move(63, 305)
		self.player_9_id.move(63, 334)
		self.player_10_id.move(63, 363)
		self.player_name.move(124, 75)
		self.player_1_name.move(124, 104)
		self.player_2_name.move(124, 131)
		self.player_3_name.move(124, 160)
		self.player_4_name.move(124, 189)
		self.player_5_name.move(124, 218)
		self.player_6_name.move(124, 247)
		self.player_7_name.move(124, 276)
		self.player_8_name.move(124, 305)
		self.player_9_name.move(124, 334)
		self.player_10_name.move(124, 363)
		self.player_value.move(273, 75)
		self.player_1_value.move(273, 104)
		self.player_2_value.move(273, 131)
		self.player_3_value.move(273, 160)
		self.player_4_value.move(273, 189)
		self.player_5_value.move(273, 218)
		self.player_6_value.move(273, 247)
		self.player_7_value.move(273, 276)
		self.player_8_value.move(273, 305)
		self.player_9_value.move(273, 334)
		self.player_10_value.move(273, 363)


		records_list_read = open('records_list.txt', 'r')
		records_list = records_list_read.read()
		
		if (records_list.count(':') > 0):
			records_list_array = records_list.split(';')

			i = 0
			while True:
				records_list_ar = records_list_array[i].split(':')
				self.records_table_users_array[records_list_ar[0]] = int(records_list_ar[1])

				i += 1
				if (i >= len(records_list_array) - 1):
					break
			records_list_read.close()


			records_table_users_values = list( self.records_table_users_array.values() ) # Добавляем все значения словаря в массив
			records_table_users_values.sort() # Сортировка результатов
			records_table_users_values.reverse() # Переварачиваем сортированный список, чтобы результаты шли от большего к меньшему

			# Функция для получения ключей по значениям
			def get_key(records_table_users_array, value):
			    for k, v in self.records_table_users_array.items():
			        if v == value:
			            return k

			# Вывод 10 Логинов, 10 самые большие (последние) результаты
			if ( len(records_table_users_values) == 1 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
			elif ( len(records_table_users_values) == 2 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
			elif ( len(records_table_users_values) == 3 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
			elif ( len(records_table_users_values) == 4 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
			elif ( len(records_table_users_values) == 5 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
			elif ( len(records_table_users_values) == 6 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
				self.player_6_name.setText( get_key(self.records_table_users_array, records_table_users_values[5]) )
				self.player_6_value.setText( str(records_table_users_values[5]) )
			elif ( len(records_table_users_values) == 7 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
				self.player_6_name.setText( get_key(self.records_table_users_array, records_table_users_values[5]) )
				self.player_6_value.setText( str(records_table_users_values[5]) )
				self.player_7_name.setText( get_key(self.records_table_users_array, records_table_users_values[6]) )
				self.player_7_value.setText( str(records_table_users_values[6]) )
			elif ( len(records_table_users_values) == 8 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
				self.player_6_name.setText( get_key(self.records_table_users_array, records_table_users_values[5]) )
				self.player_6_value.setText( str(records_table_users_values[5]) )
				self.player_7_name.setText( get_key(self.records_table_users_array, records_table_users_values[6]) )
				self.player_7_value.setText( str(records_table_users_values[6]) )
				self.player_8_name.setText( get_key(self.records_table_users_array, records_table_users_values[7]) )
				self.player_8_value.setText( str(records_table_users_values[7]) )
			elif ( len(records_table_users_values) == 9 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
				self.player_6_name.setText( get_key(self.records_table_users_array, records_table_users_values[5]) )
				self.player_6_value.setText( str(records_table_users_values[5]) )
				self.player_7_name.setText( get_key(self.records_table_users_array, records_table_users_values[6]) )
				self.player_7_value.setText( str(records_table_users_values[6]) )
				self.player_8_name.setText( get_key(self.records_table_users_array, records_table_users_values[7]) )
				self.player_8_value.setText( str(records_table_users_values[7]) )
				self.player_9_name.setText( get_key(self.records_table_users_array, records_table_users_values[8]) )
				self.player_9_value.setText( str(records_table_users_values[8]) )
			elif ( len(records_table_users_values) == 10 ):
				self.player_1_name.setText( get_key(self.records_table_users_array, records_table_users_values[0]) )
				self.player_1_value.setText( str(records_table_users_values[0]) )
				self.player_2_name.setText( get_key(self.records_table_users_array, records_table_users_values[1]) )
				self.player_2_value.setText( str(records_table_users_values[1]) )
				self.player_3_name.setText( get_key(self.records_table_users_array, records_table_users_values[2]) )
				self.player_3_value.setText( str(records_table_users_values[2]) )
				self.player_4_name.setText( get_key(self.records_table_users_array, records_table_users_values[3]) )
				self.player_4_value.setText( str(records_table_users_values[3]) )
				self.player_5_name.setText( get_key(self.records_table_users_array, records_table_users_values[4]) )
				self.player_5_value.setText( str(records_table_users_values[4]) )
				self.player_6_name.setText( get_key(self.records_table_users_array, records_table_users_values[5]) )
				self.player_6_value.setText( str(records_table_users_values[5]) )
				self.player_7_name.setText( get_key(self.records_table_users_array, records_table_users_values[6]) )
				self.player_7_value.setText( str(records_table_users_values[6]) )
				self.player_8_name.setText( get_key(self.records_table_users_array, records_table_users_values[7]) )
				self.player_8_value.setText( str(records_table_users_values[7]) )
				self.player_9_name.setText( get_key(self.records_table_users_array, records_table_users_values[8]) )
				self.player_9_value.setText( str(records_table_users_values[8]) )
				self.player_10_name.setText( get_key(self.records_table_users_array, records_table_users_values[9]) )
				self.player_10_value.setText( str(records_table_users_values[9]) )


	def counter(self):
		''' При нажатии на правильный ответ - +1 в счет '''
		temp_count = int(self.user_record_count.text()) + 1
		self.user_record_count.setText( str(temp_count) )


	def complete_test(self):
		'''При нажатии на кнопки последнего слайда'''
		self.end_img.move(0, 0)


	def add_record_of_list(self):
		''' Функция добавления рекордов в файл '''
		records_list_file = open('records_list.txt', 'a')
		records_list_file.write(self.login_user + ':' + self.user_record_count.text() + ';')
		records_list_file.close()
		self.menu_game()


	def close_game_btn(self):
		sys.exit(0)


	def form_log(self):
		# если поля пустые
		if ( self.passwordInput_log.text() == '' ):
			self.resultText_log.setText('Введите пароль!')
			self.resultText_log.move(145, 268)
		if ( self.loginInput_log.text() == '' ):
			self.resultText_log.setText('Введите логин!')
			self.resultText_log.move(150, 268)

		# если поля не пустые
		if ( self.loginInput_log.text() != '' and self.passwordInput_log.text() != '' ):
			list_users_read = open('list_of_users.txt', 'r')
			list_users = list_users_read.read()

			# Если данные есть в Базе
			if (list_users.count(self.loginInput_log.text()) > 0):
				list_users_array = list_users.split(';')
				del list_users_array[-1] # Удаляет последний элемент (Пустая ячейка*)
				i = 0
				while True:
					user_data = list_users_array[i].split(':')
					if (self.loginInput_log.text() == user_data[0] and self.passwordInput_log.text() == user_data[1]):
						self.login_user = self.loginInput_log.text()
						self.menu_game()

					elif (self.loginInput_log.text() == user_data[0] and self.passwordInput_log.text() != user_data[1]):
						self.resultText_log.setText('Не верный пароль!')
						self.resultText_log.move(140, 268)

					i += 1
					if (i >= len(list_users_array)):
						break

			# Если данного Логина нет в Базе
			elif (self.loginInput_log.text() not in list_users):
				self.resultText_log.setText('Такой пользователь не зарегистрирован!')
				self.resultText_log.move(62, 268)

			list_users_read.close()
		self.passwordInput_log.setText('') # очищает поле пароля

	def form_reg(self):
		# если поля пустые
		if ( self.passwordInput_reg.text() == '' ):
			self.resultText_reg.setText('Заполните пароль!')
			self.resultText_reg.move(138, 306)
		if ( self.passwordInput_reg.text() != self.password2Input_reg.text() ):
			self.resultText_reg.setText('Пароли не совпадают!')
			self.resultText_reg.move(128, 306)

		# если поле Логин пустое
		if ( self.loginInput_reg.text() == '' ):
			self.resultText_reg.setText('Заполните логин!')
			self.resultText_reg.move(143, 306)

		# проверка (занят ли логин)
		if ( self.loginInput_reg.text() != '' and self.passwordInput_reg.text() != '' and self.passwordInput_reg.text() == self.password2Input_reg.text() ):
			db_logins = []
			db_read = open('list_of_users.txt', 'r')
			list_of_data_users = db_read.read()
			list_of_data_users = list_of_data_users.split(';')

			# Собираем логины в массив db_logins
			k = 0
			while True:
				user_data = list_of_data_users[k].split(':')
				db_logins.append(user_data[0])

				k += 1
				if (k >= len(list_of_data_users)):
					break

			# Если данный логин есть в Базе, то выдает Ошибку
			if (db_logins.count(self.loginInput_reg.text()) > 0):
				self.resultText_reg.setText('Этот логин занят!')
				self.resultText_reg.move(141, 306)

			# Если данного логина нет в Базе, то регистрируется
			else:
				db_write = open('list_of_users.txt', 'a')
				db_write.write(self.loginInput_reg.text() + ':' + self.passwordInput_reg.text() + ';')
				self.resultText_reg.setText('Вы зарегистировались!')
				self.resultText_reg.move(125, 306)
				db_write.close()

			db_read.close()
		self.passwordInput_reg.setText('') # Очищает поле 
		self.password2Input_reg.setText('')	# Очищает поле


app = QApplication(sys.argv)
my_window = Multi() # экземпляр класса Multi
sys.exit(app.exec_()) # исполняемый файл