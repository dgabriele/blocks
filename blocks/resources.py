import pybiz


class Block(pybiz.BizObject):
    x = pybiz.Int(default=0, nullable=False)
    y = pybiz.Int(default=0, nullable=False)
    w = pybiz.Int(default=1, nullable=False)
    h = pybiz.Int(default=1, nullable=False)
    c = pybiz.List(pybiz.Int(), default=[0, 0, 0, 0])

    @property
    def rect(self):
        return [self.x, self.y, self.w, self.h]

    @property
    def color(self):
        return self.c
