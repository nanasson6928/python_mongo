from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 방법 1
# print(db.movies.find({'title' : '사운드 오브 뮤직'}).pretty())
# AttributeError: 'Cursor' object has no attribute 'pretty' : pretty 메소드가 없어서 생긴 에러
# --> x (MongoDB에 관한 강좌)

# 방법 2
# data = db.movies.find({'title' : '사운드 오브 뮤직'})
# print(list(data))

# 방법 3
# target_movie = db.movies.find({'title' : '사운드 오브 뮤직'})
# print(target_movie)

# print(type(target_movie))
# print(type(data))


# find - 조건 조회
# 사운드 오브 뮤직의 평점과 같은 영화 조회하기

# 설계 tip
# input - 영화, 평점
# output - 영화
# logic - for문, if문 등등
