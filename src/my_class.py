class MyClass:
    def __init__(self, text):
        self.text = text

    def my_method(self):
        print(self.text)

    def set_text(self, text):
        self.text = text

    def check_text(self):
        if self.text == "hello":
            return True
        return False

    def __del__(self):
        print("destruct")

if __name__ == "__main__":
    obj = MyClass("hello")
    obj.my_method()
    
    print(obj.check_text())
    
    obj.set_text("goodbye")
    print(obj.check_text())
