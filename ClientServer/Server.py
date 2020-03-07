from PyQt5.QtCore import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI_Server import Ui_MainWindow
import sys

class Server(QMainWindow):
    port = None

    def __init__(self):
        super(Server, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.server = QTcpServer()
        self.init_slot()

    def init_slot(self):
        self.port = int(self.ui.lineEdit.text())
        self.ui.btnListen.clicked.connect(self.socket_connect)

    def socket_connect(self):
        self.ui.textBrowser.append("listening to port: {}\n".format(str(self.port)))
        self.server.listen(QHostAddress.Any, self.port)
        self.server.newConnection.connect(self.new_socket)

    def new_socket(self):
        sock = self.server.nextPendingConnection()
        addr = sock.peerAddress().toString()
        port = sock.peerPort()
        self.ui.textBrowser.append("connected to port: {}, addr: {} \n".format(str(port), addr))
        sock.readyRead.connect(lambda: self.read_data(sock))
        self.ui.btnListen.clicked.connect(lambda: self.disconnect(sock))
        self.ui.btnListen.setText("disconnected")

    def read_data(self, sock):
        ba = QByteArray()
        while sock.bytesAvailable():
            ba = sock.readAll()
            buf = QBuffer(ba)
            buf.open(QIODevice.ReadOnly)   
            img = QImageReader(buf)
            img = img.read()
            self.ui.labCamera.setPixmap(QPixmap.fromImage(img))

    def disconnect(self, sock):
        addr = sock.peerAddress().toString()
        port = sock.peerPort()
        self.ui.textBrowser.append("disconnecting  port: {}, addr: {} \n".format(str(port), addr))
        sock.close()
        self.ui.btnListen.setText("listen")




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Server()
    w.show()
    sys.exit(app.exec_())