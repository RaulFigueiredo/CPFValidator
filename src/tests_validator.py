"""
This module contains unittests for the CPF and CPFValidator classes defined in the 'validator' 
module.

It includes tests for validating CPF numbers in various formats and scenarios, covering both 
valid and invalid CPF numbers. The tests check the functionality of the CPFValidator in 
different cases like standard formatted CPFs, CPFs with irregular formatting, and CPFs with 
invalid data.
"""

import unittest
from validator import CPF, CPFValidator


class TestCPFValidator(unittest.TestCase):
    """
    Test suite for the CPFValidator class.

    This suite includes tests for validating CPF numbers, both in standard and irregular formats,
    covering cases for valid and invalid CPF numbers.
    """

    def test_valid_cpf(self):
        """
        Test the validation of standard format valid CPFs.

        This test checks if CPFs known to be valid are correctly validated by the CPFValidator
        when provided in a standard format with separators (e.g., '123.456.789-09').
        """
        valid_cpfs = ['123.456.789-09', '987.654.321-00','576.354.100-67']
        for each_cpf in valid_cpfs:
            self.assertTrue(CPFValidator.validate(CPF(each_cpf).cpf_clean))

    def test_invalid_cpf(self):
        """
        Test the validation of standard format invalid CPFs.

        This test checks if CPFs known to be invalid are correctly identified as invalid by the 
        CPFValidator when provided in a standard format with separators.
        """
        invalid_cpfs = ['111.111.111-11', '576.354.10-67', '123.456.784-190', 'abc.def.ghi-jk']
        for each_cpf in invalid_cpfs:
            self.assertFalse(CPFValidator.validate(CPF(each_cpf).cpf_clean))

    def test_valid_cpf_with_irregular_format(self):
        """
        Test the validation of irregular format valid CPFs.

        This test checks if CPFs known to be valid are correctly validated by the CPFValidator
        when provided in an irregular format without separators (e.g., '12345678909').
        """
        irregular_cpfs = ['12345678909', '98765432100', '57635410067']
        for each_cpf in irregular_cpfs:
            self.assertTrue(CPFValidator.validate(CPF(each_cpf).cpf_clean))

    def test_invalid_cpf_with_irregular_format(self):
        """
        Test the validation of irregular format invalid CPFs.

        This test checks if CPFs known to be invalid are correctly identified as invalid by the 
        CPFValidator when provided in an irregular format without separators.
        """
        irregular_cpfs = ['11111111111', '5763541067', '123456784190', 'abcdefghijk', '']
        for each_cpf in irregular_cpfs:
            self.assertFalse(CPFValidator.validate(CPF(each_cpf).cpf_clean))

if __name__ == '__main__':
    unittest.main()
