// 168. Excel Sheet Column Title

class Solution {
    public String convertToTitle(int columnNumber) {
        StringBuilder title = new StringBuilder();
        while (columnNumber > 0) {
            int rem = columnNumber % 26;
            if (rem == 0) {
                title.append("Z");
                columnNumber = (columnNumber / 26) - 1;
            } else {
                title.append((char) (rem - 1 + (int)'A'));
                columnNumber = columnNumber / 26;
            }
        }
        return title.reverse().toString();
    }
}
