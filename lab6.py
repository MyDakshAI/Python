class OrderedList:
    def __init__(self, items=None):
        self._L = sorted(list(items)) if items is not None else []

    def add(self, item):
        self._L.append(item)
        self._L.sort()

    def remove(self, item):
        if item not in self:
            raise RuntimeError(f"{item} not in OrderedList")
        self._L.remove(item)

    def __getitem__(self, index):
        return self._L[index]

    def __iter__(self):
        return iter(self._L)

    def __len__(self):
        return len(self._L)

    def __contains__(self, item):
        return self._bs(item, 0, len(self._L))

    def _bs(self, item, left, right):
        if left >= right:
            return False
        mid = (left + right) // 2
        if self._L[mid] == item:
            return True
        elif item < self._L[mid]:
            return self._bs(item, left, mid)
        else:
            return self._bs(item, mid + 1, right)
