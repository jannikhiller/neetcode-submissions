class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        auto pairs = std::vector<std::pair<int, int>>{};
        pairs.reserve(position.size());
        for (size_t i = 0; i < position.size(); ++i) {
            pairs.push_back({position[i], speed[i]});
        }
        std::ranges::sort(pairs, std::ranges::greater{});
        double last_t = -1;
        int fleets = 0;
        for (auto [p, s] : pairs) {
            double t = static_cast<double>(target - p) / s;
            if (t > last_t) {
                ++fleets;
                last_t = t;
            }
        }
        return fleets;
    }
};
