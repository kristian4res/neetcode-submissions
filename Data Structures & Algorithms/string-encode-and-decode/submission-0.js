class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let str = "";
        for (let i = 0; i < strs.length; i++) {
            str += (strs[i] + "|");
        }
        console.log("encode",str)
        return str;
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        let strs = [];
        let strItem = "";
        for (let i = 0; i < str.length; i++) {
            if (str[i] === "|") {
                strs.push(strItem);
                strItem = "";
            }
            else {
                strItem += str[i];
            }
        }
        return strs;
    }
}
