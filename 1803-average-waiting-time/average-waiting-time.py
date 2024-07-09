class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        result = 0
        start_time = 0
        
        for services in customers:
            arrival_time,prep_time =services
            if start_time<arrival_time:
                start_time=arrival_time
            time_to_prepare=prep_time+start_time
            weaiting_time=time_to_prepare-arrival_time
            start_time=time_to_prepare
            result+=weaiting_time
        return result / len(customers)

