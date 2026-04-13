from abc import ABC, abstractmethod


class HealCapability(ABC):
    
    @abstractmethod
    def heal(self, target: str = "itself") -> str:
        """
        Abstract method for healing.
        Takes an optional 'target' parameter.
        """
        pass


class TransformCapability(ABC):
    
    def __init__(self) -> None:
        """Initialize the persistent state attribute."""
        self.is_transformed: bool = False
        
    @abstractmethod
    def transform(self) -> str:
        """Abstract method to apply the transformation."""
        pass
        
    @abstractmethod
    def revert(self) -> str:
        """Abstract method to revert the transformation."""
        pass
