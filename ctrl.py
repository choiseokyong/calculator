class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()
        
    def calculate(self):
        pass
        
    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)
<<<<<<< HEAD
        self.view.btn2.clicked.connect(self.view.clearMessage)
=======
        self.view.btn2.clicked.connect(self.view.clearMessage)
        
    def sum(self, a, b):
        try:
            return a+b
        except:
            return "Calculation Error"
>>>>>>> e4ad45a7c6a40df5c802e8a79211f7591de5b855
