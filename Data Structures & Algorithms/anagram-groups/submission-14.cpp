using key = std::array<uint8_t, 26>;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        key letter_counts{};

        auto hasher = [](const key &k) {
            std::size_t h = 0;
            for (const auto &c : k) {
                h ^= std::hash<uint8_t>{}(c) + 0x9e3779b9 + (h << 6) + (h >> 2);
            }
            return h;

        };
        std::unordered_map<key, std::vector<std::string>, decltype(hasher)> groups{};
        for (auto &s : std::move(strs)) {
            letter_counts.fill(0);
            for (auto c : s) {
                letter_counts[c - 'a'] += 1;
            }
            groups[letter_counts].emplace_back(std::move(s));
        }
        std::vector<std::vector<string>> result;
        result.reserve(groups.size());
        for (auto &[k, vs] : std::move(groups)) {
            result.push_back(std::move(vs));
        }
        return result;
    }
};
