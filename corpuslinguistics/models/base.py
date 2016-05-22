#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# -------------- Imports
import sqlite3
from hashlib import sha512

# -------------- Criação da tabela
def c_table():
	con = sqlite3.connect('base_usuarios.db')
	cur = con.cursor()
	cur.execute('CREATE TABLE IF NOT EXISTS USUARIOS(ID INTEGER PRIMARY KEY AUTOINCREMENT, NOME TEXT NOT NULL, EMAIL TEXT NOT NULL, SENHA TEXT NOT NULL);')

# ------------- Classe para interagir com os outros projetos
class Base:
	def __init__(self):

		# -------------- Cursor do banco
		self.con = sqlite3.connect('base_usuarios.db')
		self.cur = self.con.cursor()

        # -------------- Select
		self.select = 'SELECT ID,NOME,EMAIL FROM USUARIOS'

		# -------------- Select insert
		self.select_in = 'SELECT EMAIL FROM USUARIOS WHERE EMAIL=(?)'


        # -------------- Insert
		self.insert = 'INSERT INTO USUARIOS (NOME, EMAIL, SENHA) VALUES (?, ?, ?)'

	def busca_replicada(self,email):
		self.cur.execute(self.select_in, email)
		return self.cur.fetchall()

	def busca(self):
		self.cur.execute(self.select)
		return self.cur.fetchall()

    # -------------- Método que faz inserção no banco
	def inserir_dados(self, nome, email, senha):
		busca = self.busca_replicada((email,))

		if busca:
			return "Usuário já cadastrado"
		else: pass

		senha = sha512(senha.encode())
		self.cur.execute(self.insert, (nome, email, senha.hexdigest()))

	def commit(self):
		self.con.commit()

	def login(self, nome, senha):

		senha = sha512(senha.encode())
		senha = senha.hexdigest()
		result = self.cur.execute('SELECT * FROM USUARIOS WHERE NOME=?', (nome,))
		result = result.fetchall()

		try:
			assert senha == result[0][3]
			return result

		except IndexError:
			return 0
c_table()
