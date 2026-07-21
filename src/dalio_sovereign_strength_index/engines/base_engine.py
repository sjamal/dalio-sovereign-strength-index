"""
Abstract Base Layer for Analytical Data Acquisition Engines.
Guarantees consistent data shapes across various alternative economic platforms.
"""
from abc import ABC, abstractmethod
import pandas as pd

class BaseDataEngine(ABC):
    @abstractmethod
    def fetch_data(self, start_yr: int, end_yr: int) -> pd.DataFrame:
        """
        Must return a structured DataFrame with exactly these index columns:
        ['year', 'Country'] along with domain-specific metrics.
        """
        pass
