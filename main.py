import sys
import datetime
import pypresence

from PyQt5 import QtWidgets, QtCore, QtWebEngineWidgets
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineCore import QWebEngineCookieStore
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineSettings, QWebEngineView

@QtCore.pyqtSlot()
def loadFinishedHandler(self):
    if browser.url().url() == "https://discord.com/login":
        browser.load(QUrl('javascript:function login(e) {setInterval(() => {window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.setToken !== undefined) {return m.default.setToken(e)}if (m.setToken !== undefined) {return m.setToken(e)}}}]);console.log("%cWorked!", "font-size: 50px");}, 50), setTimeout(() => {window.location.reload()}, 2500)}function buttonlogin(){login(document.getElementsByClassName("inputDefault-_djjkz input-cIJ7To")[0].value)}var element;(element=document.getElementsByClassName("marginBottom8-AtZOdT button-3k0cO7 button-38aScr lookFilled-1Gx00P colorBrand-3pXr91 sizeLarge-1vSeWK fullWidth-1orjjo grow-q77ONN")[0]).addEventListener("click",buttonlogin),(element=document.getElementsByClassName("marginBottom20-32qID7")[0]).parentElement.removeChild(element),(element=document.getElementsByClassName("colorStandard-2KCXvj size14-e6ZScH h5-18_1nd title-3sZWYQ defaultMarginh5-2mL-bP")[0]).innerHTML="Token",element.id="Token",(element=document.getElementsByClassName("transitionGroup-aR7y1d qrLogin-1AOZMt")[0]).parentElement.removeChild(element),(element=document.getElementsByClassName("verticalSeparator-3huAjp")[0]).parentElement.removeChild(element);'))
    else:
        pass

my_app = QApplication(sys.argv) 
browser = QWebEngineView()

browser.resize(1250,750)
browser.move(100,100)
browser.setWindowTitle("Discord Token Client")
browser.load(QUrl("https://discord.com/login"))
browser.show()
browser.loadFinished.connect(loadFinishedHandler)

with open("presence.cfg", "r") as file:
    presence = file.read()
if presence == "true":
    rpc = pypresence.Presence("914654501724639242")
    rpc.connect()
    rpc.update(state="Release 1.0.0", large_image="discord", start=datetime.datetime.now().timestamp())
else:
    pass

sys.exit(my_app.exec_())