class Solution:
    '''
    topological sort algo :
    1. calculate indegree of every node (and mantain adjacency list of every node)
    2. Initialize queue with all nodes with indegree 0 (no. of nodes coming in == 0)
    3. 
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #ok so create the adjacency list and indegree first
        adjacency_list = [[] for _ in range(numCourses)]
        indegree_list = [0 for _ in range(numCourses)]
        topo_count = 0

        for course, prereq in prerequisites:
            adjacency_list[prereq].append(course)
            indegree_list[course] += 1

        # print(adjacency_list, indegree_list)

        q = deque()
        #initialize q with all nodes with 0 indegree
        for idx, val in enumerate(indegree_list):
            if val == 0:
                q.append(idx)

        while len(q) != 0:
            curr = q.popleft()
            topo_count += 1

            for neighbor in adjacency_list[curr]:
                indegree_list[neighbor] -= 1

                if indegree_list[neighbor] == 0:
                    q.append(neighbor)

        return topo_count == numCourses