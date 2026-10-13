# Importando a biblioteca e nomeando de tk
import tkinter as tk
import random
import string

ALTURA = "450"
LARGURA = "400"

#===================================
# 7. FUNÇÕES DOS SISTEMA (A Lógica)
#===================================

def gerar_senha():
    try:
        tamanho = int(entry_tamanho_senha.get())
        # Verificando se a quantidade de caracteres definida é menor do que 4
        if tamanho < 4:
            lbl_resultado.config(
                text="Erro: Mínimo de 4 caracteres!",
                fg="#ff5555"
            )
            return

        caracteres = ""
        if var_maiusculas.get():
            caracteres += string.ascii_uppercase
        if var_minusculas.get():
            caracteres += string.ascii_lowercase
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation

        if not caracteres:
            lbl_resultado.config(
                text = "Erro: Selecione ao menos uma opção!",
                fg = "#ff5555"
            )
            return

        senha = "".join(random.choice(caracteres) for i in range(tamanho))

        lbl_resultado.config(
            text = f"Senha: {senha}",
            fg = "#50fa7b"
        )




    except ValueError:
        lbl_resultado.config(
            text = "Erro: Digite um número válido!",
            fg = "#ff5555"
            )

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

# 6. Criar botão gerador de senha
btn_gerar = tk.Button(
  janela,
  text="Gerar senha Segura",
  command=gerar_senha,
  bg="#00ffcc",
  fg="#1e1e2e",
  padx=10,
  pady=5
)
btn_gerar.pack(pady=15)

# Label que apresenta o resultado no programa
lbl_resultado = tk.Label(
    janela,
    text="A Senha aparecerá aqui",
    font=("Arial",11,"bold"),
    bg="#1e1e2e",
    fg="#f8f8f2"
)
lbl_resultado.pack(pady=5)

janela.mainloop()