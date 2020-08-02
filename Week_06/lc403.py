class Solution:
    def canCross(self, stones: List[int]) -> bool:
        hash_map = {}

        for i in range(len(stones)) :
            hash_map[stones[i]] = []
        
        hash_map[0] = [0]

        for i in range(len(stones)) :
            for k in hash_map[stones[i]]:
                for step in range(k - 1, k + 2):
                    if step > 0 and (stones[i] + step) in hash_map:
                        hash_map[stones[i] + step] += [step]
                        hash_map[stones[i] + step] = list(set(hash_map[stones[i] + step]))

        return False if hash_map[stones[-1]] == [] else True




# public class Solution {
#     public boolean canCross(int[] stones) {
#         HashMap<Integer, Set<Integer>> map = new HashMap<>();
#         for (int i = 0; i < stones.length; i++) {
#             map.put(stones[i], new HashSet<Integer>());
#         }
#         map.get(0).add(0);
#         for (int i = 0; i < stones.length; i++) {
#             for (int k : map.get(stones[i])) {
#                 for (int step = k - 1; step <= k + 1; step++) {
#                     if (step > 0 && map.containsKey(stones[i] + step)) {
#                         map.get(stones[i] + step).add(step);
#                     }
#                 }
#             }
#         }
#         return map.get(stones[stones.length - 1]).size() > 0;
#     }
# }


