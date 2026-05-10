# Importa todas as chamadas do tKinter
from tkinter import * 
from tkinter import ttk
import sqlite3

# Janela do sistema
root = Tk()

class Funcs():
    def limpar_cliente(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.fone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def conecta_db(self):
        self.conn = sqlite3.connect('clientes.db')
        self.cursor = self.conn.cursor(); print('Conectando ao banco de dados')

    def desconecta_db(self):
        self.conn.close(); print('Desconectando do Banco de dados')

    def montaTabelas(self):
        self.conecta_db(); print('Conectando banco de dados (tabela)')
        ### Criando tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
            );
        """)
        self.conn.commit(); print('Banco de dados criado')
        self.desconecta_db()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.conecta_db()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
                            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_cliente()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
                                    ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.desconecta_db()

    def OnDoubleClick(self, event):
        self.limpar_cliente()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.fone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod = ? """, (self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.limpar_cliente()
        self.select_lista()

    def altera_cliente(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute(""" UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
            WHERE cod = ? """, (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_db()
        self.select_lista()
        self.limpar_cliente()

    def busca_cliente(self):
        self.conecta_db()
        self.listaCli.delete(*self.listaCli.get_children())

        self.nome_entry.insert(END, '%')
        nome = self.nome_entry.get()
        self.cursor.execute(
            """ SELECT cod, nome_cliente, telefone, cidade FROM clientes
             WHERE nome_cliente LIKE '%s' ORDER BY nome_cliente ASC""" % nome)
        buscanomeCli = self.cursor.fetchall()
        for i in buscanomeCli:
            self.listaCli.insert("", END, values= i)
        self.limpar_cliente()
        self.desconecta_db()

class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.Menus()

        # cria um loop que faz com que a tela apareça
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes') # Titulo da tela
        self.root.configure(background= "#27A7A7") # Cor de fundo da tela
        self.root.geometry('900x700') # Define um tamanho para a tela
        self.root.resizable(True, True) # Indica se a tela é responsiva de algum dos lados
        self.root.maxsize(width= 900, height= 700) # Indica o quanto a tela pode expandir
        self.root.minsize(width= 500, height= 400) # Indica quanto a tela pode minimizar

    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg= "#EDEDF7",
                              highlightbackground= "#C4C4C4", highlightthickness= 2)
       # place, pack, grid, relx, rely
        self.frame_1.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.46)

        self.frame_2 = Frame(self.root, bd= 4, bg= "#BABABA",
                              highlightbackground= "#E9E9E9", highlightthickness= 2)
        self.frame_2.place(relx= 0.02, rely= 0.5, relwidth= 0.96, relheight= 0.46)

    def widgets_frame1(self):
        ### Criação do botao limpar
        self.bt_limpar = Button(self.frame_1, text= 'Limpar', bd= 2, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'), command= self.limpar_cliente)
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

         ### Criação do botao buscar
        self.bt_buscar = Button(self.frame_1, text= 'Buscar', bd= 3, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'), command= self.busca_cliente)
        self.bt_buscar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao novo
        self.bt_novo = Button(self.frame_1, text= 'Novo', bd= 2, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'), command= self.add_cliente)
        self.bt_novo.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao alterar
        self.bt_alterar = Button(self.frame_1, text= 'Alterar', bd= 2, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'), command= self.altera_cliente)
        self.bt_alterar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao apagar
        self.bt_apagar = Button(self.frame_1, text= 'Apagar', bd= 3, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'), command= self.deleta_cliente)
        self.bt_apagar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ## Criação da label e entrada do codigo
        self.lb_codigo = Label(self.frame_1, text = 'Código', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_codigo.place(relx= 0.05, rely= 0.05 )

        self.codigo_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.codigo_entry.place(relx= 0.05, rely= 0.15, relwidth= 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = 'Nome', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_nome.place(relx= 0.05, rely= 0.35 )

        self.nome_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.nome_entry.place(relx= 0.05, rely= 0.45, relwidth= 0.85)

        ## Criação da label e entrada do telefone
        self.lb_fone = Label(self.frame_1, text = 'Telefone', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_fone.place(relx= 0.05, rely= 0.6 )

        self.fone_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.fone_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        ## Criação da label e entrada do cidade
        self.lb_cidade = Label(self.frame_1, text = 'Cídade', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_cidade.place(relx= 0.5, rely= 0.6 )

        self.cidade_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.cidade_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(self.frame_2, height= 3, columns= ('col1', "col2", "col3", "col4"))
        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Codigo")
        self.listaCli.heading("#2", text="Nome")
        self.listaCli.heading("#3", text="Telefone")
        self.listaCli.heading("#4", text="Cidade")

        self.listaCli.column("#0", width= 1)
        self.listaCli.column("#1", width= 50)
        self.listaCli.column("#2", width= 200)
        self.listaCli.column("#1", width= 125)
        self.listaCli.column("#1", width= 125)

        self.listaCli.place(relx=0.01, rely=0.08, relwidth=0.95, relheight= 0.85)

        ## Barra de rolagem
        self.scroolLista = Scrollbar(self.frame_2, orient= 'vertical')
        self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx= 0.97, rely= 0.08, relwidth= 0.02, relheight= 0.85)
        self.listaCli.bind("<Double-1>", self.OnDoubleClick)

    def Menus(self):
        menubar = Menu(self.root)
        self.root.config(menu= menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def Quit(): self.root.destroy()
        
        menubar.add_cascade(label= "Opções", menu= filemenu)
        menubar.add_cascade(label= "Relatorios", menu= filemenu2)

        filemenu.add_command(label= "Sair", command= Quit)
        filemenu.add_command(label= "limpa Cliente", command= self.limpar_cliente)

Application()
