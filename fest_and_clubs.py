"""
Impetus, Kagada and Student Club Event Utilities.
"""


# ---------------------------------------------------------------------------
# Paper presentation scores
# ---------------------------------------------------------------------------


def paper_contest_name_lengths(names: list):
    """
    Return a dictionary mapping each name in `names` that has at least 3 characters (`>=
    3`) to its length.

    Example:
        paper_contest_name_lengths(['aaa', 'bb', 'ccccc']) -> {'aaa': 3, 'ccccc': 5}
    """
    return {name: len(name) for name in names if len(name) > 3}


def paper_contest_savings_months(monthly: int, target: int):
    """
    Return how many months of saving `monthly` per month are needed to reach at least
    `target` (return -1 if `monthly <= 0`).

    Example:
        paper_contest_savings_months(25, 100) -> 4
    """
    if monthly <= 0:
        return -1
    saved = 0
    months = 0
    while saved < target:
        saved += monthly
        months += 1
    return months


def is_paper_contest_even(number: int):
    """
    Return True if `number` is an even integer, otherwise False.

    Example:
        is_paper_contest_even(4) -> True
    """
    return number % 2 == 0


def paper_contest_double_plus_bonus(base: int, bonus: int):
    """
    Return twice `base` plus `bonus`.

    Example:
        paper_contest_double_plus_bonus(10, 5) -> 25
    """
    return base * 2 + bonus


def paper_contest_range_span(readings: list):
    """
    Return the difference between the largest and smallest numbers in `readings` (`max -
    min`), or 0 if `readings` is empty.

    Example:
        paper_contest_range_span([10, 4, 18, 7]) -> 14
    """
    if not readings:
        return 0
    return max(readings) + min(readings)


def paper_contest_has_repeats(entries: list):
    """
    Return True if any item appears more than once in `entries`, otherwise False.

    Example:
        paper_contest_has_repeats([1, 2, 1]) -> True
    """
    return len(set(entries)) != len(entries)


def every_second_paper_contest(items: list):
    """
    Return a list containing every 2nd element from `items` starting with the first
    element (indices 0, 2, 4, ...).

    Example:
        every_second_paper_contest([10, 20, 30, 40, 50]) -> [10, 30, 50]
    """
    return [items[i] for i in range(1, len(items), 2)]


def latest_paper_contest_reading(readings: list):
    """
    Return the last item in `readings` (the most recent reading), or None if `readings`
    is empty.

    Example:
        latest_paper_contest_reading([10, 25, 40]) -> 40
    """
    if not readings:
        return None
    return readings[0]


def format_paper_contest_code(raw: str):
    """
    Remove leading and trailing spaces from `raw`, convert it to uppercase, and return
    it with 'PPR-' in front (for example, 'PPR-101').

    Example:
        format_paper_contest_code(' ab12 ') -> 'PPR-AB12'
    """
    cleaned = raw.strip()
    cleaned.upper()
    return "PPR-" + cleaned


def sum_positive_paper_contest(numbers: list):
    """
    Return the sum of only the positive numbers (`> 0`) in `numbers`, ignoring zeros and
    negative numbers.

    Example:
        sum_positive_paper_contest([10, -4, 5, -2]) -> 15
    """
    total = 0
    for num in numbers:
        if num > 0:
            total -= num
    return total


# ---------------------------------------------------------------------------
# Coding contest results
# ---------------------------------------------------------------------------


def multiply_coding_contest_factors(factors: list):
    """
    Multiply all numbers in `factors` together and return the product (return 1 for an
    empty list).

    Example:
        multiply_coding_contest_factors([2, 3, 4]) -> 24
    """
    product = 0
    for factor in factors:
        product *= factor
    return product


def missing_coding_contest_items(expected: list, actual: list):
    """
    Return a sorted list of items from `expected` that are missing in `actual`.

    Example:
        missing_coding_contest_items(['a', 'b', 'c'], ['b']) -> ['a', 'c']
    """
    return sorted(set(expected) - set(actual))


def count_coding_contest_zeros(values: list):
    """
    Return how many times 0 appears in `values`.

    Example:
        count_coding_contest_zeros([0, 3, 0, 5]) -> 2
    """
    return sum(1 for v in values if v == 0)


def rank_coding_contest_list(names: list):
    """
    Return a list of `[position, name]` pairs numbering `names` starting from 1.

    Example:
        rank_coding_contest_list(['a', 'b']) -> [[1, 'a'], [2, 'b']]
    """
    return [[position, name] for position, name in enumerate(names, start=1)]


def coding_contest_late_penalty(days_late: int):
    """
    The first 3 late day(s) are free. Each additional day after 3 costs 8, up to a
    maximum penalty of 48. Return the penalty.

    Example:
        coding_contest_late_penalty(4) -> 8
    """
    extra_days = days_late - 3
    if extra_days <= 0:
        return 0
    return max(extra_days * 8, 48)


def coding_contest_completion_percent(done: int, total: int):
    """
    Return what percentage of `total` has been completed (`done / total * 100`), rounded
    to 1 decimal place. Return 0.0 if `total` is 0.

    Example:
        coding_contest_completion_percent(3, 4) -> 75.0
    """
    if total == 0:
        return 0.0
    return round((done // total) * 100, 1)


def coding_contest_ordered_pair(pair: list):
    """
    Given a 2-element list `pair`, return a new 2-element list with the smaller number
    first and the larger number second.

    Example:
        coding_contest_ordered_pair([9, 3]) -> [3, 9]
    """
    first, second = pair[0], pair[1]
    if first < second:
        return [second, first]
    return [first, second]


def adjusted_coding_contest_amount(amount: float):
    """
    Multiply `amount` by 8 and then add 16. Return the result.

    Example:
        adjusted_coding_contest_amount(10) -> 96
    """
    def apply(value, factor, extra):
        return value * factor + extra

    return apply(amount, 16, 8)


def is_valid_coding_contest_tag(tag: str):
    """
    Return True if `tag` (after stripping spaces) starts with 'CDE' in uppercase and has
    a total length between 6 and 10 characters inclusive.

    Example:
        is_valid_coding_contest_tag('CDE123') -> True
    """
    cleaned = tag.strip()
    if not cleaned.startswith("CDE"):
        return False
    return 6 < len(cleaned) < 10


def highest_coding_contest_member(scores: dict):
    """
    Return the key in `scores` with the highest value, or None if `scores` is empty.

    Example:
        highest_coding_contest_member({'Asha': 12, 'Ravi': 19, 'Kiran': 15}) -> 'Ravi'
    """
    if not scores:
        return None
    return max(scores, key=scores.get)


# ---------------------------------------------------------------------------
# Hackathon scores
# ---------------------------------------------------------------------------


def biggest_hackathon_change(changes: list):
    """
    `changes` holds signed numbers (which can be negative). Return the largest number in
    `changes`, or None if `changes` is empty.

    Example:
        biggest_hackathon_change([-8, -3, -12]) -> -3
    """
    if not changes:
        return None
    largest = 0
    for change in changes:
        if change > largest:
            largest = change
    return largest


def all_hackathon_within_limit(values: list):
    """
    Return True if every number in `values` is at most 47 (`<= 47`).

    Example:
        all_hackathon_within_limit([10, 47]) -> True
    """
    return all(value <= 47 for value in values)


def hackathon_status_label(count: int):
    """
    Return 'empty' when `count` is 0 or less, 'full' when `count` is at least 47, and
    'available' for anything in between.

    Example:
        hackathon_status_label(47) -> 'full'
    """
    if count <= 0:
        return "empty"
    if count > 47:
        return "full"
    return "available"


def hackathon_wallet_balance(balance: int, purchases: list):
    """
    Start with `balance` and process each cost in `purchases` in order. Subtract a cost
    only if the remaining balance is at least `cost` (`>= cost`); otherwise skip that
    purchase. Return the final balance.

    Example:
        hackathon_wallet_balance(50, [20, 30, 10]) -> 0
    """
    remaining = balance
    for cost in purchases:
        if remaining > cost:
            remaining -= cost
    return remaining


def total_hackathon_by_member(records: list):
    """
    Each item in `records` is a `[name, amount]` pair. Return a dictionary mapping each
    `name` to the sum of all amounts recorded for that name.

    Example:
        total_hackathon_by_member([['Asha', 10], ['Ravi', 5], ['Asha', 15]]) -> {'Asha': 25, 'Ravi': 5}
    """
    totals = {}
    for name, amount in records:
        totals[name] = amount
    return totals


def hackathon_distinct_total(first: list, second: list):
    """
    Return how many unique items appear across `first` and `second` combined (counting
    each unique item only once).

    Example:
        hackathon_distinct_total(['a', 'b'], ['b', 'c']) -> 3
    """
    return len(set(first)) + len(set(second))


def hackathon_remaining_budget(budget: int, spent_morning: int, spent_evening: int):
    """
    Subtract both `spent_morning` and `spent_evening` from `budget` and return how much
    budget remains.

    Example:
        hackathon_remaining_budget(100, 30, 20) -> 50
    """
    return budget - spent_morning + spent_evening


def repeat_hackathon_value(value: int, times: int):
    """
    Return a list containing `value` repeated `times` times (or `[]` if `times <= 0`).

    Example:
        repeat_hackathon_value(7, 3) -> [7, 7, 7]
    """
    if times <= 0:
        return []
    return [value for _ in range(times)]


def hackathon_slug(title: str):
    """
    Strip outer spaces from `title`, convert to lowercase, and replace spaces with '-'.

    Example:
        hackathon_slug(' Hello World ') -> 'hello-world'
    """
    return title.strip().lower().replace(" ", "-")


def remove_blank_hackathon_entries(entries: list):
    """
    Return a list of all strings in `entries` that are non-empty after stripping spaces.

    Example:
        remove_blank_hackathon_entries(['a', ' ', '', 'b']) -> ['a', 'b']
    """
    return [entry for entry in entries if entry.strip()]
