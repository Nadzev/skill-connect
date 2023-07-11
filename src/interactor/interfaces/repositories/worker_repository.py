
from abc import ABC,abstractmethod
from src.domain.value_objects import WorkerID
from src.domain.entities.worker import Worker

class WorkerRepository(ABC):
    @abstractmethod
    def get(self,worker_id:WorkerID)-> Worker:
        """ Get a worker by id
        :param worker_id: worker's id
        :return: Worker
        """

    @abstractmethod
    def create(self,name:str, description:str)->Worker:
        pass


    
