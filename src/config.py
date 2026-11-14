"""Caminhos, períodos e definições usados em todos os notebooks do artigo."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"  # tabelas de entrada (fora do git)
ARTIGO = ROOT.parent / "artigo"  # repositório do Overleaf: recebe as figuras e as tabelas

# Supressão: contagens publicadas abaixo de MIN viram vazio (LGPD; mesmo critério do site)
MIN = 5

# Período do estudo
INICIO = "201801"
FIM_APS = "202609"  # como no site: até set/2026
FIM_CAPS = "202606"  # como no site: jul–ago/2026 descartados (os CAPS ainda estão enviando a produção)
FIM_TRENDS = "202610"  # como no site: nov/2026 é parcial

PANDEMIA = ("202003", "202112")
CPI = ("202411", "202506")  # CPI das Bets no Senado: 12/11/2024 a 12/06/2025


# Atenção primária (SISAB): grupos de diagnóstico (CID-10)
APS_JOGO = ["jogo_cid"]  # F63.0
APS_CONTROLE = ["piromania_cid", "cleptomania_cid", "tricotilomania_cid"]  # F63.1–F63.3
APS_REF = ["depressao_cid", "depressao_rec_cid", "ansiedade_cid", "estresse_cid", "alcool_cid", "esquizofrenia_cid"]
# F32, F33, F41, F43, F10, F20

# CAPS (SIA-PS/RAAS)
CAPS_JOGO = ["F630"]
CAPS_CONTROLE = ["F631", "F632", "F633"]

FAIXAS = ["0-17", "18-24", "25-34", "35-44", "45-59", "60+"]
