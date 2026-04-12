
def solution(genres, plays):
    answer = []
    hash_set={}
    index_list=[]
    for gen,ply in zip(genres,plays):
        hash_set[gen]=hash_set.get(gen,0)+ply # 장르별 총 play 수 딕셔너리 구현
    sorted_gen = sorted(hash_set, key= lambda x: hash_set[x], reverse=True)
    
    songs = {}
    for i, (gen, ply) in enumerate(zip(genres, plays)):
        songs.setdefault(gen, []).append((ply, i)) # 키가 장르고 값이 (플레이수,고유번호)
    
    for gen in songs:
        songs[gen].sort(key=lambda x: (-x[0],x[1])) # 플레이수 기준으로 내림차순, 고유번호 기준으로 오름차순(고유번호 낮은 노래가 먼저 수록되기때문)
    for gen in sorted_gen:
        for song in songs[gen][:2]:
            answer.append(song[1])
    return answer
    
from collections import Counter

def solution(genres, plays):
    answer = []
    # for gen,ply in zip(genres,plays):
    #     hash_set[gen]=hash_set.get(gen,0)+ply # 장르별 총 play 수 딕셔너리 구현
    # sorted_gen = sorted(hash_set, key= lambda x: hash_set[x], reverse=True)
    hash_set = Counter()
    for gen, ply in zip(genres,plays):
        hash_set[gen] += ply # Counter 쓰면 .get()도 필요 없음 없으면 0 반환
    sorted_gen = sorted(hash_set,key = lambda gen : hash_set[gen], reverse=True)
    
    songs = {}
    for i, (gen, ply) in enumerate(zip(genres, plays)):
        songs.setdefault(gen, []).append((ply, i)) # 키가 장르고 값이 (플레이수,고유번호)
    
    for gen in songs:
        songs[gen].sort(key=lambda x: (-x[0],x[1])) # 플레이수 기준으로 내림차순, 고유번호 기준으로 오름차순(고유번호 낮은 노래가 먼저 수록되기때문)
    for gen in sorted_gen:
        for song in songs[gen][:2]:
            answer.append(song[1])
    return answer
    
    

    
        
    
