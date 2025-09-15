from fastapi import HTTPException, status

class PetNotFoundException(HTTPException):
    def __init__(self, id: str):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pet com o id '{id}' não foi encontrado. Verifique o id ou a lista de todos os pets."
        )
