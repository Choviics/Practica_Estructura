MAX_TABLE_SIZE = 1024*1024		
TRUE = 1
FALSE = 0

import random


class HashNode:
    def __init__(self):
        self.next = None
        self.key = None
        self.value = None
        self.is_occupied = False


class HashTable:
    def __init__(self):
        self.table = [None] * MAX_TABLE_SIZE



def jshash(key, key_len):
    hash_value = 1315423911
    for i in range(key_len):
        hash_value ^= ((hash_value << 5) + ord(key[i]) + (hash_value >> 2))
    return hash_value


def init_hs_node(node):
    node.next = None
    node.key = None
    node.value = None
    node.is_occupied = FALSE


def create_hash_table():
    hs_table = HashTable()
    hs_table.table = [HashNode() for _ in range(MAX_TABLE_SIZE)]
    return hs_table


def add_node_to_hash_table(hs_table, key, key_len, value):
    if not hs_table or not key:
        print("Something is None")
        return -1

    i = jshash(key, key_len) % MAX_TABLE_SIZE
    p = hs_table.table[i]
    pri = p

    while p:
        if key == p.key:
            if p.is_occupied:
                p.value = value
                p.is_occupied = TRUE
                break
        pri = p
        p = p.next

    if not p:
        tmp = HashNode()
        init_hs_node(tmp)
        tmp.key = key[:key_len]
        tmp.value = value
        tmp.is_occupied = TRUE

        if not pri:
            hs_table.table[i] = tmp
        else:
            pri.next = tmp

    return 0


def get_value_from_hash_table(hs_table, key, key_len):
    if not hs_table or not key:
        print("Something is None")
        return None

    i = jshash(key, key_len) % MAX_TABLE_SIZE
    tmp = hs_table.table[i]

    while tmp:
        if key == tmp.key:
            return tmp.value
        tmp = tmp.next

    return None


def hash_table_delete(hs_table):
    if hs_table:
        if hs_table.table:
            for i in range(MAX_TABLE_SIZE):
                p = hs_table.table[i]
                q = None
                while p:
                    q = p.next
                    p.is_occupied = FALSE
                    p = q
            hs_table.table = None
        hs_table = None


class Com:
    def __init__(self):
        self.name = ""
        self.price = 0.0


def printf_com_info(com):
    print("name=%s\tprice=%.1f" % (com.name, com.price))


if __name__ == "__main__":
    hs_table = create_hash_table()
    if not hs_table:
        print("Failed to create hash table")
        exit(-1)
    
    name = [0] * 32
    for i in range(100):
        tmp_com = Com()
        tmp_com.name = f"com{i}"
        tmp_com.price = random.randint(0, 999)
        
        add_node_to_hash_table(hs_table, tmp_com.name, len(tmp_com.name), tmp_com)
    
    for i in range(100):
        name = f"com{i}"
        get_com = get_value_from_hash_table(hs_table, name, len(name))
        if get_com:
            printf_com_info(get_com)
    
    hash_table_delete(hs_table)