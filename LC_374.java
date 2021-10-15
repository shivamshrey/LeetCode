// 374. Guess Number Higher or Lower

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is lower than the guess number
 *			      1 if num is higher than the guess number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int low = 1, high = n;
        
        while (low < high) {
            int myGuess = low + (high - low) / 2;
            
            if (guess(myGuess) == 1)
                low = myGuess + 1;
            else
                high = myGuess;
        }
        
        return low;
    }
}
