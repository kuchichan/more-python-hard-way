from exc_13.dllist.dllist.double_linked_list import DoubleLinkedList

class Dictionary(object):
    def __init__(self, num_buckets=256) -> None:
        self.map = DoubleLinkedList()
        for _ in range(num_buckets):
            self.map.push(DoubleLinkedList())

    def hash_key(self, key):
        return hash(key) % self.map.count() 

    def get_bucket(self, key):
        bucket_num = self.hash_key(key)
        return self.map.get(bucket_num)

    def get_slot(self, key, default=None):
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin

            while node:
                if node.value[0] == key:
                    return bucket, node 

                node = node.next_

        return bucket, None 

    def get(self, key, default=None):
        bucket, node = self.get_slot(key, default)
        return node and node.value[1] or default 

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
            node = node.next_


    def list(self):
        map_begin = self.map.begin
        while map_begin:
            bucket_begin = map_begin.value.begin
            while bucket_begin:
                print(bucket_begin.value)
                bucket_begin = bucket_begin.next_
            map_begin = map_begin.next_
                
    
