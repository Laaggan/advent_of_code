# tests/test_ranges.py

# from day5_2 import solution, Range, pretty_print_ranges
from day5_4 import solution, Range, pretty_print_ranges

def test_removing_subsets_yields_single_range():
    data = '''1-10
    2-3
    6-7

    1
    '''
    assert solution(data) == [Range(1,10)]

def test_removing_subsets_yields_multiple_range():
    data = '''1-10
    2-3
    6-7
    12-15

    1
    '''
    assert solution(data) == [Range(1,10), Range(12,15)]

def test_subset_same_start():
    data = '''1-10
    1-5
    1-3
    12-15

    1
    '''
    assert solution(data) == [Range(1,10), Range(12,15)]

def test_subset_same_start():
    data = '''1-2
    2-3
    3-4
    4-5

    1
    '''
    assert solution(data) == [Range(1,5)]

def test_merging():
    data = '''1-4
    3-7
    6-10

    1
    '''
    assert solution(data) == [Range(1,10)]

def test_sample_input():
    data = '''3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32'''
    assert solution(data) == [Range(3,5), Range(10, 20)]

def test_merge_two_overlapping_ranges():
    data = """3-5
    4-10

    1"""
    sol = solution(data)
    pretty_print_ranges(sol)
    assert sol == [Range(3, 10)]


def test_add_non_intersecting_range():
    data = """3-5
6-10

1"""
    assert solution(data) == [Range(3, 5), Range(6, 10)]


def test_add_then_extend_range():
    data = """3-5
6-10
4-11

1"""
    sol = solution(data)
    pretty_print_ranges(sol)
    assert sol == [Range(3, 11)]


def test_multiple_ranges_with_gap():
    data = """3-5
6-7
8-10
4-11
15-17

# 1"""
    assert solution(data) == [Range(3, 11), Range(15, 17)]


def test_merge_from_behind():
    data = """3-5
1-4

1"""
    assert solution(data) == [Range(1, 5)]

def test_multiple_merged_regions():
    data = """1-2
3-5
4-7
6-9
10-11
12-15
14-17
16-20
21-25

# 1"""
    assert solution(data) == [Range(1, 2), Range(3, 9), Range(10, 11), Range(12, 20), Range(21, 25)]


def test_even_more_multiple_regions():
    data = """1-2
3-5
4-7
6-9
10-11
20-30
25-30
50-55
54-58
16-20
60-80
70-100
120-150

# 1"""
    assert solution(data) == [Range(1, 2), 
                              Range(3, 9),
                              Range(10, 11),
                              Range(16, 30), 
                              Range(50, 58),
                              Range(60, 100),
                              Range(120, 150)]

def test_intersecting_values_are_merged():
    data = '''1-2
    2-3

    1'''

    assert solution(data) == [Range(1,3)]

def test_subset_from_real_data():
    data = '''81372270812981-81736399903236
    81503580676246-81736399903236
    84085152109418-84257649453332
    84085152109418-84790304933533
    85317591943576-85801599011340
    85801599011340-86349113877053
    86822392613517-87129569221834
    87418699689306-88031386175374
    92052411952466-97545773427008
    102126778607251-106245986122913

    1'''
    assert solution(data) == [Range(81372270812981, 81736399903236),
                              Range(84085152109418, 84790304933533),
                              Range(85317591943576, 86349113877053),
                              Range(86822392613517, 87129569221834),
                              Range(87418699689306, 88031386175374),
                                Range(92052411952466, 97545773427008),
                                Range(102126778607251, 106245986122913)]