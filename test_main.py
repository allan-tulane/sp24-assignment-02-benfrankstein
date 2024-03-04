from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
    assert subquadratic_multiply(BinaryNumber(40), BinaryNumber(25)) == 40*25
    assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(2)) == 5*2

if __name__ == "__main__":
    test_multiply()
