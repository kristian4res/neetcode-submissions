class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s === t) {
            return true;
        }
        if (s.length !== t.length) {
            return false;
        }

        let map = {};

        for (let i = 0 ; i <= s.length - 1; i++) {
           if (map[s[i]] !== 1) {
              map[s[i]] = 1
           }
           else { 
            map[s[i]] += 1;
           }
        }

        for (let j = 0; j <= t.length - 1; j++) {
            if (map[t[j]] !== 1) {
                map[t[j]] = 1
          }
            else {
               map[t[j]] += 1
           }
         }
        
        for (const item in map) {
          if (!(s.includes(item) && t.includes(item))) {
            return false;
          }
          if ((map[item] % 2 !== 0)) {
            return false;
          };
        }
        return true;
    }
}
