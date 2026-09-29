// Definition for a pair
// public class Pair {
//     public int Key;
//     public string Value;

//     public Pair(int key, string value) {
//         Key = key;
//         Value = value;
//     }
// }

public class Solution {
    public List<List<Pair>> InsertionSort(List<Pair> pairs) {
        List<List<Pair>> pairsList = new List<List<Pair>>();
        
        for (int i = 0; i < pairs.Count; i++) {
            int j = i - 1;
            while (j >= 0 && pairs[j].Key > pairs[j + 1].Key) {
                Pair tmp = pairs[j];
                pairs[j] = pairs[j + 1];
                pairs[j + 1] = tmp; 
                j--;
            }
            List<Pair> cloneList = new List<Pair>(pairs);
            pairsList.Add(cloneList);
        };
        return pairsList;
    }
}
