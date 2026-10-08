# Importando a biblioteca e nomeando de tk
import tkinter as tk
ALTURA = "450"
LARGURA = "400"

# Função temporária apenas para testar o clique por enquanto
def acao_clique():
  print("O botão foi clicado!")


#===================================
#1. Configuração da Janela Principal
#==================================
janela = tk.Tk()
janela.title("Gerador de Senhas Seguras")
janela.geometry(f"{LARGURA}x{ALTURA}")
janela.config(bg="#1e1e2e")

# 2. Título principal do aplicativo
titulo = tk.Label(
    text="Gerador de Senhas",
    font=("Arial",16,"bold"),
    bg="#1e1e2e",
    fg="#00ffcc"
)
titulo.pack(pady=20)

# 3. Label Tamanho Senha
lbl_tamanho_senha = tk.Label(
    text="Tamanho da Senha",
    font=("Arial",11),
    bg="#1e1e2e",
    fg="#ffffff"
)
lbl_tamanho_senha.pack(pady=12)

# 4. Entrada tamando da Senha
entry_tamanho_senha = tk.Entry(
    janela,
    font=("Arial",12),
    width=10,
    justify="center"
)
entry_tamanho_senha.pack(pady=5)

# 5. Criando as variáveis de controle True or False
var_maiusculas = tk.BooleanVar(value=True)
var_minusculas = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=False)
var_simbolos = tk.BooleanVar(value=False)

# 5. Criando as caixinhas de seleção
chk_maiuscula = tk.Checkbutton(
    janela,
    text="Maiúsculas (A-Z)",
    variable=var_maiusculas,
    bg="#1e1e2e",
    fg="#ffffff",
    selectcolor="#1e1e2e",
    activebackground="#1e1e2e",
    activeforeground="#ffffff"
)
chk_maiuscula.pack(anchor="w", padx=60,pady=2)

chk_minuscula = tk.Checkbutton(
    janela,
    text="Minúsculas (a-z)",
    variable=var_minusculas,
    bg="#1e1e2e",
    fg="#ffffff",
    selectcolor="#1e1e2e",
    activebackground="#1e1e2e",
    activeforeground="#ffffff"
)
chk_minuscula.pack(anchor="w", padx=60,pady=2)

chk_numeros = tk.Checkbutton(
    janela,
    text="Números (0-9)",
    variable=var_numeros,
    bg="#1e1e2e",
    fg="#ffffff",
    selectcolor="#1e1e2e",
    activebackground="#1e1e2e",
    activeforeground="#ffffff"
)
chk_numeros.pack(anchor="w", padx=60,pady=2)

chk_simbolos = tk.Checkbutton(
    janela,
    text="Caracteres Especiais (@#!*)",
    variable=var_simbolos,
    bg="#1e1e2e",
    fg="#ffffff",
    selectcolor="#1e1e2e",
    activebackground="#1e1e2e",
    activeforeground="#ffffff"
)
chk_simbolos.pack(anchor="w", padx=60,pady=2)

janela.mainloop()