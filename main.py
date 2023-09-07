import customtkinter as ctk
from PIL import Image
from validador_cpf import validar_padrao_cpf
from gerador_cpf import gerar_cpf
from tkinter import StringVar
cores = {
    'botoes_hover': '#656469',
    'fg_botao': 'transparent',
    'cor_texto_botao': '#c5c5c7',
    'cor_borda_evento': '#25b2c2',
    'text_label': '#c5c5c7',
    'cor_frames': '#616366'
}

class TelaCpf:
    def __init__(self):
        self.root = ctk.CTk()
        self.config_root_inicial()
        self.widgts_tela()

        self.root.mainloop()

    def config_root_inicial(self):
        largura = 900
        altura = 600
        systema_largura = self.root.winfo_screenwidth()
        systema_altura = self.root.winfo_screenheight()
        x = systema_largura/2 - largura/2
        y = systema_altura/2 - altura/2
        self.root.geometry('%dx%d+%d+%d' % (largura,altura,x,y))
        self.root.title("Gerador e Validador de CPF")
        self.root._set_appearance_mode('System')
        self.root.resizable(False,False)
        self.root.iconbitmap('./assets/img/gestao.ico')
   
    def widgts_tela(self):
        self.frame_lateral = ctk.CTkFrame(self.root,width=150,height=600,corner_radius=0,fg_color=cores['cor_frames'])
        self.frame_lateral.place(relx=0.0,rely=0.0)

        img_gerar = ctk.CTkImage(light_image=Image.open("./assets/img/gerar_black.png"),dark_image=Image.open("./assets/img/gerenciar.png"),size=(34,34))
        self.botao_gerar = ctk.CTkButton(self.frame_lateral,command=self.frame_gerar_cpf,text='Gerar CPF',image=img_gerar,fg_color=cores['fg_botao'],hover=False,text_color=cores['cor_texto_botao'],border_width=1,border_color=cores['botoes_hover'])
        self.botao_gerar.place(relx=0.08,rely=0.20,relwidth=0.8,relheight=0.1)
        self.botao_gerar.bind('<Enter>',self.evento_cor_borda_botao)
        self.botao_gerar.bind('<Leave>',self.evento_cor_borda_botao_off)

        img_validar = ctk.CTkImage(light_image=Image.open("./assets/img/validar_black.png"),dark_image=Image.open("./assets/img/validar.png"),size=(34,34))
        self.botao_validar = ctk.CTkButton(self.frame_lateral,text='Validar CPF',image=img_validar,fg_color=cores['fg_botao'],hover=False,text_color=cores['cor_texto_botao'],border_width=1,border_color=cores['botoes_hover'],command=self.frame_validar)
        self.botao_validar.place(relx=0.08,rely=0.32,relwidth=0.8,relheight=0.1)
        self.botao_validar.bind('<Enter>',self.evento_cor_borda_botao_validar)
        self.botao_validar.bind('<Leave>',self.evento_cor_borda_botao_off_validar)

        img_logo = ctk.CTkImage(light_image=Image.open("./assets/img/logo_system.png"),dark_image=Image.open("./assets/img/logo_system.png"),size=(70,70))
        label = ctk.CTkLabel(self.frame_lateral,text='',image=img_logo,width=100,height=100)
        label.place(relx=0.20,rely=0.0)
    def frame_validar(self):
        self.frame_validacao = ctk.CTkFrame(self.root,width=600,height=400,fg_color=cores['cor_frames'])
        self.frame_validacao.place(relx=0.24,rely=0.15)
        # frame entry
        self.frame_entry = ctk.CTkFrame(self.frame_validacao,width=600,height=80,corner_radius=0,fg_color=cores['cor_frames'])
        self.frame_entry.place(relx=0.0,rely=0.0)
        #entry
        self.entry_cpf = ctk.CTkEntry(self.frame_entry,width=250,height=40,placeholder_text='CPF',font=('helvetica',18,'italic'))
        self.entry_cpf.place(relx=0.06,rely=0.3) 

        img_validar_confi = ctk.CTkImage(light_image=Image.open("./assets/img/confirmar.png"),dark_image=Image.open("./assets/img/confirmar.png"),size=(15,15))
        self.botao_confirmar = ctk.CTkButton(self.frame_entry,text='Confirmar',image=img_validar_confi,fg_color=cores['fg_botao'],hover=False,text_color=cores['cor_texto_botao'],border_width=1,border_color=cores['botoes_hover'],command=self.chamando_funcao_validar)
        self.botao_confirmar.place(relx=0.5,rely=0.3,relwidth=0.16,relheight=0.5)
        self.botao_confirmar.bind('<Enter>',self.evento_cor_borda_botao_confirmar)
        self.botao_confirmar.bind('<Leave>',self.evento_cor_borda_botao_off_confirmar)
        # label
        self.text_variavel_cpf = StringVar()
        self.text_variavel_msg = StringVar()
        self.label = ctk.CTkLabel(self.frame_validacao,textvariable=self.text_variavel_cpf,text_color=cores['text_label'],width=300,height=100,font=('helvetica',25,'italic'))
        self.label.place(relx=0.25,rely=0.35)
        self.label_msg = ctk.CTkLabel(self.frame_validacao,textvariable=self.text_variavel_msg,text_color=cores['text_label'],width=300,height=80,font=('helvetica',25,'italic'))
        self.label_msg.place(relx=0.25,rely=0.55)
    def chamando_funcao_validar(self):
        cpf_entry = self.entry_cpf.get()
        cpf,msg = validar_padrao_cpf(cpf_entry)
        if msg == 'CPF INVALIDO':
            self.text_variavel_cpf.set(f'{cpf_entry[:3]}.{cpf_entry[3:6]}.{cpf_entry[6:9]}-{cpf_entry[9:]}')
        else:
            self.text_variavel_cpf.set(f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')
        self.text_variavel_msg.set(msg)
    def frame_gerar_cpf(self):
        self.frame_gerador = ctk.CTkFrame(self.root,width=600,height=400,fg_color=cores['cor_frames'])
        self.frame_gerador.place(relx=0.24,rely=0.15) 
        self.text_box = ctk.CTkTextbox(self.frame_gerador,text_color=cores['cor_texto_botao'],fg_color=cores['cor_frames'],border_spacing=50,width=400,height=100,font=('helvetica',30,'italic'))
        self.text_box.place(relx=0.25,rely=0.35)
        img_validar_confi = ctk.CTkImage(light_image=Image.open("./assets/img/gerir.png"),dark_image=Image.open("./assets/img/gerir.png"),size=(40,40))
        self.botao_gerador_cpf = ctk.CTkButton(self.frame_gerador,text='GERAR CPF',image=img_validar_confi,fg_color=cores['fg_botao'],hover=False,text_color=cores['cor_texto_botao'],border_width=1,border_color=cores['botoes_hover'],command=self.chamando_funcao_gerar)
        self.botao_gerador_cpf.place(relx=0.72,rely=0.85,relwidth=0.25,relheight=0.11)
        self.botao_gerador_cpf.bind('<Enter>',self.evento_cor_borda_botao_gerador_cpf)
        self.botao_gerador_cpf.bind('<Leave>',self.evento_cor_borda_botao_off_gerador_cpf)
    def chamando_funcao_gerar(self):
        cpf_gerado = gerar_cpf()
        self.text_box.delete('0.0','end')
        self.text_box.insert('0.0',cpf_gerado)

    # EVENTOS    
    def evento_cor_borda_botao(self,event):
        self.botao_gerar.configure(border_color=cores['cor_borda_evento']) 
    def evento_cor_borda_botao_off(self,event):
        self.botao_gerar.configure(border_color=cores['botoes_hover'])
    def evento_cor_borda_botao_validar(self,event):
        self.botao_validar.configure(border_color=cores['cor_borda_evento']) 
    def evento_cor_borda_botao_off_validar(self,event):
        self.botao_validar.configure(border_color=cores['botoes_hover'])
    def evento_cor_borda_botao_confirmar(self,event):
        self.botao_confirmar.configure(border_color=cores['cor_borda_evento']) 
    def evento_cor_borda_botao_off_confirmar(self,event):
        self.botao_confirmar.configure(border_color=cores['botoes_hover'])   
    def evento_cor_borda_botao_gerador_cpf(self,event):
        self.botao_gerador_cpf.configure(border_color=cores['cor_borda_evento']) 
    def evento_cor_borda_botao_off_gerador_cpf(self,event):
        self.botao_gerador_cpf.configure(border_color=cores['botoes_hover']) 

app = TelaCpf()


        