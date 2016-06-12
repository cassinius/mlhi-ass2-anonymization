class RangeGenHierarchy:

    def __init__(self, label, min, max):
        if min > max:
            raise Exception('Range invalid. Min greater than max.')

        if min == max:
            raise Exception('Range invalid. Min equals max.')

        self._label = ""
        self._min = float(min)
        self._max = float(max)


    def getCostOfRange(self, low, high):
        if low > high:
            raise Exception('Cannot generalize to negative range.')

        if low < self._min:
            raise Exception('Low parameter less than range minimum.')

        if high > self._max:
            raise Exception('High parameter greater than range maximum.')

        return ((high-low) / (self._max-self._min))
