def solution(players, callings):
    players_num = {player:rank for rank,player in enumerate(players)}
    num_players = {rank:player for rank,player in enumerate(players)}
    
    from collections import deque
    callings = deque(callings)

    while callings:
        called_person = callings.popleft()
        
        called_person_rank = players_num[called_person]
        faster_person = num_players[called_person_rank-1]
        
        players_num[called_person] = called_person_rank-1
        players_num[faster_person] = called_person_rank

        num_players[called_person_rank] = faster_person
        num_players[called_person_rank-1] = called_person
    
    return list(num_players.values())