# pip install kivy

# Passos:
# instalar o kivyy
# importar o App e o Builder (GUI)
# criar o aplicativo
# criar a função build

from kivy.app import App
from kivy.lang import Builder


GUI = Builder.load_file("../telas/tela.kv")


class MeuAplicativo(App):
    def build(self):
        return GUI
    
MeuAplicativo().run()