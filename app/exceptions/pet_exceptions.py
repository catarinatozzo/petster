from fastapi import HTTPException, status

class PetNotFoundException(HTTPException):
    def __init__(self, detail: str = None):
        message = "Nenhum pet encontrado" if not detail else f"Pet com o id '{detail}' não foi encontrado. Verifique o id ou os filtros aplicados."
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=message
        )