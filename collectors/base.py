"""
=========================================================
EZENOX Base Collector

All protocol collectors inherit from this class.

Author : Ezeduties
=========================================================
"""

from abc import ABC, abstractmethod


class BaseCollector(ABC):
    """
    Base class for all protocol collectors.
    """

    def __init__(self, timeout=3):
        self.timeout = timeout

    @abstractmethod
    def collect(self, host, port, service):
        """
        Collect evidence from a service.

        Parameters
        ----------
        host : str
        port : int
        service : str

        Returns
        -------
        Evidence | None
        """
        pass
