class CustomException1(BaseException):
    pass

class CustomException2(BaseException):
    pass

class CustomException3(BaseException):
    pass

class DataProcessor:
    def method1(self):
        raise CustomException1("Error in method1")

    def method2(self):
        raise CustomException2("Error in method2")

    def method3(self):
        raise CustomException3("Error in method3")

class DataManager:
    def __init__(self):
        self.data_processor = DataProcessor()

    def process_data(self):
        try:
            self.data_processor.method1()
            self.data_processor.method2()
            self.data_processor.method3()
        except CustomException1 as e:
            print(f"Caught CustomException1: {str(e)}")
        except CustomException2 as e:
            print(f"Caught CustomException2: {str(e)}")
        except CustomException3 as e:
            print(f"Caught CustomException3: {str(e)}")

data_manager = DataManager()
data_manager.process_data()