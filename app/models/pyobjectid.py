def curso_helper(curso) -> dict:
    return {
        "id": str(curso["_id"]),
        "titulo": curso["titulo"],
        "categoria": curso["categoria"],
        "instructor": curso["instructor"],
        "duracion_horas": curso["duracion_horas"],
        "activo": curso["activo"]
    }