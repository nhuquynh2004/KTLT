from CodingBlog59_SerializeDeserialize.utils.JsonFactory import JsonFactory


@JsonFactory.register #Decorator: Gọi register(cls) tự động
class Product(object):
    def __init__(self,product_id=None,product_name=None,unit_price=None):
        self.product_id=product_id
        self.product_name=product_name
        self.unit_price=unit_price
    def __str__(self):
        return f"{self.product_id}\t{self.product_name}\t{self.unit_price}"

'''
register(cls): Lấy ds thuộc tính của lớp Product (product_id, product_name, unit_price và lưu vào dic mappings
Khi JsonFactory cần tạo lại đối tượng từ JSON -> dùng class_mapper để tìm lớp phù hợp trong dic mappings
'''

'''
Coding tương đương:
from...
class Product():
    ...
Product=JsonFactory.register(Product)
'''

