#include <vector>
#include <algorithm>

using namespace std;

struct Service {
    int throughput;
    int scaling_cost;
    double efficiency;
};

int getMaximumThroughput(vector<int> throughput, vector<int> scaling_cost, int budget) {
    int n = throughput.size();
    vector<Service> services(n);
    
    // Create the service structure with efficiency
    for (int i = 0; i < n; ++i) {
        services[i] = {throughput[i], scaling_cost[i], (double)throughput[i] / scaling_cost[i]};
    }
    
    // Sort services by efficiency (descending order)
    sort(services.begin(), services.end(), [](const Service& a, const Service& b) {
        return a.efficiency > b.efficiency;
    });
    
    int total_throughput = 0;
    int remaining_budget = budget;
    
    for (const auto& service : services) {
        // Calculate the maximum number of times this service can be scaled
        int max_scale = remaining_budget / service.scaling_cost;
        
        // Update total throughput and remaining budget
        total_throughput += service.throughput * max_scale;
        remaining_budget -= service.scaling_cost * max_scale;
        
        if (remaining_budget <= 0) {
            break;
        }
    }
    
    return total_throughput;
}

int main() {
    // Sample input
    vector<int> throughput = {3, 2, 5};
    vector<int> scaling_cost = {2, 5, 10};
    int budget = 28;
    
    int result = getMaximumThroughput(throughput, scaling_cost, budget);
    cout << result << endl; // Output: 6

    return 0;
}
