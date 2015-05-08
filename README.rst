#############
IS210 Midterm
#############
***************************
Programming Examination
***************************

:College: CUNY School of Professional Studies
:Course-Name: Software Application Programming I
:Course-Code: IS 210
:Student-Name: Youqing Xiang
:Created-Date: 2015-03-27

Overview
=========

This midterm task aims to create function which should filter out players with bad connections and produce the lists of players, segregated into the appropriate teams.

My strategy
===========

I broke the whole task into two functions. 

1. First function named **filter_list()** that takes three parameters, in order:
  
  1) players(a list): a list of tuples of usernames and connection strength  for each users.
    
  2) teams(int): the number of teams to build for this game, defaults to 3.
    
  3) max_team(int, optional): the maxium number of players per team, default to None.
    
  By using this function, I am able to fiter out players with bad connections.
    
2. The other function named **matchmaking()** that takes four parameters, in order:
  
  1) players(a list): a list of tuples of usernames and connection strengty for each users.
    
  2) teams(int): the number of teams to build for this game, defaults to 3.
    
  3) min_team(int, optional): the minimum numbe of players per team, default to 1.
    
  4) max_team(int, optional): the maxium number of players per team, default to None.
    
  In this function, I use the previous ''filter_list()'' function to create a list with qualified players and then I
  assigned them into appropriate teams.

My examples
============

.. code:: pycon

    >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
    >>> matchmaking(players, teams=1, min_team=1, max_team=1)
    [['a']]
    
    >>> players =  [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
    >>> matchmaking(players, teams=1, min_team=1)
    [['a', 'c', 'd', 'e', 'f']]
