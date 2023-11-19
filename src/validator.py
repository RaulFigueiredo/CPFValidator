"""
This module provides functionalities for handling CPFs. It includes a class for
representing and cleaning CPFs, as well as a static class for CPF validation.

Classes:
    CPF: Represents a CPF number, offering functionalities for string cleaning.
    CPFValidator: Provides static methods for CPF number validation.
"""
import re


class CPF:
    """
    A class representing a CPF.

    Attributes:
        _cpf_clean (str): A cleaned version of the CPF string with non-digit characters removed.

    Methods:
        _clean_cpf(cpf): Static method to remove non-digit characters from a CPF string.
    """

    def __init__(self, cpf: str):
        """
        Initialize the CPF object with a CPF string.

        Args:
            cpf (str): A string representing a CPF number.
        """
        self._cpf_clean = self.clean_cpf(cpf)

    @staticmethod
    def clean_cpf(cpf: str) -> str:
        """
        Remove non-digit characters from a CPF string.

        Args:
            cpf (str): The CPF string to clean.

        Returns:
            str: The cleaned CPF string containing only digits.
        """
        return re.sub(r"\D", "", cpf)

    @property
    def cpf_clean(self) -> str:
        """
        Get the cleaned CPF string.

        Returns:
            str: The cleaned CPF string.
        """
        return self._cpf_clean


class CPFValidator:
    """
    A static class for validating CPF numbers.

    Methods:
        validate(cpf): Static method to validate a CPF number.
        _calculate_digit(cpf, num_digits): Helper static method to calculate a digit of 
                                           the CPF number.
    """

    @staticmethod
    def validate(cpf: str) -> bool:
        """
        Validate a CPF number.

        Args:
            cpf (str): The CPF number to validate.

        Returns:
            bool: True if the CPF is valid, False otherwise.
        """
        if len(cpf) != 11 or cpf == cpf[0] * len(cpf):
            return False
        return (CPFValidator.calculate_digit(cpf, 9) == int(cpf[9]) and
                CPFValidator.calculate_digit(cpf, 10) == int(cpf[10]))

    @staticmethod
    def calculate_digit(cpf, num_digits):
        """
        Calculate a digit of the CPF number.

        Args:
            cpf (str): The CPF number.
            num_digits (int): The number of digits to use in the calculation.

        Returns:
            int: The calculated digit.
        """
        sum_digits = sum(int(digit)*(num_digits+1-i) for i, digit in enumerate(cpf[:num_digits]))
        calculated_digit = (sum_digits * 10) % 11
        return 0 if calculated_digit == 10 else calculated_digit
