"""
有一个人前来买瓜，但他忘记了到水果摊应该走哪个道。幸好，他手上有一份城市地图，里面记录了所有道路的起点、终点和长度（最近交警查得严，所以只能单向通行）。请你帮他找到一条从当前位置（Start）到水果摊（Goal）的路径，并且路径的长度越短越好。如果他不可能到达水果摊，请输出“Unreachable”（不含引号）。

Input
输入若干行，每行包含两个字符串和一个正整数，表示一条道路的起点、终点和长度。输入以单独一行 END 结束。

Output
输出仅一行，表示从当前位置到水果摊的最短路径（用“->”连接各个节点，详见样例），或者“Unreachable”（不含引号）。所有数据保证最短路径若存在则一定唯一。

Sample Input 1

Start A 11
A B 45
B Goal 14
END

Sample Output 1

Start->A->B->Goal

Sample Input 2

Start A 1
Goal A 1
END

Sample Output 2

Unreachable
"""


import heapq
import sys


class PriorityQueue:

    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # If item already in priority queue with higher priority, update its priority and rebuild the heap.
        # If item already in priority queue with equal or lower priority, do nothing.
        # If item not in priority queue, do the same thing as self.push.

        for index, (p, c, i) in enumerate(self.heap):
            assert type(i) == node, 'item must be node'

            if i.state == item.state:
                if p <= priority:
                    break

                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)


class node:
    """define node"""

    def __init__(self, state, parent, path_cost, action,):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost
        self.action = action


class problem:
    """searching problem"""

    def __init__(self, initial_state, actions):
        self.initial_state = initial_state
        self.actions = actions

    def search_actions(self, state):
        """Search actions for the given state.
        Args:
            state: a string e.g. 'A'

        Returns:
            a list of action string list
            e.g. [['A', 'B', '2'], ['A', 'C', '3']]
        """
        # ------------------------------- Your code here -------------------------
        raise Exception

    def solution(self, node):
        """Find th path from the beginning to the given node.

        Args:
            node: the node class defined above.

        Returns:
            ['Start', 'A', 'B', ....]
        """
        # ------------------------------- Your code here -------------------------
        raise Exception

    def transition(self, state, action):
        """Find the next state from the state adopting the given action.

        Args:
            state: 'A'
            action: ['A', 'B', '2']

        Returns:
            string, representing the next state, e.g. 'B'
        """
        # ------------------------------- Your code here -------------------------
        raise Exception

    def goal_test(self, state):
        """Test if the state is goal

        Args:
            state: string, e.g. 'Goal' or 'A'

        Returns:
            a bool (True or False)
        """
        # ------------------------------- Your code here -------------------------
        raise Exception

    def step_cost(self, state1, action, state2):
        if (state1 == action[0]) and (state2 == action[1]):
            return int(action[2])
        else:
            print("Step error!")
            sys.exit()

    def child_node(self, node_begin, action):
        """Find the child node from the node adopting the given action

        Args:
            node_begin: the node class defined above.
            action: ['A', 'B', '2']

        Returns:
            a node as defined above
        """
        # ------------------------------- Your code here -------------------------
        raise Exception


def UCS(problem):
    """Using Uniform Cost Search to find a solution for the problem.

    Args:
        problem: problem class defined above.

    Returns:
        a list of strings representing the path.
            e.g. ['A', 'B', '2']
        if the path does not exist, return 'Unreachable'
    """
    node_test = node(problem.initial_state, '', 0, '')
    frontier = PriorityQueue()
    frontier.push(node_test, node_test.path_cost)
    explored = []

    # ------------------------------- Your code here -------------------------
    raise Exception


if __name__ == '__main__':
    Actions = []

    while True:
        a = input().strip()

        if a != 'END':
            a = a.split()
            Actions += [a]
        else:
            break

    graph_problem = problem('Start', Actions)
    answer = UCS(graph_problem)
    s = "->"

    if answer == 'Unreachable':
        print(answer)
    else:
        path = s.join(answer)
        print(path)
