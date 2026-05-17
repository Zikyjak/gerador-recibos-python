"""
GERADOR DE RECIBOS
==================================
Instale:
pip install reportlab Pillow
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import date
from PIL import Image, ImageTk

from reportlab.lib.pagesizes import A5
from reportlab.platypus import (
    SimpleDocTemplate,
    Spacer,
    Paragraph,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm


# ==========================================
# CONFIGURAÇÕES DA EMPRESA
# ==========================================

EMPRESA = "SUA EMPRESA"
ENDERECO = "Seu endereço"
TELEFONE = "(00) 00000-0000"
CIDADE = "Sua cidade"
CNPJ = "00.000.000/0000-00"


# ==========================================
# CORES
# ==========================================

COR_BG = "#F4F4F8"
COR_CARD = "#FFFFFF"
COR_PRIMARIA = "#1A1A2E"
COR_DESTAQUE = "#E94560"
COR_TEXTO = "#2D2D2D"


# ==========================================
# FUNÇÃO GERAR PDF
# ==========================================

def gerar_pdf():

    cliente = entry_cliente.get()
    valor = entry_valor.get()
    descricao = txt_descricao.get("1.0", tk.END).strip()

    if not cliente or not valor:
        messagebox.showerror(
            "Erro",
            "Preencha os campos obrigatórios."
        )
        return

    caminho = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")]
    )

    if not caminho:
        return

    doc = SimpleDocTemplate(
        caminho,
        pagesize=A5,
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20
    )

    estilos = getSampleStyleSheet()
    elementos = []

    titulo = Paragraph(
        f"<b>{EMPRESA}</b>",
        estilos["Title"]
    )

    elementos.append(titulo)
    elementos.append(Spacer(1, 10))

    info_empresa = Paragraph(
        f"""
        {ENDERECO}<br/>
        {CIDADE}<br/>
        Tel: {TELEFONE}<br/>
        CNPJ: {CNPJ}
        """,
        estilos["BodyText"]
    )

    elementos.append(info_empresa)
    elementos.append(Spacer(1, 20))

    dados = [
        ["Cliente:", cliente],
        ["Valor:", f"R$ {valor}"],
        ["Data:", str(date.today())]
    ]

    tabela = Table(dados, colWidths=[60 * mm, 80 * mm])

    tabela.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    elementos.append(tabela)
    elementos.append(Spacer(1, 20))

    descricao_txt = Paragraph(
        f"<b>Descrição:</b><br/>{descricao}",
        estilos["BodyText"]
    )

    elementos.append(descricao_txt)

    doc.build(elementos)

    messagebox.showinfo(
        "Sucesso",
        "Recibo gerado com sucesso!"
    )


# ==========================================
# INTERFACE
# ==========================================

janela = tk.Tk()
janela.title("Gerador de Recibos")
janela.geometry("500x500")
janela.configure(bg=COR_BG)

frame = tk.Frame(
    janela,
    bg=COR_CARD,
    padx=20,
    pady=20
)

frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)

titulo = tk.Label(
    frame,
    text="GERADOR DE RECIBOS",
    font=("Arial", 18, "bold"),
    bg=COR_CARD,
    fg=COR_PRIMARIA
)

titulo.pack(pady=10)


# ==========================================
# CLIENTE
# ==========================================

tk.Label(
    frame,
    text="Cliente",
    bg=COR_CARD
).pack(anchor="w")

entry_cliente = tk.Entry(frame, width=40)
entry_cliente.pack(pady=5)


# ==========================================
# VALOR
# ==========================================

tk.Label(
    frame,
    text="Valor",
    bg=COR_CARD
).pack(anchor="w")

entry_valor = tk.Entry(frame, width=40)
entry_valor.pack(pady=5)


# ==========================================
# DESCRIÇÃO
# ==========================================

tk.Label(
    frame,
    text="Descrição",
    bg=COR_CARD
).pack(anchor="w")

txt_descricao = tk.Text(
    frame,
    width=40,
    height=8
)

txt_descricao.pack(pady=5)


# ==========================================
# BOTÃO
# ==========================================

btn_gerar = tk.Button(
    frame,
    text="GERAR PDF",
    bg=COR_DESTAQUE,
    fg="white",
    font=("Arial", 12, "bold"),
    command=gerar_pdf
)

btn_gerar.pack(pady=20)


janela.mainloop()
