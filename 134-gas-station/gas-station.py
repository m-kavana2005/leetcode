class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        tot_gas=sum(gas)
        tot_cost=sum(cost)
        if tot_gas<tot_cost:
            return -1
        cur_gas=0
        start=0
        for i in range(len(gas)):
            cur_gas+=gas[i]-cost[i]
            if cur_gas<0:
                start=i+1
                cur_gas=0
        return start