from CodingBlog59_SerializeDeserialize.utils.JsonFactory import JsonFactory


@JsonFactory.register
class Categories(object):
    def __init__(self,categories=None):
        if categories == None:
            self.categories=[]
        else:
            self.categories=categories
    def add_cate(self,cate):
        self.categories.append(cate)
    def print_all_categories(self):
        for cate in self.categories:
            print("%"*25)
            print(cate)
            print("-" * 25)
            for p in cate.products:
                print(p)