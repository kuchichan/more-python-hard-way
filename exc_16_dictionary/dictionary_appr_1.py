from ..exc_13_double_linked_list.double_linked_list.dl_list import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256) -> None:
        self.map_ = DoubleLinkedList()
        for _ in range(num_buckets):
            self.map_.push(DoubleLinkedList())


    def get_hash(self, key):
        return hash(key) % self.map_.count()

    def get_bucket(self, key):
        bucket_num = self.get_hash(key)
        return self.map_.get(bucket_num)

    def get_slot(self, key, default=None):
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin

            while node:
                if node.value[0] == key:
                    return bucket, node
                else:
                    node = node.next_

        return bucket, None

    def get(self, key, default=None):
        bucket, slot = self.get_slot(key, default=default)
        return slot and slot.value[1] or default

    def set(self, key, value):
        bucket, slot = self.get_slot(key)
        if slot:
            slot.value = (key, value)
        else:
            bucket.push((key, value))

    def delete(self, key):
        bucket = self.get_bucket(key)

        node = bucket.begin
        while node:
            if node.value[0] == key:
                bucket.detach(node)
                break

    def list(self):
        map_begin = self.map_.begin
        while map_begin:
            bucket_begin = map_begin.value.begin
            while bucket_begin:
                print(bucket_begin.value)
                bucket_begin = bucket_begin.next_
            map_begin = map_begin.next_
