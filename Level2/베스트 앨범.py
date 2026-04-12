
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
    
# 모범 답안
from collections import Counter, defaultdict

def solution(genres, plays):
    answer = []
    
    # 1. 장르별 총 재생 수
    genre_count = Counter()
    for g, p in zip(genres, plays):
        genre_count[g] += p
    
    # 2. 장르 정렬 (핵심)
    sorted_gen = sorted(genre_count, key=lambda x: genre_count[x], reverse=True)
    
    # 3. 장르별 노래 정리
    songs = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        songs[g].append((p, i))
    
    # 4. 장르별 정렬
    for g in songs:
        songs[g].sort(key=lambda x: (-x[0], x[1]))
    
    # 5. 최대 2개씩 담기
    for g in sorted_gen:
        answer.extend([idx for _, idx in songs[g][:2]])
    
    return answer
    

    
        
    
