import os
from uuid import uuid4


def uuid_upload_to(instance, filename):
    uuid_name = uuid4().hex
    ext = os.path.splitext(filename)[-1].lower()
    return '/'.join([  # 역슬래시로 안해도 괜찮음(python 내부에서 처리라)
        uuid_name[:2],  # 256가지 조합
        uuid_name[2:4],
        uuid_name[4:] + ext
    ])
