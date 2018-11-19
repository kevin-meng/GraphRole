from abc import ABC, abstractmethod
from typing import Iterable, Tuple, TypeVar, Union

import pandas as pd


Node = Union[int, str]
Edge = Tuple[Node, Node]


class BaseGraphInterface(ABC):

    """
    Abstract class to define the interface used to interact with various graph libraries
    """

    @abstractmethod
    def get_neighborhood_features(self) -> pd.DataFrame:
        """
        Return neighborhood features (local + egonet) for each node in the graph
        """
        pass
    
    @abstractmethod
    def get_nodes(self) -> Iterable[Node]:
        """
        Return iterable of nodes in the graph
        """
        pass

    @abstractmethod
    def get_neighbors(self, node: Node) -> Iterable[Node]:
        """
        Return iterable of neighbors of specified node
        """
        pass