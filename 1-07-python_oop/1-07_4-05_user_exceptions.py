# Целесообразно выбирать именно класс Exception для формирования
# новых собственных классов исключений.

# Мы создали новый тип исключения, просто прописав новый класс.
# И благодаря этому можем отличить ошибку передачи данных принтеру
# от каких-либо других ошибок.

class ExceptionPrintSendData(Exception): # Наследуем от Exception
    """Класс исключения при отправке данных принтеру"""
    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f"Ошибка: {self.message}"


# Имитация работы принтера
class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"печать: {str(data)}")

    def send_data(self, data):
        if not self.printer_answer():
            raise ExceptionPrintSendData("принтер не отвечает")

    def printer_answer(self):
        return False

p = PrintData()


p.print("123")


# Наконец, пользовательские классы исключений
# дают возможность создавать свою иерархию исключений.

# class ExceptionPrint(Exception):
#     """Общий класс исключения принтера"""

# class ExceptionPrintSendData(ExceptionPrint):
#     """Класс исключения при отправке данных принтеру"""

# p = PrintData()

# try:
#     p.print("123")
# except ExceptionPrintSendData as e:
#     print(e)
# except ExceptionPrint:
#     print("Ошибка печати")