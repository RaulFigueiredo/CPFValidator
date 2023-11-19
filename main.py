"""
This module provides a simple user interface for validating CPF numbers using 
the CPFValidator and CPF classes from the 'src.validator' module.

Usage:
    Run the module and input the CPF number.
    The module will then display whether the CPF is valid or invalid.
"""

from src.validator import CPFValidator, CPF


if __name__ == "__main__":
    provided_cpf = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    cpf = CPF(provided_cpf)

    if CPFValidator.validate(cpf.cpf_clean):
        print("CPF é válido")
    else:
        print("CPF é inválido")
