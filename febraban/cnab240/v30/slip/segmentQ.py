from ...characterType import numeric, alphaNumeric
from ..row import Row


class SegmentQ:

    def __init__(self):
        self.content = "0000000000000  000000000000000000                                                                                               00000000                 0000000000000000                                        000                            "
        self.defaultValues()

    def defaultValues(self):
        structs = [
            ( 3,  7, 4,      numeric, "1"),
            ( 7,  8, 1,      numeric, "3"),
            (13, 14, 1, alphaNumeric, "Q"),
            (15, 17, 2,      numeric, "01"),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setSenderBank(self, bank):
        structs = [
            (0, 3, 3, numeric, bank.bankId),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPositionInLot(self, index):
        structs = [
            (8, 13, 5, numeric, index)                                                # Indica index do lote
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPayer(self, user):
        structs = [
            (17,  18,  1,      numeric, "1" if len(user.identifier) == 11 else "2"), # 1 - CPF/ 2 - CNPJ
            (18,  33, 15,      numeric, user.identifier),                            # CPF/CNPJ do Pagador
            (33,  63, 30, alphaNumeric, user.name)                                   # Nome do Pagador
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)

    def setPayerAddress(self, address):
        structs = [
            ( 73, 113, 40, alphaNumeric, "%s %s %s" % (address.streetName, address.number, address.complement)),
            (113, 128, 15, alphaNumeric, address.district),
            (128, 136,  8,      numeric, address.zipcode),
            (136, 151, 15, alphaNumeric, address.city),
            (151, 153,  2, alphaNumeric, address.state),
        ]
        self.content = Row.setStructs(structs=structs, content=self.content)