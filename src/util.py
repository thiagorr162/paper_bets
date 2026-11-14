"""Funções pequenas usadas por todos os notebooks: números no padrão brasileiro e figuras e tabelas no formato da
CSP, gravadas em ../artigo/.

Normas da CSP aplicadas aqui (ver ../csp_normas_formato.md):
- figuras: PNG com 300 dpi para a submissão, e SVG/EPS (vetor gerado pelo código) para depois do aceite; sem título
  na imagem (título e legenda vão em arquivo separado); largura de até 17 cm; em gráficos de linha, as séries se
  diferenciam só pela cor (nada de tracejado ou marcador);
- tabelas: até 17 cm, Times New Roman 9, um dado por célula (sem células mescladas), n e % em colunas separadas.
"""

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from src.config import ARTIGO

# ------------------------------------------------------------------ números
MESES = "jan fev mar abr mai jun jul ago set out nov dez".split()


def br(x, casas=1):
    """1234.5 -> '1.234,5'"""
    s = f"{x:,.{casas}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def nome_mes(cmp):
    """'202606' -> 'jun/2026'"""
    return f"{MESES[int(cmp[4:]) - 1]}/{cmp[:4]}"


def mes_idx(cmp):
    """'AAAAMM' -> meses desde jan/2018 (jan/2018 = 0)."""
    return (int(cmp[:4]) - 2018) * 12 + int(cmp[4:]) - 1


# ------------------------------------------------------------------ figuras
CM = 1 / 2.54
LARGURA = 17 * CM
COR = {"aps": "#0072B2", "caps": "#D55E00", "aps_claro": "#A9CCE6", "caps_claro": "#F2C1A3",
       "controle_aps": "#56B4E9", "controle_caps": "#E69F00", "ref": "#8C8C8C", "trends": "#009E73"}  # Okabe-Ito

plt.rcParams.update({
    "font.family": "serif", "font.serif": ["Times New Roman", "Liberation Serif", "TeX Gyre Termes", "DejaVu Serif"],
    "font.size": 9, "xtick.labelsize": 8, "ytick.labelsize": 8, "legend.fontsize": 8,
    "axes.spines.top": False, "axes.spines.right": False, "axes.linewidth": 0.6, "lines.linewidth": 1.2,
    "legend.frameon": False, "svg.fonttype": "none", "ps.fonttype": 42, "pdf.fonttype": 42,
    "savefig.bbox": "tight", "savefig.pad_inches": 0.03,
})

eixo_br = FuncFormatter(lambda v, _: br(v, 0) if float(v).is_integer() else br(v, 1))


def salvar_figura(fig, nome):
    """Grava ../artigo/figuras/<nome>.png (300 dpi, RGB com fundo branco), .svg e .eps (vetor, para depois do aceite)."""
    from PIL import Image

    pasta = ARTIGO / "figuras"
    pasta.mkdir(parents=True, exist_ok=True)
    for ext in ("png", "svg", "eps"):
        fig.savefig(pasta / f"{nome}.{ext}", dpi=300 if ext == "png" else None, facecolor="white")
    png = pasta / f"{nome}.png"
    Image.open(png).convert("RGB").save(png, dpi=(300, 300))  # sem canal de transparência


# ------------------------------------------------------------------ tabelas
def _esc(s):
    return str(s).replace("%", r"\%").replace("&", r"\&")


def tabela_tex(nome, titulo, cabecalho, linhas, nota, alinhamento):
    """Grava ../artigo/tabelas/<nome>.tex: título acima, notas abaixo, fonte de 9 pt, sem células mescladas.
    `alinhamento` pode usar R{largura}: coluna alinhada à direita com quebra de linha (definida no main.tex)."""
    corpo = [" & ".join(_esc(c) for c in cabecalho) + r" \\ \midrule"]
    corpo += [" & ".join(_esc(c) for c in linha) + r" \\" for linha in linhas]
    tex = "\n".join([
        r"\begin{table}[!htbp]", r"\centering", r"\fontsize{9}{11}\selectfont", r"\setlength{\tabcolsep}{4pt}",
        rf"\caption{{{_esc(titulo)}}}", rf"\label{{tab:{nome}}}",
        rf"\begin{{tabular}}{{{alinhamento}}}", r"\toprule", *corpo, r"\bottomrule", r"\end{tabular}",
        r"\par\smallskip\parbox{\linewidth}{\raggedright " + _esc(nota) + "}", r"\end{table}", ""])
    pasta = ARTIGO / "tabelas"
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / f"{nome}.tex").write_text(tex)
