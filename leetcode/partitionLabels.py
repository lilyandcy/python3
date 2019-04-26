class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        end_map = {}
        for pos, c in enumerate(S):
            end_map[c] = pos
        parts_list = []
        max_pos = 0
        part_count = 0
        for pos, c in enumerate(S):
            if pos > max_pos:
                parts_list.append(part_count)
                part_count = 0
            max_pos = max(max_pos, end_map[c])
            part_count += 1
        parts_list.append(part_count)
        return parts_list