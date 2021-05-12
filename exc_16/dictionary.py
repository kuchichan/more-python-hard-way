from exc_13.dllist.dllist.double_linked_list import DoubleLinkedList 

class Dictionary(object):    
    
    def __init__(self, num_buckets=256) -> None:
        """Initializes a Map with the given numbers of buckets"""
        self.map = DoubleLinkedList()
        for i in range(0, num_buckets):
            self.map.push(DoubleLinkedList())


    def hash_key(self, key):
        """ Given a key this will create a number and then convert it to an index for the aMap's buckets."""
        return hash(key) % self.map.count()

    def get_bucket(self, key):
        """ Given a key, find the bucket where it would go."""
        bucket_id = self.hash_key(key)
        return self.map.get(bucket_id)


    def get_slot(self, key, default=None):
        """ 
        Returns either the bucket and node of a slot or None
        """
        bucket = self.get_bucket(key)
        if bucket:
            node = bucket.begin
            i = 0 

            while node:
                if key == node.value[0]:
                    return bucket, node
                else:
                    node = node.next_
                    i += 1

        return bucket, None 
    
    def get(self, key, default=None):
        bucket, node = self.get_slot(key, default=default)
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
            k, v = node.value
            if key == k:
                bucket.detach_node(node)
                break

    def list(self):
        bucket_node = self.map.begin

        while bucket_node:
            slot_node = bucket_node.value.begin
            while slot_node:
                print(slot_node.value)
                slot_node = slot_node.next_
            bucket_node = bucket_node.next_
