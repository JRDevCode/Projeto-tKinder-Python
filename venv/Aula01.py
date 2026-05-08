# Importa todas as chamadas do tKinter
from tkinter import * 
from tkinter import ttk

# Janela do sistema
root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()

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
                                ,font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.2, rely= 0.1, relwidth= 0.1, relheight= 0.15)

         ### Criação do botao buscar
        self.bt_limpar = Button(self.frame_1, text= 'Buscar', bd= 3, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.3, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao novo
        self.bt_limpar = Button(self.frame_1, text= 'Novo', bd= 2, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.6, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao alterar
        self.bt_limpar = Button(self.frame_1, text= 'Alterar', bd= 2, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.7, rely= 0.1, relwidth= 0.1, relheight= 0.15)

        ### Criação do botao apagar
        self.bt_limpar = Button(self.frame_1, text= 'Apagar', bd= 3, bg= "#2aa5ec", fg= "#FFFFFF"
                                ,font= ('verdana', 8, 'bold'))
        self.bt_limpar.place(relx= 0.8, rely= 0.1, relwidth= 0.1, relheight= 0.15)

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
        self.lb_codigo = Label(self.frame_1, text = 'Telefone', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_codigo.place(relx= 0.05, rely= 0.6 )

        self.codigo_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.codigo_entry.place(relx= 0.05, rely= 0.7, relwidth= 0.4)

        ## Criação da label e entrada do cidade
        self.lb_codigo = Label(self.frame_1, text = 'Cídade', bg= "#EDEDF7", fg= "#2aa5ec")
        self.lb_codigo.place(relx= 0.5, rely= 0.6 )

        self.codigo_entry = Entry(self.frame_1, bg= "#EAF8FE")
        self.codigo_entry.place(relx= 0.5, rely= 0.7, relwidth= 0.4)

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

Application()
