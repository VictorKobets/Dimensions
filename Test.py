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


class D:
    """
    Examples of writing: 5h7, 5.5js6, 10Js7, 15.5H14, 5.5+-0.1, 4.5+0.5, 4.5+0.5-0.02
    """

    def __init__(self, dimension):
        if isinstance(dimension, str):
            self.dimension, self.max, self.min = self.__parser(dimension)
            self.max += self.dimension
            self.min += self.dimension
        else:
            raise DimentionsInputTypeError
    
    def __str__(self):
        return(
            'Abs: {}\nMax: {}\nMin: {}\nDelta: {}'.format(
                self.dimension,
                self.max,
                self.min,
                self.max - self.min
            )
        )
    
    def __add__(self, other):
        if isinstance(other, D):
            self.dimension += other.dimension
            self.max += other.max
            self.min += other.min
            return self
        else:
            raise SomeOperandIsNotTypeDimensions
    
    def __mul__(self, num):
        if isinstance(num, int):
            self.dimension *= num
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

        def tolerance_search(dimension):
            """
            Finds dimension in the database.
            """
            if Decimal('0.000') < dimension <= Decimal('3.000'):
                return '0/3'
            elif Decimal('3.000') < dimension <= Decimal('6.000'):
                return '3/6'
            elif Decimal('6.000') < dimension <= Decimal('10.000'):
                return '6/10'
            elif Decimal('10.000') < dimension <= Decimal('18.000'):
                return '10/18'
            elif Decimal('18.000') < dimension <= Decimal('24.000'):
                return '18/24'
            elif Decimal('24.000') < dimension <= Decimal('30.000'):
                return '24/30'
            elif Decimal('30.000') < dimension <= Decimal('40.000'):
                return '30/40'
            elif Decimal('40.000') < dimension <= Decimal('50.000'):
                return '40/50'
            elif Decimal('50.000') < dimension <= Decimal('65.000'):
                return '50/65'
            elif Decimal('65.000') < dimension <= Decimal('80.000'):
                return '65/80'
            elif Decimal('80.000') < dimension <= Decimal('100.000'):
                return '80/100'
            elif Decimal('100.000') < dimension <= Decimal('120.000'):
                return '100/120'
            elif Decimal('120.000') < dimension <= Decimal('140.000'):
                return '120/140'
            elif Decimal('140.000') < dimension <= Decimal('160.000'):
                return '140/160'
            elif Decimal('160.000') < dimension <= Decimal('180.000'):
                return '160/180'
            elif Decimal('180.000') < dimension <= Decimal('200.000'):
                return '180/200'
            elif Decimal('200.000') < dimension <= Decimal('225.000'):
                return '200/225'
            elif Decimal('225.000') < dimension <= Decimal('250.000'):
                return '225/250'
            elif Decimal('250.000') < dimension <= Decimal('280.000'):
                return '250/280'
            elif Decimal('280.000') < dimension <= Decimal('315.000'):
                return '280/315'
            elif Decimal('315.000') < dimension <= Decimal('355.000'):
                return '315/355'
            elif Decimal('355.000') < dimension <= Decimal('400.000'):
                return '355/400'
            elif Decimal('400.000') < dimension <= Decimal('450.000'):
                return '400/450'
            elif Decimal('450.000') < dimension <= Decimal('500.000'):
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
        _type = re.findall(r"^(\d+\.?\d*?)(\+{1}\d+\.?\d*?)(\-{1}\d+\.?\d*?)$", dimension)
        if _type != list():
            return(
                Decimal(_type[0][0]).quantize(Decimal('0.000')),
                Decimal(_type[0][1]).quantize(Decimal('0.000')),
                Decimal(_type[0][2]).quantize(Decimal('0.000'))
            )
        else:
            raise DimensionInputError


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
    a = D('4.5-0.2')
    a += D('4.5-0.2')
    a *= 1
    print(a)
