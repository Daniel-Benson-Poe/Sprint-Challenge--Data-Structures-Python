class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list = []  # create empty list to keep track of values and length
        self.iter = 0  # create iterator to keep track of index that holds the oldest value

    def append(self, item):
        if len(self.list) >= self.capacity:  # check if length of list has reached the given capacity
            self.list.remove(self.list[self.iter])  # remove the oldest value in the last based on the iterator
            self.list.insert(self.iter, item)  # insert the new item/value in that same position
            if self.iter < self.capacity-1:  # check if iterator is between the bounds of 0 and capacity-1 exclusive
                self.iter += 1  # increment the iterator by 1
            elif self.iter >= self.capacity-1:  # if the iterator is out of the required bounds
                self.iter = 0  # set iterator back to 0

        else:  # if length of list has not reached the given capacity
            self.list.append(item)  # append the item to the end of the list
            if self.iter < self.capacity-1:  # check if iterator is within the required bounds
                self.iter += 1  # increment iterator by 1
            elif self.iter >= self.capacity-1:  # if iterator not in bounds
                self.iter = 0  # set iterator to 0

    def get(self):
        for i in self.list:  # for each item in the list
            if i is None:  # check if item is None
                self.list.remove(i)  # if item is None, remove the item
        return self.list  # return the list, minus any None values