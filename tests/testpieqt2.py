from pieqt import*

app = App()
layout = QVboxLayout()
btn1 = QPushButton("Ok")
btn2 = QPushButton("Cancel")
layout.addWidget(btn1)
layout.addWidget(btn2)
app.setLayout(layout)
app.run()

