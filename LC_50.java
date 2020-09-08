// 50. Pow(x, n)

class Solution {    
    public double myPow(double x, int n) {
        return powUtil(x, n);
    }
    
    public double powUtil(double x, long n) {
        if (n == 0)
            return 1.0;
        else if (n == 1)
            return x;
        else if (n < 0)
            return powUtil(1 / x, -n);
        
        double result = powUtil(x * x, n / 2);
        if (n % 2 != 0)
            result *= x;
        
        return result;
    }
}
