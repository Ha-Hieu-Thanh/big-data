from elasticsearch import Elasticsearch, exceptions as es_exceptions

# Kết nối đến Elasticsearch
es = Elasticsearch(['http://localhost:9200'])

# Định nghĩa mapping cho index
mapping = {
    "mappings": {
        "properties": {
            "time": {"type": "date"},
            "open": {"type": "integer"},
            "high": {"type": "integer"},
            "low": {"type": "integer"},
            "close": {"type": "integer"},
            "volume": {"type": "integer"},
            "ticker": {"type": "keyword"}
        }
    }
}

# mapping = {
#     "mappings": {
#         "properties": {
#             "borough": {"type": "keyword"},
#             "cuisine": {"type": "keyword"},
#             "grades": {
#                 "type": "nested",
#                 "properties": {
#                     "grade": {"type": "keyword"},
#                     "score": {"type": "integer"}
#                 }
#             },
#             "name": {"type": "text"},
#             "restaurant_id": {"type": "keyword"}
#         }
#     }
# }

# Tạo index với mapping được định nghĩa và kiểm tra kết quả
index_name = "data_demo2"
try:
    result = es.indices.create(index=index_name, body=mapping)
    if result["acknowledged"]:
        print(f"Mapping cho index '{index_name}' đã được tạo thành công.")
    else:
        print(f"Không thể tạo mapping cho index '{index_name}'.")
except es_exceptions.RequestError as e:
    print(f"Lỗi khi tạo mapping cho index '{index_name}': {e}")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")