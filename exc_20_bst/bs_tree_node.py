from dataclasses import dataclass
from typing import Any, Optional, List, Tuple


@dataclass
class BSTreeNode:
    key: int  # could be something comparable
    value: Any
    parent: Optional["BSTreeNode"] = None
    left: Optional["BSTreeNode"] = None
    right: Optional["BSTreeNode"] = None

    def draw_node(self) -> Tuple[List[str], int, int, int]:
        if not self.left and not self.right:
            s = str(self.key)
            key_width = len(s)
            height = 1
            middle = key_width // 2
            return [s], key_width, height, middle

        s = str(self.key)
        s_width = len(s)

        left_tree, l_width, l_height, middle_l = self.left.draw_node()
        right_tree, r_width, r_height, middle_r = self.right.draw_node()

        first_line = (
            (middle_l + 1) * " "
            + (l_width - middle_l - 1) * "_"
            + s
            + middle_r * "_"
            + (r_width - middle_r) * " "
        )
        second_line = (
            middle_l * " "
            + "/"
            + (l_width - middle_l - 1 + s_width + middle_r) * " "
            + "\\"
            + (r_width - middle_r - 1) * " "
        )
        if l_height > r_height:
            right_tree += [r_height * " "] * (l_height - r_height)
        if r_height > l_height:
            left_tree += [l_height * " "] * (r_height - l_height)
        zipped_lines = zip(left_tree, right_tree)
        lines = [first_line, second_line] + [
            a + s_width * " " + b for a, b in zipped_lines
        ]
        return (
            lines,
            l_width + s_width + r_width,
            max(l_height, r_height) + 2,
            l_width + s_width // 2,
        )

    def display(self) -> None:
        lines, *_ = self.draw_node()
        for line in lines:
            print(line)

    def calc_max_depth(self) -> int:
        nodes_to_check = [(self, 0)]
        max_depth = 0
        while nodes_to_check:
            node, depth = nodes_to_check.pop()
            if max_depth < depth:
                max_depth = depth
            if node.left:
                nodes_to_check.append((node.left, depth + 1))
            if node.right:
                nodes_to_check.append((node.right, depth + 1))

        return max_depth
