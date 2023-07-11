from dataclasses import dataclass

@dataclass
class Worker:
    name: str
    cpf: str
    rg:str
    password:str
    service: str