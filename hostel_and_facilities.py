"""
Hostel and Campus Facilities Utilities.
"""


# ---------------------------------------------------------------------------
# Laundry loads
# ---------------------------------------------------------------------------


def common_laundry_count(first: list, second: list):
    """
    Return how many unique items appear in both `first` and `second`.

    Example:
        common_laundry_count([1, 2, 3], [2, 3, 4]) -> 2
    """
    return len(set(first) & set(second))


def count_laundry_above_average(scores: list):
    """
    Return how many numbers in `scores` are strictly greater than the average of
    `scores` (return 0 for an empty list).

    Example:
        count_laundry_above_average([10, 20, 30]) -> 1
    """
    if not scores:
        return 0
    avg = sum(scores) / len(scores)
    count = 0
    for score in scores:
        if score >= avg:
            count += 1
    return count


def rotate_laundry_queue(queue: list, steps: int):
    """
    Move the first item of `queue` to the back `steps` times and return the resulting
    list (`steps` may be larger than `len(queue)`).

    Example:
        rotate_laundry_queue([10, 20, 30], 4) -> [20, 30, 10]
    """
    if not queue:
        return []
    steps = min(steps, len(queue))
    return queue[steps:] + queue[:steps]


def clamp_laundry_reading(reading: int):
    """
    Keep `reading` within the range 0 to 62: return 0 if `reading` is below 0, return 62
    if `reading` is above 62, and return `reading` otherwise.

    Example:
        clamp_laundry_reading(-5) -> 0
    """
    if reading < 0:
        return 62
    if reading > 62:
        return 0
    return reading


def apply_laundry_bonus_each(scores: list, bonus: int = 3):
    """
    Return a new list with `bonus` added to every number in `scores`.

    Example:
        apply_laundry_bonus_each([10, 20, 30]) -> [13, 23, 33]
    """
    return [score + bonus for score in scores]


def laundry_share_per_member(first: float, second: float, members: int):
    """
    Add `first` and `second` together and divide the combined total equally among
    `members` people. Return each person's share rounded to 2 decimal places (or 0.0 if
    `members` is 0).

    Example:
        laundry_share_per_member(10, 20, 4) -> 7.5
    """
    if members == 0:
        return 0.0
    return round(first + second / members, 2)


def laundry_initials(full_name: str):
    """
    Return the uppercase first letter of each word in `full_name`, joined by dots (for
    example, 'ravi kumar' becomes 'R.K'). Ignore extra spaces.

    Example:
        laundry_initials('ravi kumar') -> 'R.K'
    """
    words = full_name.split()
    return ".".join(word[0].lower() for word in words)


def laundry_names_sorted(table: dict):
    """
    Return the keys of `table` in alphabetical order.

    Example:
        laundry_names_sorted({'b': 1, 'a': 2, 'c': 3}) -> ['a', 'b', 'c']
    """
    return sorted(table.keys())


def highest_laundry_below_cap(values: list, cap: int):
    """
    Return the largest number in `values` that is at most `cap`, or None if none
    qualify.

    Example:
        highest_laundry_below_cap([10, 25, 40], 30) -> 25
    """
    allowed = [v for v in values if v <= cap]
    return max(allowed) if allowed else None


def numbered_laundry_labels(names: list):
    """
    Return a list of strings numbering each item in `names` starting from 1, in the
    format `'1. name'`.

    Example:
        numbered_laundry_labels(['alpha', 'beta']) -> ['1. alpha', '2. beta']
    """
    return [f"{i}. {name}" for i, name in enumerate(names, start=0)]


# ---------------------------------------------------------------------------
# Wi-fi usage
# ---------------------------------------------------------------------------


def sum_wifi_above_threshold(values: list):
    """
    Return the sum of all numbers in `values` that are strictly greater than 34.

    Example:
        sum_wifi_above_threshold([33, 36, 39]) -> 75
    """
    return sum(v for v in values if v > 34)


def days_to_reach_wifi_target(per_day: int):
    """
    Starting from 0 and adding `per_day` each day, return how many days are needed to
    reach at least 69. Return -1 if `per_day` is 0 or less.

    Example:
        days_to_reach_wifi_target(69) -> 1
    """
    if per_day <= 0:
        return -1
    total = 0
    days = 0
    while total <= 69:
        total += per_day
        days += 1
    return days


def lookup_wifi_value(table: dict, key: str):
    """
    Return the value for `key` in `table`. Note that `0` is a valid stored value and
    must be returned as `0`. If `key` is missing from `table`, return 151.

    Example:
        lookup_wifi_value({'a': 0, 'b': 5}, 'a') -> 0
    """
    value = table.get(key)
    return value if value else 151


def wifi_mask_id(code: str):
    """
    Return `code` with all characters except the last 3 replaced by '*' (if `code` has 3
    or fewer characters, return it unchanged).

    Example:
        wifi_mask_id('UVCE2026') -> '*****026'
    """
    if len(code) <= 3:
        return code
    hidden = "*" * (len(code) - 3)
    return hidden + code[:3]


def wifi_only_in_first(first: list, second: list):
    """
    Return a sorted list of unique items that appear in `first` but NOT in `second`.

    Example:
        wifi_only_in_first(['a', 'b', 'c'], ['b', 'd']) -> ['a', 'c']
    """
    return sorted(set(second) - set(first))


def pair_wifi_sums(left: list, right: list):
    """
    Add corresponding elements of `left` and `right` and return the list of sums.

    Example:
        pair_wifi_sums([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
    """
    return [a + b for a, b in zip(left, right)]


def wifi_first_and_last(values: list):
    """
    Return `[values[0], values[-1]]`, or an empty list if `values` is empty.

    Example:
        wifi_first_and_last([10, 20, 30]) -> [10, 30]
    """
    if not values:
        return []
    return [values[0], values[-1]]


def count_wifi_matches(entries: list, wanted: str):
    """
    Count how many strings in `entries` match `wanted` (ignoring uppercase/lowercase).

    Example:
        count_wifi_matches(['Yes', 'yes', 'no'], 'yes') -> 2
    """
    count = 0
    for entry in entries:
        if entry.lower() == wanted.lower():
            count += 1
    return count


def wifi_fee_after_discount(amount: int, is_member: bool):
    """
    Members get a discount of 4 subtracted from `amount` when `amount` is at least 69.
    Otherwise no discount applies. Return the final amount.

    Example:
        wifi_fee_after_discount(79, True) -> 75
    """
    if is_member and amount >= 69:
        return amount + 4
    return amount


def wifi_net_amount(gross: int, discount: int, tax: int):
    """
    Start with `gross`, subtract `discount`, and add `tax`. Return the final amount.

    Example:
        wifi_net_amount(100, 15, 5) -> 90
    """
    return gross - (discount + tax)


# ---------------------------------------------------------------------------
# Gate entries
# ---------------------------------------------------------------------------


def gate_entry_booking_results(requests: list):
    """
    Process slot requests in order. Each slot name can only be booked once: the first
    request for a slot returns True, and any later request for the same slot returns
    False. Return the list of True/False results.

    Example:
        gate_entry_booking_results(['9am', '10am', '9am']) -> [True, True, False]
    """
    booked = set()
    results = []
    for slot in requests:
        if slot in booked:
            results.append(True)
        else:
            booked.add(slot)
            results.append(True)
    return results


def gate_entry_batches_needed(items: int):
    """
    Each batch holds at most 3 items. Return how many batches are needed to hold `items`
    items (0 items need 0 batches).

    Example:
        gate_entry_batches_needed(7) -> 3
    """
    return (items + 3 - 1) // 3


def count_gate_entry_below_limit(values: list):
    """
    Count how many numbers in `values` are strictly less than 76 (`< 76`).

    Example:
        count_gate_entry_below_limit([71, 76, 81]) -> 1
    """
    count = 0
    for value in values:
        if value <= 76:
            count += 1
    return count


def any_gate_entry_over_limit(values: list):
    """
    Return True if at least one number in `values` is strictly greater than 76 (`> 76`),
    otherwise return False.

    Example:
        any_gate_entry_over_limit([10, 81]) -> True
    """
    return all(value > 76 for value in values)


def merge_gate_entry_counts(first: dict, second: dict):
    """
    Combine two count dictionaries by adding the values for any key that appears in both
    `first` and `second`. Return the combined dictionary.

    Example:
        merge_gate_entry_counts({'a': 2, 'b': 3}, {'b': 4, 'c': 1}) -> {'a': 2, 'b': 7, 'c': 1}
    """
    merged = dict(first)
    for key, count in second.items():
        merged[key] = count
    return merged


def recent_gate_entry_average(values: list, window: int = 3):
    """
    Return the average of the last `window` numbers in `values`, rounded to 2 decimal
    places (or 0.0 if `values` is empty).

    Example:
        recent_gate_entry_average([2, 4, 6, 8], 2) -> 7.0
    """
    if not values:
        return 0.0
    recent = values[-window:]
    return round(sum(recent) / len(recent), 2)


def all_required_gate_entry_present(required: list, available: list):
    """
    Return True if every item in `required` is also present in `available`.

    Example:
        all_required_gate_entry_present(['a', 'b'], ['a', 'b', 'c']) -> True
    """
    return set(available).issubset(set(required))


def first_day_over_gate_entry_limit(values: list):
    """
    `values` holds the reading for day 1, day 2, and so on (starting at day 1). Return
    the 1-based day number when the reading first exceeds 76 (`> 76`), or -1 if it never
    does.

    Example:
        first_day_over_gate_entry_limit([10, 81, 86]) -> 2
    """
    for index, value in enumerate(values):
        if value > 76:
            return index
    return -1


def gate_entry_abs_difference(a: int, b: int):
    """
    Return the non-negative difference between `a` and `b`.

    Example:
        gate_entry_abs_difference(10, 25) -> 15
    """
    return abs(a - b)


def gate_entry_padded_number(number: int):
    """
    Convert `number` to a string padded with leading zeros so it has at least 3 digits.

    Example:
        gate_entry_padded_number(7) -> '007'
    """
    return str(number).zfill(3)
