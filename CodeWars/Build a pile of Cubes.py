def cub_bricks(given_V):
    volume = 0
    n = 0
    while volume < given_V:
        n += 1
        volume += n ** 3
    
    if volume == given_V:
        return n
    return -1

print(cub_bricks(1071225))