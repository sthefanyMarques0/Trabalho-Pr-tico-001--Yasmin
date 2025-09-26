def calcular_media(alunos: List[Dict]) -> float:
    """Retorna a média das notas (0.0 se vazio)."""
    if not alunos:
        return 0.0
    return sum(a["nota"] for a in alunos)/len(alunos)