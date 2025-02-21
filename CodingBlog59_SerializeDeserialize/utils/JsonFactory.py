import json

class JsonFactory(object):
    mappings={}
    @classmethod #cls instead of self -> access class attributes only

    def class_mapper(clsself,d): #Tìm lớp cls phù hợp để khôi phục obj từ json
        for keys, cls in clsself.mappings.items():
            if keys.issuperset(d.keys()):
                return cls(**d)
        else:
            raise ValueError('Unable to find a matching class for object: {!s}.format(d)')

    @classmethod
    def complex_handler(clsself,Obj): #Xử lý objs ko chuyển thành json trực tiếp
        if hasattr(Obj,'__dict__'): #Check obj có thuộc tính dic
            return Obj.__dict__ #Dic chứa dữ liệu obj
        else:
            raise TypeError('Object of type %s with value of %s is not JSON serializable' % (type(Obj),repr(Obj)))

    @classmethod
    def register(clsself,cls): #Các lớp obj đăng ký Serialize và Deserialize
        clsself.mappings[frozenset(tuple([attr for attr,val in cls().__dict__.items()]))] = cls
        return cls

    @classmethod
    def parse_json(clsself, obj): #Chuyển đổi obj py --> json
        return json.dumps(obj.__dict__, default=clsself.complex_handler, indent=4)
                #json.dumps: chuyển objs py --> str json

    @classmethod
    def restore_object(clsself, json_str): #Chuyển đổi json --> obj py
        return json.loads(json_str, object_hook=clsself.class_mapper)
                #json.loads: chuyển str json --> objs py

    @classmethod
    def serialize(clsself, obj, path): #Lưu obj xuống ROM dạng .json
        with open(path, 'w') as jfile:
            jfile.writelines([clsself.parse_json(obj)])
        return path

    @classmethod
    def deserialize(clsself, filepath): #Hồi phục obj từ .json trong ROM
        result = None
        with open(filepath, 'r') as jfile:
            result = clsself.restore_object(jfile.read())
        return result
