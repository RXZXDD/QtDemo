from PyQt5.QtCore import *
from PyQt5.QtNetwork import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from UI_Client import Ui_MainWindow
import sys
import cv2 as cv
class Server(QMainWindow):
    PORT = None
    ADDR = None
    TRAMSIMT_FLAG = False

    def __init__(self):
        super(Server, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.socket = QTcpSocket()
        self.timer = QTimer()
        self.init_slot()
        self.cap = cv.VideoCapture(0) 
        ret, frame = self.cap.read()
        if not ret:
            msg = QMessageBox.warning(self, u'Warining', u'Cannot open camera', 
                                      buttons=QMessageBox.Ok)
        else:
            #print("opened")
            self.timer.start(30)

    def init_slot(self):
        self.ui.btnConntect.clicked.connect(self.socket_connect)
        self.ui.btnDisconnect.clicked.connect(self.disconnect)
        self.timer.timeout.connect(self.display_camera)

    def socket_connect(self):
        self.PORT = int(self.ui.txtPort.toPlainText())
        self.ADDR = self.ui.txtAddr.toPlainText()
        qDebug("connecting to port: {} addr: {} \n".format(str(self.PORT),self.ADDR))
        self.socket.connectToHost(self.ADDR, self.PORT)
        self.socket.connected.connect(self.socket_connected)

    def socket_connected(self):
        qDebug("connected to port: {} addr: {} \n".format(str(self.PORT),self.ADDR))
        self.TRAMSIMT_FLAG = True


    def display_camera(self):
        _, image = self.cap.read()
        img = cv.resize(image, (640,480))
        img = cv.cvtColor(img , cv.COLOR_BGR2RGB)
        img = QImage(img.data, img.shape[1], img.shape[0], QImage.Format_RGB888)
        self.ui.label_2.setPixmap(QPixmap.fromImage(img))
      
        if(self.TRAMSIMT_FLAG):
            try:
                ba = QByteArray()
                buf = QBuffer(ba)
                buf.open(QIODevice.WriteOnly)       
                img.save(buf, "JPG")
                self.socket.write(ba)
            except:
                self.disconnect()

    #def read_data(self, sock):
    #    while sock.byteAvailable():
    #        buf = sock.readAll()
    #        img = QImage().loadFromData(buf)
    #        self.ui.labCamera.setPixmap(QPixmap.fromImage(img))

    def disconnect(self):
        self.ADDR = self.socket.peerAddress().toString()
        self.PORT = self.socket.peerPort()
        qDebug("disconnecting  port: {}, addr: {} \n".format(str(self.PORT), self.ADDR))
        self.socket.close()
        self.TRAMSIMT_FLAG = False





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Server()
    w.show()
    sys.exit(app.exec_())
