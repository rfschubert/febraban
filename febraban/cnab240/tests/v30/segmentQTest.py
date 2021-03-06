from unittest.case import TestCase
from febraban.cnab240.user import User, UserBank, UserAddress
from febraban.cnab240.v30.slip.segmentQ import SegmentQ


user = User(
    name="JOHN SMITH",
    identifier="12345678901",
)

bank = UserBank(
    bankId="341",
    branchCode="1234",
    accountNumber="1234567",
    accountVerifier="8"
)

address = UserAddress(
    streetName="AV PAULISTA",
    number="1000",
    city="SAO PAULO",
    state="SP",
    zipcode="01310000"
)


class SegmentQTest(TestCase):

    def testSegmentQlengh(self):
        string = SegmentQ().content
        self.assertEqual(len(string), 240)

    def testSegmentQdefaultValues(self):
        content = SegmentQ().content
        self.assertEqual(content[3:7], "0001")
        self.assertEqual(content[7:8], "3")
        self.assertEqual(content[13:14], "Q")
        self.assertEqual(content[15:17], "01")

    def testSegmentQsets(self):
        segment = SegmentQ()
        segment.setPositionInLot(1)
        segment.setSenderBank(bank)
        segment.setPayer(user)
        segment.setPayerAddress(address)
        response = "3410001300001Q 011000012345678901JOHN SMITH                              AV PAULISTA 1000                                       01310000SAO PAULO      SP0000000000000000                                        000                            "
        self.assertEquals(segment.content, response)