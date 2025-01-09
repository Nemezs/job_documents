from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HomeProcuracaoPFScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeProcuracaoPFScreen, self).__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)

        # Adiciona um título à tela inicial
        titulo = Label(
            text="Tipos de procuração",
            font_size=30,
            size_hint=(None, None),
            size=(200, 50),
            pos_hint={"center_x": 0.5, "center_y": 0.3}  # Centraliza o título
        )
        layout.add_widget(titulo)

        # Campo clicável para navegar até a tela de Procuracao
        btn_procuracao = Button(
            text="Ir para Procuração Criminal",
            size_hint=(None, None),
            size=(230, 50),
            pos_hint={"center_x": 0.5, "top": 0.6},  # Ajuste na posição do botão
            on_press=self.ir_para_procuracao_cmn
        )
        layout.add_widget(btn_procuracao)

        # Campo clicável para navegar até a tela de Processo
        btn_processo = Button(
            text="Ir para Procuração Queixa Crime",
            size_hint=(None, None),
            size=(230, 50),
            pos_hint={"center_x": 0.5, "top": 0.4},  # Ajuste na posição do botão
            on_press=self.ir_para_procuracao_qc
        )
        layout.add_widget(btn_processo)
        
        btn_voltar = Button(
            text="<",
            size_hint=(None, None),
            size= (50,50),
            pos_hint={"center_x": 0.1, "center_y": 0.1},
            on_press=self.voltar
        )
        
        layout.add_widget(btn_voltar)

        # Adiciona o layout à tela
        self.add_widget(layout)
        
    def voltar(self, instance):
        
        self.manager.current = "home_procuracao_screen"

    def ir_para_procuracao_qc(self, instance):
        """
        Função para ir até a tela de ProcuracaoScreen
        """
        self.manager.current = "procuracao_screen_queixa_crime_PF"
        
    def ir_para_procuracao_cmn(self, instance):
        """
        Função para ir até a tela de ProcessoScreen
        """
        self.manager.current = "procuracao_criminal_screen_PF"
