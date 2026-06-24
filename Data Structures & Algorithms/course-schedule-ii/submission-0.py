class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        adjacency list, indegree list - initialize
        initialize q with 0 indegree nodes
        for each node in the queue, reduce the indegree of the neighbors by 1 and if indegree[neighbor] == 0 append to q
        if result == numCourses then done else cycle was detected
        '''

        adjacency = [deque() for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        res = deque()

        for course, prereq in prerequisites:
            #add the course to the adjacency list of the prereq (make the connection outgoing from the prereq)
            adjacency[prereq].append(course)
            #add one node coming into the course
            indegree[course] += 1

        #add. indegree nodes to the queue
        q = deque()

        for idx, val in enumerate(indegree):
            if val == 0:
                q.append(idx)

        while len(q) != 0:
            curr = q.popleft()
            res.append(curr)

            for neighbor in adjacency[curr]:
                #decrease one from he indegree count of the neighbor indicating that we processed one of the prereqs
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return list(res) if len(res) == numCourses else []
