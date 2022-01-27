class HitCounter:

    def __init__(self):
        
        self.hit_counter={}
        
        

    def hit(self, timestamp: int) -> None:
        
        if timestamp not in self.hit_counter:
            self.hit_counter[timestamp]=1
        else:
            self.hit_counter[timestamp]+=1
            
        

    def getHits(self, timestamp: int) -> int:
        
        count=0
        
        for tstamp,hits in self.hit_counter.items():
            
            if((timestamp-tstamp)<300):
                count+=hits
        
        return count
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)