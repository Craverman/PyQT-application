from setuptools import setup, find_packages

setup(name='client_chat_pyqt_June',
      version='0.1',
      description='Client packet',
      packages=find_packages(),  # ,Будем искать пакеты тут(включаем авто поиск пакетов)
      author_email='isp@mail.ru',
      author='Nikolai Nagornyi',
      install_requeres=['PyQt5', 'sqlalchemy', 'pycruptodome', 'pycryptodomex']
      ##зависимости которые нужно до установить
      )
