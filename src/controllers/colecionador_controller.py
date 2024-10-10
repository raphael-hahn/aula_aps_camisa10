import os
import pickle
from models.colecionador import Colecionador
from views.colecionador_view import TelaColecionador


class ControladorColecionador:
    def __init__(self, arquivo='colecionadores.pkl'):
        self.__arquivo = arquivo
        self.__colecionadores = self.carregar_dados()
        self.__view = TelaColecionador()
        self.__colecionador_atual = None

    # Carregar os dados do pickle
    def carregar_dados(self):
        if os.path.exists(self.__arquivo):
            with open(self.__arquivo, 'rb') as f:
                return pickle.load(f)
        return []

    # Salvar os dados no arquivo pickle
    def salvar_dados(self):
        with open(self.__arquivo, 'wb') as f:
            pickle.dump(self.__colecionadores, f)

    # Cadastrar um novo colecionador
    def cadastrar_colecionador(self, novo_colecionador):
        self.__colecionadores.append(novo_colecionador)
        self.salvar_dados()

    # Verificar se um colecionador já existe
    def verificar_colecionador(self, username):
        for colecionador in self.__colecionadores:
            if colecionador.username == username:
                return True
        return False

    # Função para iniciar o cadastro
    def iniciar_cadastro(self):
        self.__view.cadastrar_colecionador(self.salvar_colecionador)

    ######## FAZER AS VERIFICAÇÕES DE CAMPO AQUI/CHAMAR A FUNÇÃO DE VERIFICAÇÃO #########
    # Função para salvar o colecionador a partir da view
    def salvar_colecionador(self, username, senha, nome, telefone, cidade, estado):
        if self.verificar_colecionador(username):
            self.__view.usuario_ja_existe(username)
        else:
            novo_colecionador = Colecionador(username, senha, nome, telefone, cidade, estado)
            self.__colecionador_atual = novo_colecionador
            self.cadastrar_colecionador(novo_colecionador)
            self.__view.janela.destroy()
            self.abrir_opcoes_cadastro(self.__colecionador_atual.username)

    # Função para excluir um colecionador
    def excluir_colecionador(self, username):
        for colecionador in self.__colecionadores:
            if colecionador.username == username:
                self.__colecionadores.remove(colecionador)
                self.__view.colecionador_excluido(username)
                self.salvar_dados()
                exit() 
                break

    # Função para salvar alterações do colecionador existente
    def salvar_edicao_colecionador(self, username, senha, nome, telefone, cidade, estado):
        if self.verificar_colecionador(username):
            self.__colecionador_atual.senha = senha
            self.__colecionador_atual.nome = nome
            self.__colecionador_atual.telefone = telefone
            self.__colecionador_atual.cidade = cidade
            self.__colecionador_atual.estado = estado
            
            # Atualizando as alterações no pikle
            self.atualizar_colecionador(username, senha, nome, telefone, cidade, estado)
            
            # Fechando a janela da edição
            self.__view.janela.destroy()
            
            # Abrir opções de cadastro novamente com os dados atualizados
            self.abrir_opcoes_cadastro(self.__colecionador_atual.username)

    # Função para atualizar os dados do colecionador
    def atualizar_colecionador(self, username, senha, nome, telefone, cidade, estado):
        for colecionador in self.__colecionadores:
            if colecionador.username == username:
                colecionador.senha = senha
                colecionador.nome = nome
                colecionador.telefone = telefone
                colecionador.cidade = cidade
                colecionador.estado = estado
                self.salvar_dados()
                break

    # Função para iniciar a edição do colecionador
    def iniciar_edicao(self, username, senha, nome, telefone, cidade, estado):
        self.__view.janela.destroy()
        self.__view.editar_colecionador({
            'username': username,
            'senha': senha,
            'nome': nome,
            'telefone': telefone,
            'cidade': cidade,
            'estado': estado
        }, self.salvar_edicao_colecionador)

    # Função para abrir as opções de cadastro
    def abrir_opcoes_cadastro(self, username):
        for colecionador in self.__colecionadores:
            if colecionador.username == username:
                self.__view.abrir_opcoes_cadastro(
                    colecionador.username,
                    colecionador.senha,
                    colecionador.nome,
                    colecionador.telefone,
                    colecionador.cidade,
                    colecionador.estado,
                    self.iniciar_edicao,
                    self.excluir_colecionador
                )
                break
