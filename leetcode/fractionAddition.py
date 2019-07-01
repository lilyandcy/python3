class Solution:
    def fractionAddition(self, expression: str) -> str:
        # Separate each number and store them in a list, with the set (child, base) format
        # Execute (child1, base1) + (child2, base2) -> find out gcd for base1 and base2
        # -> Execute result = ((child1*(gcd//base1) + child2*(gcd//base2)), gcd)
        # find gcd of new child and new base
        def gcd(a, b):
            return b if a%b == 0 else gcd(b, a%b)
        def lcm(a, b):
            return int(a*b/gcd(a,b))

        if expression.count('/') == 1:
            return expression
        expression = expression.replace('-', '+-')
        tmp = expression.split('+')
        tmp1 = []
        for x in tmp:
            if len(x):
                y = x.split('/')
                tmp1.append((int(y[0]), int
                (y[1])))
        fm, fz = 1, 0
        for x in tmp1:
            fm = lcm(fm,x[1])
        for x in tmp1:
            fz+=x[0]*(fm//x[1])
        if fz == 0:
            return '0/1'
        gys = gcd(fm, abs(fz))
        return str(fz//gys) + '/' + str(fm//gys)