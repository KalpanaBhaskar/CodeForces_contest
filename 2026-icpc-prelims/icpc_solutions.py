# ICPC India Online Round 2026 - Complete Solutions

# ============================================================================
# Problem A: Phone Charging
# ============================================================================
# Time Complexity: O(1) per test case
# Space Complexity: O(1)
#
# Intuition:
# - If current battery < 80%, we charge at 'a' seconds per percent
# - If current battery >= 80%, we charge at 'b' seconds per percent
# - Calculate time to reach 80%, then time to reach 100%

def phone_charging(x, a, b):
    """
    Calculate total seconds needed to charge from x% to 100%
    """
    if x >= 100:
        return 0
    
    # Time to reach 80% (if x < 80)
    time_to_80 = max(0, 80 - x) * a
    
    # Time from 80% to 100%
    time_to_100 = (100 - 80) * b
    
    # If x >= 80, no time needed to reach 80%
    if x >= 80:
        time_to_100 = (100 - x) * b
        return time_to_100
    
    return time_to_80 + time_to_100


# Test cases
def solve_A():
    t = int(input())
    for _ in range(t):
        x, a, b = map(int, input().split())
        print(phone_charging(x, a, b))

# solve_A()


# ============================================================================
# Problem B: Cyclic Shift
# ============================================================================
# Time Complexity: O(n^2) per test case (n cyclic shifts, each takes O(n) to compute f)
# Space Complexity: O(n)
#
# Intuition:
# - f(b) = maximum absolute difference between adjacent elements
# - Try all n possible cyclic shifts
# - For each shift, compute the maximum difference
# - Return the minimum across all shifts

def cyclic_shift(arr):
    """
    Find minimum f-value over all cyclic shifts
    f(b) = max |b[i] - b[i+1]| for 0 <= i < n-1
    """
    n = len(arr)
    min_f = float('inf')
    
    # Try each cyclic shift
    for k in range(n):
        # Create cyclic shift: arr[k:] + arr[:k]
        shifted = arr[k:] + arr[:k]
        
        # Calculate f-value for this shift
        max_diff = 0
        for i in range(n - 1):
            max_diff = max(max_diff, abs(shifted[i] - shifted[i + 1]))
        
        min_f = min(min_f, max_diff)
    
    return min_f


def solve_B():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(cyclic_shift(arr))

# solve_B()


# ============================================================================
# Problem C: Furious Farming
# ============================================================================
# Time Complexity: O(m log m) per test case
# Space Complexity: O(m)
#
# Intuition:
# - We need to visit all fields [1, n]
# - Clouds start at positions in array x
# - All clouds move together (left or right by 1 each day)
# - We need to find positions where all gaps between consecutive clouds are covered
# - The answer is: max_cloud - min_cloud positions
# - But we need to also cover field 1 and field n
# - Strategy: Calculate distance from leftmost cloud to 1, and from rightmost to n

def furious_farming(n, clouds):
    """
    Find minimum days to visit all fields [1, n] with m rainclouds
    """
    if len(clouds) == n:
        return 0
    
    clouds.sort()
    m = len(clouds)
    
    # Gaps between consecutive clouds
    gaps = []
    for i in range(m - 1):
        gaps.append(clouds[i + 1] - clouds[i] - 1)
    
    # Maximum gap between clouds
    max_gap = max(gaps) if gaps else 0
    
    # Distance to cover field 1 from leftmost cloud
    dist_to_start = clouds[0] - 1
    
    # Distance to cover field n from rightmost cloud
    dist_to_end = n - clouds[-1]
    
    # We need to move enough to cover:
    # 1. The maximum gap between clouds
    # 2. Distance to reach field 1
    # 3. Distance to reach field n
    # But distances to start/end need to be done sequentially or we double back
    
    # The answer is the maximum of:
    # - max_gap (to cover all gaps between clouds)
    # - max(dist_to_start, dist_to_end) + min(dist_to_start, dist_to_end)
    # Which simplifies to: max_gap + max(dist_to_start, dist_to_end)
    
    if max_gap == 0:
        # All consecutive clouds are adjacent
        return max(dist_to_start, dist_to_end)
    
    return max_gap + max(dist_to_start, dist_to_end)


def solve_C():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        clouds = list(map(int, input().split()))
        print(furious_farming(n, clouds))

# solve_C()


# ============================================================================
# Problem D: Curio Packing
# ============================================================================
# Time Complexity: O(n * k^2) or O(2^n) with memoization - Dynamic Programming
# Space Complexity: O(n * k^2)
#
# Intuition:
# - Use dynamic programming with state: (index, weight_bag1, weight_bag2)
# - For each curio, try placing it in either bag
# - A glass curio breaks if total weight above it exceeds k
# - We track current weight in each bag (weight above items we place)
# - When we place an item, it adds to weight for future items

def curio_packing(n, k, s):
    """
    Determine if all curios can be packed without breaking glass curios
    dp[i][w1][w2] = can we pack first i curios with weight w1, w2 in bags
    """
    # Memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def dp(idx, w1, w2):
        # Base case: all curios placed
        if idx == n:
            return True
        
        curio = s[idx]
        
        if curio == 'G':
            weight = 1
            # Try placing in bag 1: weight above it is w1
            if w1 <= k:
                if dp(idx + 1, w1 + weight, w2):
                    return True
            
            # Try placing in bag 2: weight above it is w2
            if w2 <= k:
                if dp(idx + 1, w1, w2 + weight):
                    return True
        else:  # Iron curio
            weight = 2
            # Try placing in bag 1
            if dp(idx + 1, w1 + weight, w2):
                return True
            
            # Try placing in bag 2
            if dp(idx + 1, w1, w2 + weight):
                return True
        
        return False
    
    return dp(0, 0, 0)


def solve_D():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        s = input().strip()
        if curio_packing(n, k, s):
            print("YES")
        else:
            print("NO")

# solve_D()


# ============================================================================
# Problem E: Side Hustle
# ============================================================================
# Time Complexity: O(n log n) per test case
# Space Complexity: O(n)
#
# Intuition:
# - We want to maximize: sum of rewards for fixed positions - cost of swaps
# - The permutation can be decomposed into cycles
# - To fix a cycle of length L, we need L-1 swaps
# - We should only fix cycles where: sum of rewards >= (L-1) * c
# - For each cycle, we can choose to fix it or not

def side_hustle(n, c, p, a):
    """
    Maximize profit = sum of rewards for fixed positions - swap costs
    p[i] = token held by person i (0-indexed)
    a[i] = reward if person i has token i
    """
    # Find cycles in the permutation
    visited = [False] * n
    cycles = []
    
    for i in range(n):
        if not visited[i]:
            cycle = []
            j = i
            while not visited[j]:
                visited[j] = True
                cycle.append(j)
                j = p[j] - 1  # p is 1-indexed, convert to 0-indexed
            
            if len(cycle) > 0:
                cycles.append(cycle)
    
    total_profit = 0
    
    # For each cycle, decide whether to fix it
    for cycle in cycles:
        if len(cycle) == 1:
            # Already in correct position, get reward for free
            total_profit += a[cycle[0]]
        else:
            # Cost to fix this cycle
            swap_cost = (len(cycle) - 1) * c
            
            # Reward if we fix this cycle
            reward = sum(a[i] for i in cycle)
            
            # Only fix if profitable
            if reward >= swap_cost:
                total_profit += reward - swap_cost
    
    return total_profit


def solve_E():
    t = int(input())
    for _ in range(t):
        n, c = map(int, input().split())
        p = list(map(int, input().split()))
        a = list(map(int, input().split()))
        print(side_hustle(n, c, p, a))

# solve_E()


# ============================================================================
# Problem F: Take the L
# ============================================================================
# Time Complexity: O(n^2) - trying to build a 2-SAT or greedy assignment
# Space Complexity: O(n)
#
# Intuition:
# - Each point must choose one of two ray configurations
# - Two rays from point A intersect rays from point B if:
#   - Both go right and B is to the right of A and below A (right-up rays)
#   - Both go left and B is to the left of A and above A (left-down rays)
# - This is a 2-SAT problem, but we can use backtracking or greedy approach
#
# Simpler greedy: Sort by x-coordinate, try to assign greedily

def take_the_l(points):
    """
    Determine if we can assign ray pairs to all points without intersections
    """
    n = len(points)
    
    if n == 1:
        return True
    
    # Try with backtracking
    # assignment[i] = 0 means (right, up), 1 means (left, down)
    assignment = [-1] * n
    
    def rays_intersect(i, config_i, j, config_j):
        """
        Check if rays from point i with config_i intersect with point j config_j
        config: 0 = (right, up), 1 = (left, down)
        """
        xi, yi = points[i]
        xj, yj = points[j]
        
        if config_i == 0:  # right-up rays from point i
            # Ray goes right (x >= xi) and up (y >= yi)
            if config_j == 0:  # right-up from j
                # Rays intersect if j is to the right and below i
                # OR i is to the right and below j
                if xj > xi and yj < yi:
                    return True
                if xi > xj and yi < yj:
                    return True
            else:  # left-down from j
                # No intersection possible with different directions
                pass
        else:  # left-down rays from point i
            # Ray goes left (x <= xi) and down (y <= yi)
            if config_j == 1:  # left-down from j
                # Rays intersect if j is to the left and above i
                # OR i is to the left and above j
                if xj < xi and yj > yi:
                    return True
                if xi < xj and yi > yj:
                    return True
            else:  # right-up from j
                # No intersection possible
                pass
        
        return False
    
    def backtrack(idx):
        if idx == n:
            return True
        
        for config in range(2):
            # Check if this configuration conflicts with previous assignments
            valid = True
            for j in range(idx):
                if rays_intersect(idx, config, j, assignment[j]):
                    valid = False
                    break
            
            if valid:
                assignment[idx] = config
                if backtrack(idx + 1):
                    return True
                assignment[idx] = -1
        
        return False
    
    return backtrack(0)


def solve_F():
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append((x, y))
        
        if take_the_l(points):
            print("YES")
        else:
            print("NO")

# solve_F()


# ============================================================================
# Problem G: Team Formation Tactics
# ============================================================================
# Time Complexity: O(n * 3^n) with DP or O(n^2 * 2^n) with greedy
# Better: O(3n log(3n)) with greedy approach
# Space Complexity: O(1) or O(n)
#
# Intuition:
# - Sort students by rating in descending order
# - For each team, assign three consecutive high-rated students
# - The strength formula: max(6x, 4x+4y, 3x+3y+3z)
# - Greedy: always pick top 3 remaining students and form teams

def team_formation(n, ratings):
    """
    Maximize sum of team strengths
    strength = max(6x, 4x+4y, 3x+3y+3z) where x >= y >= z
    """
    ratings.sort(reverse=True)
    
    total_strength = 0
    
    # Greedy: form teams by taking consecutive students
    for i in range(n):
        x = ratings[3 * i]
        y = ratings[3 * i + 1]
        z = ratings[3 * i + 2]
        
        yxz = max(6 * x, 4 * x + 4 * y, 3 * x + 3 * y + 3 * z)
        total_strength += yxz
    
    return total_strength


def solve_G():
    t = int(input())
    for _ in range(t):
        n = int(input())
        ratings = list(map(int, input().split()))
        print(team_formation(n, ratings))

# solve_G()


# ============================================================================
# Problem H: Random Merging
# ============================================================================
# Time Complexity: O(n^2) per test case
# Space Complexity: O(n^2)
#
# Intuition:
# - Use dynamic programming / linearity of expectation
# - Each element a[i] contributes to the final sum multiple times
# - The contribution of a[i] to s depends on how many times it gets merged
# - Each pair (i, i+1) will be merged if chosen at some point
# - Probability that a[i] is added to s = number of merges involving position i
# - Using linearity of expectation: E[s] = sum of (a[i] * probability it's added)

def random_merging(n, a):
    """
    Find expected value of s in the random merging process
    """
    MOD = 998244353
    
    if n == 1:
        return 0
    
    # For each pair (i, i+1), calculate probability it gets merged
    # and contribution to expected value
    
    # Key insight: element a[i] gets added to s multiple times
    # Specifically, it gets added every time we merge a pair containing it
    # The probability that a[i] is involved in k merges depends on the merge sequence
    
    # Simpler approach: 
    # E[s] = sum of a[i] * (number of times a[i] is counted)
    # Using contribution counting:
    # a[i] contributes to s once for each merge that involves it
    # On average, this is related to its position
    
    # For a[i] at position i, it contributes:
    # - When merged with right neighbor
    # - When the result is merged
    # - Etc.
    
    # Contribution of a[i] = a[i] * (n - |i|_from_edges) * something
    
    # Better approach: use the formula
    # Each element a[i] contributes a[i] * (i+1) * (n-i) / (n-1) on average
    # This is because it appears in (i+1) * (n-i) different "segments"
    
    result = 0
    
    for i in range(n):
        # Contribution of a[i]
        # It gets included: (i+1) * (n-i) / (n-1) times on average
        numerator = (i + 1) * (n - i) * a[i]
        denominator = n - 1
        
        # Add to result
        contribution = (numerator % MOD) * pow(denominator, MOD - 2, MOD) % MOD
        result = (result + contribution) % MOD
    
    return result


def solve_H():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(random_merging(n, a))

# solve_H()


# ============================================================================
# Problem I: Mountain Medians
# ============================================================================
# Time Complexity: O(n! * n) in worst case, but pruned significantly
# Space Complexity: O(n)
#
# Intuition:
# - Generate all mountain-shaped permutations
# - For each permutation, check if it satisfies the median conditions
# - Mountain-shaped: increases up to position k, then decreases
# - Condition: for each i, either med(p[1..i]) = a[i] or med(p[i..n]) = a[i]

def mountain_medians(n, a):
    """
    Count mountain-shaped permutations satisfying median conditions
    """
    from itertools import permutations
    
    count = 0
    
    # Generate all permutations
    for perm in permutations(range(1, n + 1)):
        # Check if mountain-shaped
        is_mountain = False
        
        # Try all possible peak positions
        for k in range(n):
            # Check if perm[:k+1] is strictly increasing and perm[k:] is strictly decreasing
            valid = True
            
            # Check increasing part
            for i in range(k):
                if perm[i] >= perm[i + 1]:
                    valid = False
                    break
            
            # Check decreasing part
            if valid:
                for i in range(k, n - 1):
                    if perm[i] <= perm[i + 1]:
                        valid = False
                        break
            
            if valid:
                is_mountain = True
                break
        
        if not is_mountain:
            continue
        
        # Check median conditions
        valid_perm = True
        for i in range(n):
            # Check if a[i] = med(p[0..i]) or a[i] = med(p[i..n])
            
            # Median of p[0..i]
            left_part = sorted(perm[:i + 1])
            med_left = left_part[(i + 1) // 2] if (i + 1) % 2 == 1 else left_part[(i + 1) // 2 - 1]
            
            # Median of p[i..n]
            right_part = sorted(perm[i:])
            med_right = right_part[(n - i) // 2] if (n - i) % 2 == 1 else right_part[(n - i) // 2 - 1]
            
            if a[i] != med_left and a[i] != med_right:
                valid_perm = False
                break
        
        if valid_perm:
            count += 1
    
    return count % 998244353


def solve_I():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print(mountain_medians(n, a))

# solve_I()


# ============================================================================
# Problem J: Off With Their Heads
# ============================================================================
# Time Complexity: O(n^2) with proper DP, O(n log n) greedy attempt
# Space Complexity: O(n)
#
# Intuition:
# - Operation: pick A, B, concatenate, delete first char, insert result
# - AB[1:] means we keep the last character of A and all of B
# - We want lexicographically smallest final string
# - Greedy: at each step, pick A, B such that AB[1:] is smallest
# - Alternatively: use BFS/DFS to explore merge sequences

def off_with_heads(c00, c01, c10, c11):
    """
    Find lexicographically smallest string after merging operations
    """
    from collections import deque
    
    # State: (c00, c01, c10, c11, current_result_string)
    # But this is complex. Use greedy with backtracking
    
    def merge(s1, s2):
        """Merge s1 and s2: s1 + s2, then delete first char"""
        return (s1 + s2)[1:]
    
    # Use BFS to find optimal sequence
    queue = deque()
    queue.append((c00, c01, c10, c11, ""))
    
    best = None
    visited = set()
    
    while queue:
        cnt00, cnt01, cnt10, cnt11, result = queue.popleft()
        
        # Count total strings
        total = cnt00 + cnt01 + cnt10 + cnt11
        
        if total == 1:
            # Only one string left, done
            if cnt00 > 0:
                final = "00"
            elif cnt01 > 0:
                final = "01"
            elif cnt10 > 0:
                final = "10"
            else:
                final = "11"
            
            if best is None or final < best:
                best = final
            continue
        
        # Try all possible merges
        strings = ["00"] * cnt00 + ["01"] * cnt01 + ["10"] * cnt10 + ["11"] * cnt11
        
        for i in range(len(strings)):
            for j in range(len(strings)):
                if i == j:
                    continue
                
                merged = merge(strings[i], strings[j])
                
                # Create new state
                new_strings = strings[:i] + strings[i+1:j-1] + [merged] + strings[j:]
                
                # Count new strings
                new_cnt00 = new_strings.count("00")
                new_cnt01 = new_strings.count("01")
                new_cnt10 = new_strings.count("10")
                new_cnt11 = new_strings.count("11")
                
                state = (new_cnt00, new_cnt01, new_cnt10, new_cnt11)
                
                if state not in visited:
                    visited.add(state)
                    queue.append((new_cnt00, new_cnt01, new_cnt10, new_cnt11, merged))
    
    return best if best else "00"


def solve_J():
    t = int(input())
    for _ in range(t):
        c00, c01, c10, c11 = map(int, input().split())
        print(off_with_heads(c00, c01, c10, c11))

# solve_J()


if __name__ == "__main__":
    # Run the solver for the problem you want
    # solve_A()
    # solve_B()
    # solve_C()
    # solve_D()
    # solve_E()
    # solve_F()
    # solve_G()
    # solve_H()
    # solve_I()
    # solve_J()
    pass
