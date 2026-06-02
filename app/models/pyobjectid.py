def curso_helper(curso) -> dict:
    return {
        "id": str(curso["_id"]),
        "titulo": curso["titulo"],
        "categoria": curso["categoria"],
        "instructor": curso["instructor"],
        "duracion_horas": curso["duracion_horas"],
        "activo": curso["activo"]
    }


def estudiante_helper(estudiante) -> dict:
    return {
        "id": str(estudiante["_id"]),
        "nombre": estudiante["nombre"],
        "email": estudiante["email"],
        "telefono": estudiante.get("telefono"),
        "fecha_registro": estudiante["fecha_registro"]
    }


def inscripcion_helper(inscripcion) -> dict:
    return {
        "id": str(inscripcion["_id"]),
        "estudiante_id": inscripcion["estudiante_id"],
        "curso_id": inscripcion["curso_id"],
        "fecha_inscripcion": inscripcion["fecha_inscripcion"]
    }
