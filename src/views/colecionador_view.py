from tkinter import *
from tkinter import messagebox

class TelaColecionador:
    def __init__(self):
        #self.__janela = None
        pass

    #@property
    #def janela(self):
     #   return self.__janela

    #@janela.setter
    #def janela(self, janela):
     #   self.__janela = janela

    def cadastrar_colecionador(self, salvar_callback):
        preto = "#000000"
        cinza = "#d9d9d9"
        verde = "#76a620"

        self.janela = Tk()
        self.janela.title('Cadastro')
        self.janela.geometry('600x400')
        self.janela.configure(background=cinza)
        self.janela.resizable(width=FALSE, height=FALSE)

        padding_y = 5

        # Função interna que coleta os dados e chama o callback do controlador
        def cadastrar():
            username = e_username.get()
            senha = e_senha.get()
            nome = e_nome.get()
            telefone = e_telefone.get()
            cidade = e_cidade.get()
            estado = e_estado.get()
            
            # Chama o controlador com os dados coletados
            salvar_callback(username, senha, nome, telefone, cidade, estado)

        # Configurações da interface gráfica
        frame_cima = Frame(self.janela, width=600, height=80, bg=cinza, relief='flat')
        frame_cima.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

        frame_baixo = Frame(self.janela, width=600, height=320, bg=cinza, relief='flat')
        frame_baixo.grid(row=1, column=0, pady=10, padx=20, sticky=NSEW)

        l_titulo = Label(frame_cima, text='CADASTRO', anchor=CENTER, font=('Arvo 24 bold'), bg=cinza, fg=preto)
        l_titulo.pack(pady=5)

        # Campos de entrada (labels e inputs)
        l_username = Label(frame_baixo, text='Username *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_username.grid(row=0, column=0, padx=10, pady=padding_y, sticky=W)
        e_username = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_username.grid(row=1, column=0, padx=10, pady=padding_y, sticky=W)

        l_senha = Label(frame_baixo, text='Senha *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_senha.grid(row=0, column=1, padx=10, pady=padding_y, sticky=W)
        e_senha = Entry(frame_baixo, width=23, show='*', font=("", 14), highlightthickness=1, relief='solid')
        e_senha.grid(row=1, column=1, padx=10, pady=padding_y, sticky=W)

        # Segunda linha
        l_nome = Label(frame_baixo, text='Nome *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_nome.grid(row=2, column=0, padx=10, pady=padding_y, sticky=W)
        e_nome = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_nome.grid(row=3, column=0, padx=10, pady=padding_y, sticky=W)

        l_telefone = Label(frame_baixo, text='Telefone *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_telefone.grid(row=2, column=1, padx=10, pady=padding_y, sticky=W)
        e_telefone = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_telefone.grid(row=3, column=1, padx=10, pady=padding_y, sticky=W)

        # Terceira linha
        l_cidade = Label(frame_baixo, text='Cidade *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_cidade.grid(row=4, column=0, padx=10, pady=padding_y, sticky=W)
        e_cidade = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_cidade.grid(row=5, column=0, padx=10, pady=padding_y, sticky=W)

        l_estado = Label(frame_baixo, text='Estado *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_estado.grid(row=4, column=1, padx=10, pady=padding_y, sticky=W)
        e_estado = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_estado.grid(row=5, column=1, padx=10, pady=padding_y, sticky=W)

        # Botão de confirmar
        b_confirmar = Button(frame_baixo, command=cadastrar, text='CADASTRAR', width=15, font=('Ivy 12 bold'),
                            bg=verde, fg=preto, relief=RAISED, overrelief=RIDGE)
        b_confirmar.grid(row=6, column=0, columnspan=2, pady=20)

        self.janela.mainloop()

    #Alerta que o usuário já existe
    def usuario_ja_existe(self, username):
        messagebox.showwarning("Aviso", f"Usuário {username} já cadastrado!")

    #Alerta que o colecionador foi excluído
    def colecionador_excluido(self, username):
        messagebox.showwarning("Aviso", f"Colecionador {username} excluído!")

    def abrir_opcoes_cadastro(self, username, senha, nome, telefone, cidade, estado, editar_callback, excluir_callback):
        self.janela = Tk()
        self.janela.title("Opções de Cadastro")
        self.janela.geometry('400x200')
        self.janela.configure(background="#d9d9d9")
        
        label = Label(self.janela, text=f"Bem-vindo, {nome}", font=('Arvo 16 bold'), bg="#d9d9d9", fg="#000000")
        label.pack(pady=10)
        
        # Botão para editar cadastro
        btn_editar = Button(self.janela, text="Editar Cadastro", font=('Ivy 12 bold'), command=lambda: editar_callback(username, senha, nome, telefone, cidade, estado))
        btn_editar.pack(pady=10)
        
        # Botão para excluir cadastro
        btn_excluir = Button(self.janela, text="Excluir Cadastro", font=('Ivy 12 bold'), command=lambda: excluir_callback(username))
        btn_excluir.pack(pady=10)
        
        self.janela.mainloop()

    def editar_colecionador(self, dados, salvar_callback):
        preto = "#000000"
        cinza = "#d9d9d9"
        verde = "#76a620"

        self.janela = Tk()
        self.janela.title('Cadastro')
        self.janela.geometry('600x400')
        self.janela.configure(background=cinza)
        self.janela.resizable(width=FALSE, height=FALSE)

        padding_y = 5

        # Configurações da interface gráfica
        frame_cima = Frame(self.janela, width=600, height=80, bg=cinza, relief='flat')
        frame_cima.grid(row=0, column=0, pady=10, padx=0, sticky=NSEW)

        frame_baixo = Frame(self.janela, width=600, height=320, bg=cinza, relief='flat')
        frame_baixo.grid(row=1, column=0, pady=10, padx=20, sticky=NSEW)

        l_titulo = Label(frame_cima, text='CADASTRO', anchor=CENTER, font=('Arvo 24 bold'), bg=cinza, fg=preto)
        l_titulo.pack(pady=5)

        # Campos de entrada (labels e inputs)
        l_username = Label(frame_baixo, text='Username *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_username.grid(row=0, column=0, padx=10, pady=padding_y, sticky=W)
        e_username = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_username.grid(row=1, column=0, padx=10, pady=padding_y, sticky=W)

        l_senha = Label(frame_baixo, text='Senha *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_senha.grid(row=0, column=1, padx=10, pady=padding_y, sticky=W)
        e_senha = Entry(frame_baixo, width=23, show='*', font=("", 14), highlightthickness=1, relief='solid')
        e_senha.grid(row=1, column=1, padx=10, pady=padding_y, sticky=W)

        # Segunda linha
        l_nome = Label(frame_baixo, text='Nome *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_nome.grid(row=2, column=0, padx=10, pady=padding_y, sticky=W)
        e_nome = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_nome.grid(row=3, column=0, padx=10, pady=padding_y, sticky=W)

        l_telefone = Label(frame_baixo, text='Telefone *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_telefone.grid(row=2, column=1, padx=10, pady=padding_y, sticky=W)
        e_telefone = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_telefone.grid(row=3, column=1, padx=10, pady=padding_y, sticky=W)

        # Terceira linha
        l_cidade = Label(frame_baixo, text='Cidade *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_cidade.grid(row=4, column=0, padx=10, pady=padding_y, sticky=W)
        e_cidade = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_cidade.grid(row=5, column=0, padx=10, pady=padding_y, sticky=W)

        l_estado = Label(frame_baixo, text='Estado *', font=('Ivy 12'), bg=cinza, fg=preto)
        l_estado.grid(row=4, column=1, padx=10, pady=padding_y, sticky=W)
        e_estado = Entry(frame_baixo, width=23, font=("", 14), highlightthickness=1, relief='solid')
        e_estado.grid(row=5, column=1, padx=10, pady=padding_y, sticky=W)

        # Preencher os campos com os dados
        e_username.insert(0, dados['username'])
        e_username.config(state='readonly')
        e_senha.insert(0, dados['senha'])
        e_nome.insert(0, dados['nome'])
        e_telefone.insert(0, dados['telefone'])
        e_cidade.insert(0, dados['cidade'])
        e_estado.insert(0, dados['estado'])

        # Botão de confirmar
        b_confirmar = Button(frame_baixo, command=lambda: salvar_callback(e_username.get(), e_senha.get(), e_nome.get(), e_telefone.get(), e_cidade.get(), e_estado.get()), text='CONFIRMAR', width=15, font=('Ivy 12 bold'),
                            bg=verde, fg=preto, relief=RAISED, overrelief=RIDGE)
        b_confirmar.grid(row=6, column=0, columnspan=2, pady=20)

        self.janela.mainloop()
