class Solution {
    isAlphanumeric(char) {
        return (char >= 'a' && char <= 'z') || 
               (char >= 'A' && char <= 'Z') || 
               (char >= '0' && char <= '9');
    }
    
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        let l = 0;
        let r = s.length - 1;

        while (l < r) {
            if (l < r && !this.isAlphanumeric(s[l])) {
                l++;
            }
            else if (r > l && !this.isAlphanumeric(s[r])) {
                r--;
            }
            else if (s[l].toLowerCase() !== s[r].toLowerCase()) {
                return false;
            }
            else {
                l++;
                r--;
            }
        }
        return true;
    }
}
