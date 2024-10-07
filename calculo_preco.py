import tkinter as tk
from tkinter import ttk, messagebox
import sys

# Adicionando o diretório do tema ao sys.path
sys.path.append(r'C:\py\Azure-ttk-theme-main')

from ttkbootstrap import Style

# Definindo a margem padrão
MARGEM_PADRAO = 45.0

def calcular_preco_venda():
    try:
        # Recupera os dados dos campos de entrada
        nome_item = entry_nome_item.get()
        custo_total = float(entry_valor_item.get())
        
        # Usar a margem alterada ou padrão
        if entry_taxa.get():
            margem_lucro = float(entry_taxa.get())
        else:
            margem_lucro = MARGEM_PADRAO
        
        # Usando a fórmula para calcular o preço de venda
        preco_venda = custo_total / (1 - (margem_lucro / 100))
        
        # Adiciona o resultado à lista de resultados
        resultado_texto = f"{nome_item}: R$ {preco_venda:.2f}"
        listbox_resultados.insert(tk.END, resultado_texto)
        
        # Limpa os campos de entrada após calcular
        entry_nome_item.delete(0, tk.END)
        entry_valor_item.delete(0, tk.END)
        entry_taxa.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

def alternar_tema():
    global tema_atual
    if tema_atual == 'light':
        style.theme_use('darkly')
        tema_atual = 'dark'
    else:
        style.theme_use('flatly')
        tema_atual = 'light'

# Criando a janela principal
root = tk.Tk()
root.title("Calculadora de Preço de Venda")
root.geometry("600x700")  # Ajustei o tamanho inicial
root.resizable(True, True)  # Janela ajustável

# Inicializando o estilo
style = Style(theme='flatly')
tema_atual = 'light'

# Criando um frame principal para centralizar e ajustar o layout
frame_principal = ttk.Frame(root, padding="20")
frame_principal.pack(fill=tk.BOTH, expand=True)

# Scrollbar que controla a janela inteira
canvas = tk.Canvas(frame_principal)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_principal, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Estilos personalizados
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12), padding=5)

# Título
label_titulo = ttk.Label(scrollable_frame, text="Calculadora de Preço de Venda", font=('Helvetica', 16, 'bold'))
label_titulo.pack(pady=10)

# Campo para o nome do item
label_nome_item = ttk.Label(scrollable_frame, text="Nome do Item:")
label_nome_item.pack(pady=(10, 2))
entry_nome_item = ttk.Entry(scrollable_frame, width=40)
entry_nome_item.pack(pady=5)

# Campo para o custo do item
label_valor_item = ttk.Label(scrollable_frame, text="Custo Total:")
label_valor_item.pack(pady=(10, 2))
entry_valor_item = ttk.Entry(scrollable_frame, width=40)
entry_valor_item.pack(pady=5)

# Campo para a margem de lucro (com 45% como padrão)
label_taxa = ttk.Label(scrollable_frame, text="Margem de Lucro (%): (Padrão: 45%)")
label_taxa.pack(pady=(10, 2))
entry_taxa = ttk.Entry(scrollable_frame, width=40)
entry_taxa.insert(0, str(MARGEM_PADRAO))  # Define o valor padrão no campo
entry_taxa.pack(pady=5)

# Botão para calcular preço de venda
botao_calcular = ttk.Button(scrollable_frame, text="Calcular Preço de Venda", command=calcular_preco_venda)
botao_calcular.pack(pady=(15, 10))

# Listbox para mostrar resultados com scrollbar dedicado
listbox_resultados = tk.Listbox(scrollable_frame, width=50, height=10)
listbox_resultados.pack(pady=(10, 5))

# Botão para copiar resultados
def copiar_resultados():
    resultados = listbox_resultados.get(0, tk.END)
    if resultados:
        resultado_texto = "\n".join(resultados)
        root.clipboard_clear()  # Limpa a área de transferência
        root.clipboard_append(resultado_texto)  # Adiciona os resultados à área de transferência
        messagebox.showinfo("Sucesso", "Resultados copiados para a área de transferência!")
    else:
        messagebox.showwarning("Aviso", "Não há resultados para copiar.")

botao_copiar = ttk.Button(scrollable_frame, text="Copiar Resultados", command=copiar_resultados)
botao_copiar.pack(pady=(10, 10))

# Botão para alternar tema
botao_alternar_tema = ttk.Button(scrollable_frame, text="Alternar Tema", command=alternar_tema)
botao_alternar_tema.pack(pady=(10, 10))

# Iniciando a aplicação
root.mainloop()
