import re
from decimal import Decimal


tolerance_database = {
    '0/3': {
        'h5': {'max': '0.000', 'min': '-0.004'},
        'g6': {'max': '-0.002', 'min': '-0.008'},
        'h6': {'max': '0.000', 'min': '-0.006'},
        'js6': {'max': '0.003', 'min': '-0.003'},
        'k6': {'max': '0.006', 'min': '0.000'},
        'n6': {'max': '0.010', 'min': '0.004'},
        'r6': {'max': '0.016', 'min': '0.010'},
        'f7': {'max': '-0.006', 'min': '-0.016'},
        'h7': {'max': '0.000', 'min': '-0.010'},
        's7': {'max': '0.024', 'min': '0.014'},
        'e8': {'max': '-0.014', 'min': '-0.028'},
        'u8': {'max': '0.032', 'min': '0.018'},
        'd9': {'max': '-0.020', 'min': '-0.045'},
        'e9': {'max': '-0.014', 'min': '-0.039'},
        'f9': {'max': '-0.006', 'min': '-0.031'},
        'h9': {'max': '0.000', 'min': '-0.025'},
        'd11': {'max': '-0.020', 'min': '-0.080'},
        'h11': {'max': '0.000', 'min': '-0.060'},
        'b12': {'max': '-0.140', 'min': '-0.240'},
        'h12': {'max': '0.000', 'min': '-0.100'},
        'h14': {'max': '0.000', 'min': '-0.250'},
        'h15': {'max': '0.000', 'min': '-0.400'},
        'h16': {'max': '0.000', 'min': '-0.600'},
        'Js6': {'max': '0.003', 'min': '-0.003'},
        'K6': {'max': '0.000', 'min': '-0.006'},
        'H7': {'max': '0.010', 'min': '0.000'},
        'Js7': {'max': '0.005', 'min': '-0.005'},
        'K7': {'max': '0.000', 'min': '-0.010'},
        'N7': {'max': '-0.004', 'min': '-0.014'},
        'F8': {'max': '0.020', 'min': '0.006'},
        'H8': {'max': '0.014', 'min': '0.000'},
        'H9': {'max': '0.025', 'min': '0.000'},
        'H11': {'max': '0.060', 'min': '0.000'},
        'H12': {'max': '0.100', 'min': '0.000'},
        'H14': {'max': '0.250', 'min': '0.000'},
        'H15': {'max': '0.400', 'min': '0.000'},
        'H16': {'max': '0.600', 'min': '0.000'}
    }
}


class DimentionsInputTypeError(Exception):
    """
    Checking the correctness of the type entered dimension.
    """


class DimensionInputError(DimentionsInputTypeError):
    """
    Checking the correctness of the entered dimension.
    """


class DimensionsRangeDoesNotExist(DimentionsInputTypeError):
    """
    Checking there is dimensions in the database.
    """

class SomeOperandIsNotTypeDimensions(DimentionsInputTypeError):
    """
    Checking the types of operands.
    """


class ChainDimentionsInputTypeError(Exception):
    """
    Checking the correctness of the type entered chain of dimension.
    """


class ChainDimensionInputError(ChainDimentionsInputTypeError):
    """
    Checking the correctness of the entered chain of dimension.
    """


class A:
    """
    Examples of writing: 5h7, 5.5js6, 10Js7, 15.5H14, 5.5+-0.1, 4.5+0.5, 4.5+0.5-0.02
    """

    def __init__(self, dimension):
        if isinstance(dimension, str):
            self.nominal, self.max, self.min = self.__parser(dimension)
        elif isinstance(dimension, A):
            self.nominal, self.max, self.min = dimension.nominal, dimension.max, dimension.min
        else:
            raise DimentionsInputTypeError
    
    def __str__(self):
        return(
            'Abs: {}\nMax: {}\nMin: {}\nDelta: {}\nTolerance max: {}\nTolerance min: {}'.format(
                self.nominal,
                self.nominal + self.max,
                self.nominal + self.min,
                self.max - self.min,
                self.max,
                self.min
            )
        )
    
    def __add__(self, other):
        if isinstance(other, A):
            self.nominal += other.nominal
            self.max += other.max
            self.min += other.min
            return self
        else:
            raise SomeOperandIsNotTypeDimensions
    
    def __mul__(self, num):
        if isinstance(num, int):
            self.nominal *= num
            self.max *= num
            self.min *= num
            return self
        else:
            raise SomeOperandIsNotTypeDimensions
    
    __radd__ = __add__

    __rmul__ = __mul__

    __iadd__ = __add__

    __imul__ = __mul__
    
    @staticmethod
    def __parser(dimension):
        """
        Finds dimension and tolerance or throws an exception.
        """

        def tolerance_search(nominal):
            """
            Finds dimension in the database.
            """
            if Decimal('0.000') < nominal <= Decimal('3.000'):
                return '0/3'
            elif Decimal('3.000') < nominal <= Decimal('6.000'):
                return '3/6'
            elif Decimal('6.000') < nominal <= Decimal('10.000'):
                return '6/10'
            elif Decimal('10.000') < nominal <= Decimal('18.000'):
                return '10/18'
            elif Decimal('18.000') < nominal <= Decimal('24.000'):
                return '18/24'
            elif Decimal('24.000') < nominal <= Decimal('30.000'):
                return '24/30'
            elif Decimal('30.000') < nominal <= Decimal('40.000'):
                return '30/40'
            elif Decimal('40.000') < nominal <= Decimal('50.000'):
                return '40/50'
            elif Decimal('50.000') < nominal <= Decimal('65.000'):
                return '50/65'
            elif Decimal('65.000') < nominal <= Decimal('80.000'):
                return '65/80'
            elif Decimal('80.000') < nominal <= Decimal('100.000'):
                return '80/100'
            elif Decimal('100.000') < nominal <= Decimal('120.000'):
                return '100/120'
            elif Decimal('120.000') < nominal <= Decimal('140.000'):
                return '120/140'
            elif Decimal('140.000') < nominal <= Decimal('160.000'):
                return '140/160'
            elif Decimal('160.000') < nominal <= Decimal('180.000'):
                return '160/180'
            elif Decimal('180.000') < nominal <= Decimal('200.000'):
                return '180/200'
            elif Decimal('200.000') < nominal <= Decimal('225.000'):
                return '200/225'
            elif Decimal('225.000') < nominal <= Decimal('250.000'):
                return '225/250'
            elif Decimal('250.000') < nominal <= Decimal('280.000'):
                return '250/280'
            elif Decimal('280.000') < nominal <= Decimal('315.000'):
                return '280/315'
            elif Decimal('315.000') < nominal <= Decimal('355.000'):
                return '315/355'
            elif Decimal('355.000') < nominal <= Decimal('400.000'):
                return '355/400'
            elif Decimal('400.000') < nominal <= Decimal('450.000'):
                return '400/450'
            elif Decimal('450.000') < nominal <= Decimal('500.000'):
                return '450/500'
            else:
                raise DimensionsRangeDoesNotExist
        
        # Finds dimension like this: 5h7, 5.5js6, 10Js7, 15.5H14
        _type = re.findall(r"^(\d+\.?\d*?)([a-zA-Z]{1,2}\d{1,2})$", dimension)
        if _type != list():
            tolerance = tolerance_search(Decimal(_type[0][0]))

            if tolerance in tolerance_database:
                tolerance = tolerance_database[tolerance].get(_type[0][1])

                if tolerance is not None:
                    return(
                        Decimal(_type[0][0]).quantize(Decimal('0.000')),
                        Decimal(tolerance['max']).quantize(Decimal('0.000')),
                        Decimal(tolerance['min']).quantize(Decimal('0.000'))
                    )
                else:
                    raise DimensionsRangeDoesNotExist
        
        # Finds dimension like this: 5.5+-0.1
        _type = re.findall(r"^(\d+\.?\d*?)\+{1}\-{1}(\d+\.?\d*?)$", dimension)
        if _type != list():
            return(
                Decimal(_type[0][0]).quantize(Decimal('0.000')),
                Decimal(_type[0][1]).quantize(Decimal('0.000')),
                - Decimal(_type[0][1]).quantize(Decimal('0.000'))
            )
        
        # Finds dimension like this: 4.5+0.5
        _type = re.findall(r"^(\d+\.?\d*?)([\+{1}|\-{1}]\d+\.?\d*?)$", dimension)
        if _type != list():

            if Decimal(_type[0][1]) > Decimal('0.000'):
                return(
                    Decimal(_type[0][0]).quantize(Decimal('0.000')),
                    Decimal(_type[0][1]).quantize(Decimal('0.000')),
                    Decimal('0.000')
                )
            else:
                return(
                    Decimal(_type[0][0]).quantize(Decimal('0.000')),
                    Decimal('0.000'),
                    Decimal(_type[0][1]).quantize(Decimal('0.000'))
                )
        
        # Finds dimension like this: 4.5+0.5-0.02
        _type = re.findall(r"^(\d+\.?\d*?)([\+{1}|\-{1}]\d+\.?\d*?)([\-{1}|\+{1}]\d+\.?\d*?)$", dimension)
        if _type != list():
            print(_type)
            if Decimal(_type[0][1]) < Decimal(_type[0][2]):
                a = _type[0][1]
                b = _type[0][2]
                a, b = b, a
            else:
                a = _type[0][1]
                b = _type[0][2]
            return(
                Decimal(_type[0][0]).quantize(Decimal('0.000')),
                Decimal(a).quantize(Decimal('0.000')),
                Decimal(b).quantize(Decimal('0.000'))
            )
        else:
            raise DimensionInputError


class I(A):
    """
    Increasing size inherited from class A, 
    for more clarity when writing dimension chains.
    """

    def __init__(self, dimension):
        super().__init__(dimension)


class R(A):
    """
    Reducing size inherited from class A,
    for more clarity when writing dimension chains.
    """

    def __init__(self, dimension):
        super().__init__(dimension)


class Chain:
    """
    Dimension chain representation. Dimension chain solver.
    Chain view: Chain([I('5h7'), R('2+0.5')]).
    """

    def __init__(self, chain):
        if isinstance(chain, list):
            self.chain = chain
        else:
            raise ChainDimentionsInputTypeError
    
    def MCI(self):
        """
        Method of complete interchangeability.
        """
        self.nominal = Decimal('0.000')
        self.max = Decimal('0.000')
        self.min = Decimal('0.000')
        for dimensions in self.chain:
            if isinstance(dimensions, I):
                self.nominal += dimensions.nominal
                self.max += dimensions.max
                self.min += dimensions.min
            elif isinstance(dimensions, R):
                self.nominal -= dimensions.nominal
                self.max -= dimensions.min
                self.min -= dimensions.max
            else:
                raise ChainDimensionInputError
        print(
            'Result of Method of Complete Interchangeability:\n',
            'Abs: {}\nMax: {}\nMin: {}\nDelta: {}\nTolerance max: {}\nTolerance min: {}'.format(
                self.nominal,
                self.nominal + self.max,
                self.nominal + self.min,
                self.max - self.min,
                self.max,
                self.min
            ),
            sep=''
        )   


if __name__ == '__main__':
    #a = D('4.5+-0.2')
    #b = D('2h7')
    #print(a.dimension, b.dimension)
    #print('max', a.max, b.max)
    #print('min', a.min, b.min)
    #c = D('4.5-0.2') + D('2-0.1') + D('4.5-0.02') * 1
    #print(c.dimension)
    #print('max', c.max)
    #print('min', c.min)
    #print(c)
    #a = I('4.5-0.2')
    #a -= I('2.5-0.1')
    #a *= 1
    #print(a)

    #c = I('50+0.15') - R('45-0.03') - R('5-0.02')
    chain = Chain(
        [
            I('50+0.15'),
            R('45-0.03'),
            R('5-0.02')
        ]
    )
    chain.MCI()
    #c = I('9-0.25+0.45')
   # d = Chain([])
    #print(chain.nominal)
    #print(chain.max)
    #print(chain.min)
