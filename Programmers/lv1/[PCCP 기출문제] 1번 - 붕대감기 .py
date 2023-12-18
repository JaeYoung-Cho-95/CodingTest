def solution(bandage, health, attacks):
    health_std = health
    from collections import deque
    attacks = deque(attacks)
    last_attack_time, last_attack_damage = attacks[-1]
    count_heal, amount_heal, bonus_heal = bandage
    
    time, cnt_heal = 1, 0
    while True:
        attack_time, attack_damage = attacks[0]
        if attack_time == time:
            attack_time, attack_damage = attacks.popleft()
            health -= attack_damage
            cnt_heal = 0
        
        else:
            cnt_heal += 1
            if cnt_heal == count_heal:
                health += bonus_heal
                cnt_heal = 0
            health += amount_heal
        
        if health > health_std:
            health = health_std
        
        if health <= 0:
            health = -1
            break
        
        time += 1
        if time > last_attack_time:
            break
            
    return health