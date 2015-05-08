#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module to build teams with qualified players."""


def filter_list(players, teams=3, max_team=None):
    """A function to filter out players and produce the lists of players.

    Args:
        players(a list): a list of tuples of usernames and connection strength
        for each users.
        teams(int): the number of teams to build for this game, defaults to 3.
        max_team(int, optional): the maxium number of players per team, default
        to None.

    Returns: a list of players.

    Examples:

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 0), ('e', 1)]
        >>> filter_list(players, teams=2, max_team=None)
        ['a', 'c', 'e']
    """
    players_list = []
    for player in players:
        if max_team is not None and player[1] is 1:
            while len(players_list) <= teams * max_team:
                players_list.append(player[0])
        elif max_team is None and player[1] is 1:
            players_list.append(player[0])
    return players_list


def matchmaking(players, teams=3, min_team=1, max_team=None):
    """A function to produce a list of players, segregated into the teams.

    Args:
        players(a list): a list of tuples of usernames and connection strength
        for each users.
        teams(int): the number of teams to build for this game, defaults to 3.
        min_team(int, optional): the minimum numbe of players per team, default
        to 1.
        max_team(int, optional): the maxium number of players per team, default
        to None.

    Returns: a list of players, segregated into the teams.

    Examples:

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 0), ('e', 1)]
        >>> matchmaking(players, teams=2, min_team=1, max_team=None)
        [['a'], ['c']]
    """
    players_list = filter_list(players, teams=3, max_team=None)
    possible_team = (len(players_list)-(len(players_list)) % teams)/teams
    game = [[] for i in range(teams)]
    if (max_team is not None and max_team >= possible_team >= min_team) \
       or (max_team is None and possible_team >= min_team):
        players_number = teams * possible_team
        actual_players = players_list[0:players_number]
        for player in actual_players:
            i = (actual_players.index(player)) % teams
            game[i].append(player)
        return game
    elif max_team is not None and possible_team > max_team:
        players_number = teams * max_team
        actual_players = players_list[0:players_number]
        for player in actual_players:
            i = (actual_players.index(player)) % teams
            game[i].append(player)
        return game
    else:
        return False
