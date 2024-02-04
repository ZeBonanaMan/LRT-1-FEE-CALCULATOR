

# RAILWAY PRICE CHECKER
#BEEP CARD
def beep_get_fare(source, destination):
    fare_prices = {
        ('roosevelt','roosevelt'): 0 ,
        ('roosevelt','balintawak'): 16 ,
        ('roosevelt','monumento'): 18 ,
        ('roosevelt','5th avenue'): 20 ,
        ('roosevelt','r.papa'): 21 ,
        ('roosevelt','abad santos'): 22 ,
        ('roosevelt','blumentrit'): 23 ,
        ('roosevelt','tayuman'): 23 ,
        ('roosevelt','bambang'): 24 ,
        ('roosevelt','doroteo jose'): 25 ,
        ('roosevelt','carriedo'): 26 ,
        ('roosevelt','central terminal'): 27 ,
        ('roosevelt','united nations'): 28 ,
        ('roosevelt','pedro gil'): 29 ,
        ('roosevelt','quirino'): 30 ,
        ('roosevelt','vito cruz'): 31 ,
        ('roosevelt','gil puyat'): 32 ,
        ('roosevelt','libertad'): 33 ,
        ('roosevelt','edsa'): 34 ,
        ('roosevelt','baclaran'): 35 ,
        ('balintawak','roosevelt'): 16,
        ('balintawak','balintawak'): 0 ,
        ('balintawak','monumento'): 16 ,
        ('balintawak','5th avenue'): 17 ,
        ('balintawak','r.papa'): 18 ,
        ('balintawak','abad santos'): 19 ,
        ('balintawak','blumentrit'): 20 ,
        ('balintawak','tayuman'): 21 ,
        ('balintawak','bambang'): 22 ,
        ('balintawak','doroteo jose'): 23 ,
        ('balintawak','carriedo'): 24 ,
        ('balintawak','central terminal'): 24 ,
        ('balintawak','united nations'): 26 ,
        ('balintawak','pedro gil'): 27 ,
        ('balintawak','quirino'): 28 ,
        ('balintawak','vito cruz'): 29 ,
        ('balintawak','gil puyat'): 30 ,
        ('balintawak','libertad'): 31 ,
        ('balintawak','edsa'): 32 ,
        ('balintawak','baclaran'): 33 ,
        ('monumento','roosevelt'): 18 ,
        ('monumento','balintawak'): 16 ,
        ('monumento','monumento'): 0 ,
        ('monumento','5th avenue'): 15 ,
        ('monumento','r.papa'): 16 ,
        ('monumento','abad santos'): 17 ,
        ('monumento','blumentrit'): 18 ,
        ('monumento','tayuman'): 18 ,
        ('monumento','bambang'): 19 ,
        ('monumento','doroteo jose'): 20 ,
        ('monumento','carriedo'): 21 ,
        ('monumento','central terminal'): 22 ,
        ('monumento','united nations'): 23 ,
        ('monumento','pedro gil'): 24 ,
        ('monumento','quirino'): 25 ,
        ('monumento','vito cruz'): 26,
        ('monumento','gil puyat'): 27 ,
        ('monumento','libertad'): 28 ,
        ('monumento','edsa'): 29 ,
        ('monumento','baclaran'): 30 ,
        ('5th avenue','roosevelt'): 20 ,
        ('5th avenue','balintawak'): 17 ,
        ('5th avenue','monumento'): 15 ,
        ('5th avenue','5th avenue'): 0 ,
        ('5th avenue','r.papa'): 14 ,
        ('5th avenue','abad santos'): 15 ,
        ('5th avenue','blumentrit'): 16 ,
        ('5th avenue','tayuman'): 17 ,
        ('5th avenue','bambang'): 18 ,
        ('5th avenue','doroteo jose'): 19 ,
        ('5th avenue','carriedo'): 20 ,
        ('5th avenue','central terminal'): 20 ,
        ('5th avenue','united nations'): 22 ,
        ('5th avenue','pedro gil'): 23 ,
        ('5th avenue','quirino'): 24 ,
        ('5th avenue','vito cruz'): 25 ,
        ('5th avenue','gil puyat'): 26 ,
        ('5th avenue','libertad'): 27 ,
        ('5th avenue','edsa'): 28 ,
        ('5th avenue','baclaran'): 29 ,
        ('r.papa','roosevelt'): 21 ,
        ('r.papa','balintawak'): 18 ,
        ('r.papa','monumento'): 16 ,
        ('r.papa','5th avenue'): 14 ,
        ('r.papa','r.papa'): 0 ,
        ('r.papa','abad santos'): 14 ,
        ('r.papa','blumentrit'): 15 ,
        ('r.papa','tayuman'): 16 ,
        ('r.papa','bambang'): 17 ,
        ('r.papa','doroteo jose'): 18 ,
        ('r.papa','carriedo'): 18 ,
        ('r.papa','central terminal'): 19 ,
        ('r.papa','united nations'): 21 ,
        ('r.papa','pedro gil'): 22,
        ('r.papa','quirino'): 23 ,
        ('r.papa','vito cruz'): 24 ,
        ('r.papa','gil puyat'): 25 ,
        ('r.papa','libertad'): 26 ,
        ('r.papa','edsa'): 27 ,
        ('r.papa','baclaran'): 28 ,
        ('abad santos','roosevelt'): 22 ,
        ('abad santos','balintawak'): 19 ,
        ('abad santos','monumento'): 17 ,
        ('abad santos','5th avenue'): 15 ,
        ('abad santos','r.papa'): 14 ,
        ('abad santos','abad santos'): 0 ,
        ('abad santos','blumentrit'): 14 ,
        ('abad santos','tayuman'): 15 ,
        ('abad santos','bambang'): 16 ,
        ('abad santos','doroteo jose'): 17 ,
        ('abad santos','carriedo'): 18 ,
        ('abad santos','central terminal'): 18 ,
        ('abad santos','united nations'): 20 ,
        ('abad santos','pedro gil'): 21 ,
        ('abad santos','quirino'): 22 ,
        ('abad santos','vito cruz'): 23 ,
        ('abad santos','gil puyat'): 24 ,
        ('abad santos','libertad'): 25,
        ('abad santos','edsa'): 26 ,
        ('abad santos','baclaran'): 27 ,
        ('blumentrit','roosevelt'): 23 ,
        ('blumentrit','balintawak'): 20 ,
        ('blumentrit','monumento'): 18 ,
        ('blumentrit','5th avenue'): 16 ,
        ('blumentrit','r.papa'): 15 ,
        ('blumentrit','abad santos'): 14 ,
        ('blumentrit','blumentrit'): 0 ,
        ('blumentrit','tayuman'): 14 ,
        ('blumentrit','bambang'): 15 ,
        ('blumentrit','doroteo jose'): 16 ,
        ('blumentrit','carriedo'): 16 ,
        ('blumentrit','central terminal'): 17 ,
        ('blumentrit','united nations'): 19 ,
        ('blumentrit','pedro gil'): 20,
        ('blumentrit','quirino'): 21 ,
        ('blumentrit','vito cruz'): 22,
        ('blumentrit','gil puyat'): 23 ,
        ('blumentrit','libertad'): 24 ,
        ('blumentrit','edsa'): 25 ,
        ('blumentrit','baclaran'): 26 ,
        ('tayuman','roosevelt'): 23,
        ('tayuman','balintawak'): 21,
        ('tayuman','monumento'): 18 ,
        ('tayuman','5th avenue'): 17 ,
        ('tayuman','r.papa'): 16 ,
        ('tayuman','abad santos'): 15 ,
        ('tayuman','blumentrit'): 14 ,
        ('tayuman','tayuman'): 0 ,
        ('tayuman','bambang'): 14 ,
        ('tayuman','doroteo jose'): 15 ,
        ('tayuman','carriedo'): 16 ,
        ('tayuman','central terminal'): 17 ,
        ('tayuman','united nations'): 18 ,
        ('tayuman','pedro gil'): 19 ,
        ('tayuman','quirino'): 20 ,
        ('tayuman','vito cruz'): 21 ,
        ('tayuman','gil puyat'): 22,
        ('tayuman','libertad'): 23 ,
        ('tayuman','edsa'): 24 ,
        ('tayuman','baclaran'): 25 ,
        ('bambang','roosevelt'): 24 ,
        ('bambang','balintawak'): 22 ,
        ('bambang','monumento'): 19 ,
        ('bambang','5th avenue'): 18 ,
        ('bambang','r.papa'): 17 ,
        ('bambang','abad santos'): 16 ,
        ('bambang','blumentrit'): 15 ,
        ('bambang','tayuman'): 14 ,
        ('bambang','bambang'): 0 ,
        ('bambang','doroteo jose'): 14 ,
        ('bambang','carriedo'): 15 ,
        ('bambang','central terminal'): 16 ,
        ('bambang','united nations'): 17 ,
        ('bambang','pedro gil'): 18 ,
        ('bambang','quirino'): 19 ,
        ('bambang','vito cruz'): 20 ,
        ('bambang','gil puyat'): 21 ,
        ('bambang','libertad'): 22 ,
        ('bambang','edsa'): 24 ,
        ('bambang','baclaran'): 24 ,
        ('doroteo jose','roosevelt'): 25,
        ('doroteo jose','balintawak'): 23 ,
        ('doroteo jose','monumento'): 20,
        ('doroteo jose','5th avenue'): 19 ,
        ('doroteo jose','r.papa'): 18 ,
        ('doroteo jose','abad santos'): 17 ,
        ('doroteo jose','blumentrit'): 16 ,
        ('doroteo jose','tayuman'): 15 ,
        ('doroteo jose','bambang'): 14 ,
        ('doroteo jose','doroteo jose'): 0 ,
        ('doroteo jose','carriedo'): 14 ,
        ('doroteo jose','central terminal'): 15 ,
        ('doroteo jose','united nations'): 16 ,
        ('doroteo jose','pedro gil'): 17 ,
        ('doroteo jose','quirino'): 18 ,
        ('doroteo jose','vito cruz'): 19,
        ('doroteo jose','gil puyat'): 21 ,
        ('doroteo jose','libertad'): 22,
        ('doroteo jose','edsa'): 23 ,
        ('doroteo jose','baclaran'): 23 ,
        ('carriedo','roosevelt'): 26 ,
        ('carriedo','balintawak'): 24 ,
        ('carriedo','monumento'): 21 ,
        ('carriedo','5th avenue'): 20 ,
        ('carriedo','r.papa'): 18 ,
        ('carriedo','abad santos'): 18 ,
        ('carriedo','blumentrit'): 16 ,
        ('carriedo','tayuman'): 16 ,
        ('carriedo','bambang'): 15 ,
        ('carriedo','doroteo jose'): 14 ,
        ('carriedo','carriedo'): 0 ,
        ('carriedo','central terminal'): 14 ,
        ('carriedo','united nations'): 16,
        ('carriedo','pedro gil'): 17 ,
        ('carriedo','quirino'): 18 ,
        ('carriedo','vito cruz'): 19 ,
        ('carriedo','gil puyat'): 20 ,
        ('carriedo','libertad'): 21 ,
        ('carriedo','edsa'): 22 ,
        ('carriedo','baclaran'): 23 ,
        ('central terminal','roosevelt'): 27 ,
        ('central terminal','balintawak'): 24 ,
        ('central terminal','monumento'): 22 ,
        ('central terminal','5th avenue'): 20 ,
        ('central terminal','r.papa'): 19 ,
        ('central terminal','abad santos'): 18 ,
        ('central terminal','blumentrit'): 17 ,
        ('central terminal','tayuman'): 17 ,
        ('central terminal','bambang'): 16 ,
        ('central terminal','doroteo jose'): 15 ,
        ('central terminal','carriedo'): 14 ,
        ('central terminal','central terminal'): 0 ,
        ('central terminal','united nations'): 15 ,
        ('central terminal','pedro gil'): 16 ,
        ('central terminal','quirino'): 17 ,
        ('central terminal','vito cruz'): 18 ,
        ('central terminal','gil puyat'): 19 ,
        ('central terminal','libertad'): 20 ,
        ('central terminal','edsa'): 21 ,
        ('central terminal','baclaran'): 22 ,
        ('united nations','roosevelt'): 28,
        ('united nations','balintawak'): 26 ,
        ('united nations','monumento'): 23 ,
        ('united nations','5th avenue'): 22 ,
        ('united nations','r.papa'): 21 ,
        ('united nations','abad santos'): 20 ,
        ('united nations','blumentrit'): 19 ,
        ('united nations','tayuman'): 18 ,
        ('united nations','bambang'): 17 ,
        ('united nations','doroteo jose'): 16 ,
        ('united nations','carriedo'): 16 ,
        ('united nations','central terminal'): 15 ,
        ('united nations','united nations'): 0 ,
        ('united nations','pedro gil'): 14 ,
        ('united nations','quirino'): 15 ,
        ('united nations','vito cruz'): 16 ,
        ('united nations','gil puyat'): 17 ,
        ('united nations','libertad'): 18 ,
        ('united nations','edsa'): 20 ,
        ('united nations','baclaran'): 20 ,
        ('pedro gil','roosevelt'): 29 ,
        ('pedro gil','balintawak'): 27 ,
        ('pedro gil','monumento'): 24 ,
        ('pedro gil','5th avenue'): 23 ,
        ('pedro gil','r.papa'): 22 ,
        ('pedro gil','abad santos'): 21 ,
        ('pedro gil','blumentrit'): 20 ,
        ('pedro gil','tayuman'): 19 ,
        ('pedro gil','bambang'): 18 ,
        ('pedro gil','doroteo jose'): 17 ,
        ('pedro gil','carriedo'): 17 ,
        ('pedro gil','central terminal'): 16 ,
        ('pedro gil','united nations'): 14 ,
        ('pedro gil','pedro gil'): 0 ,
        ('pedro gil','quirino'): 14 ,
        ('pedro gil','vito cruz'): 15 ,
        ('pedro gil','gil puyat'): 17 ,
        ('pedro gil','libertad'): 17 ,
        ('pedro gil','edsa'): 19 ,
        ('pedro gil','baclaran'): 19 ,
        ('quirino','roosevelt'): 30 ,
        ('quirino','balintawak'): 28 ,
        ('quirino','monumento'): 25 ,
        ('quirino','5th avenue'): 24 ,
        ('quirino','r.papa'): 23 ,
        ('quirino','abad santos'): 22,
        ('quirino','blumentrit'): 21 ,
        ('quirino','tayuman'): 20 ,
        ('quirino','bambang'): 19 ,
        ('quirino','doroteo jose'): 18 ,
        ('quirino','carriedo'): 18 ,
        ('quirino','central terminal'): 17,
        ('quirino','united nations'): 15 ,
        ('quirino','pedro gil'): 14 ,
        ('quirino','quirino'): 0 ,
        ('quirino','vito cruz'): 14 ,
        ('quirino','gil puyat'): 16 ,
        ('quirino','libertad'): 16 ,
        ('quirino','edsa'): 18 ,
        ('quirino','baclaran'): 18 ,
        ('vito cruz','roosevelt'): 31 ,
        ('vito cruz','balintawak'): 29 ,
        ('vito cruz','monumento'): 26 ,
        ('vito cruz','5th avenue'): 25 ,
        ('vito cruz','r.papa'): 24 ,
        ('vito cruz','abad santos'): 23 ,
        ('vito cruz','blumentrit'): 22 ,
        ('vito cruz','tayuman'): 21 ,
        ('vito cruz','bambang'): 20 ,
        ('vito cruz','doroteo jose'): 19 ,
        ('vito cruz','carriedo'): 19 ,
        ('vito cruz','central terminal'): 18 ,
        ('vito cruz','united nations'): 16 ,
        ('vito cruz','pedro gil'): 15 ,
        ('vito cruz','quirino'): 14 ,
        ('vito cruz','vito cruz'): 0 ,
        ('vito cruz','gil puyat'): 15 ,
        ('vito cruz','libertad'): 15 ,
        ('vito cruz','edsa'): 17 ,
        ('vito cruz','baclaran'): 17 ,
        ('gil puyat','roosevelt'): 32 ,
        ('gil puyat','balintawak'): 30,
        ('gil puyat','monumento'): 27 ,
        ('gil puyat','5th avenue'): 26 ,
        ('gil puyat','r.papa'): 25 ,
        ('gil puyat','abad santos'): 24 ,
        ('gil puyat','blumentrit'): 23,
        ('gil puyat','tayuman'): 22 ,
        ('gil puyat','bambang'): 21 ,
        ('gil puyat','doroteo jose'): 21 ,
        ('gil puyat','carriedo'): 20 ,
        ('gil puyat','central terminal'): 19,
        ('gil puyat','united nations'): 17 ,
        ('gil puyat','pedro gil'): 17 ,
        ('gil puyat','quirino'): 16 ,
        ('gil puyat','vito cruz'): 15 ,
        ('gil puyat','gil puyat'): 0 ,
        ('gil puyat','libertad'): 14 ,
        ('gil puyat','edsa'): 15 ,
        ('gil puyat','baclaran'): 16 ,
        ('libertad','roosevelt'): 33 ,
        ('libertad','balintawak'): 31 ,
        ('libertad','monumento'): 28 ,
        ('libertad','5th avenue'): 27 ,
        ('libertad','r.papa'): 26 ,
        ('libertad','abad santos'): 25 ,
        ('libertad','blumentrit'): 24 ,
        ('libertad','tayuman'): 23 ,
        ('libertad','bambang'): 22 ,
        ('libertad','doroteo jose'): 22 ,
        ('libertad','carriedo'): 21 ,
        ('libertad','central terminal'): 20 ,
        ('libertad','united nations'): 18 ,
        ('libertad','pedro gil'): 17 ,
        ('libertad','quirino'): 16 ,
        ('libertad','vito cruz'): 15 ,
        ('libertad','gil puyat'): 14 ,
        ('libertad','libertad'): 0 ,
        ('libertad','edsa'): 15 ,
        ('libertad','baclaran'): 15,
        ('edsa','roosevelt'): 34,
        ('edsa','balintawak'): 32 ,
        ('edsa','monumento'): 29 ,
        ('edsa','5th avenue'): 28 ,
        ('edsa','r.papa'): 27 ,
        ('edsa','abad santos'): 26 ,
        ('edsa','blumentrit'): 25 ,
        ('edsa','tayuman'): 24 ,
        ('edsa','bambang'): 24 ,
        ('edsa','doroteo jose'): 23 ,
        ('edsa','carriedo'): 22 ,
        ('edsa','central terminal'): 21 ,
        ('edsa','united nations'): 20 ,
        ('edsa','pedro gil'): 19 ,
        ('edsa','quirino'): 18 ,
        ('edsa','vito cruz'): 17 ,
        ('edsa','gil puyat'): 15 ,
        ('edsa','libertad'): 15,
        ('edsa','edsa'): 0 ,
        ('edsa','baclaran'): 14 ,
        ('baclaran','roosevelt'): 35 ,
        ('baclaran','balintawak'): 33 ,
        ('baclaran','monumento'): 30 ,
        ('baclaran','r.papa'): 28 ,
        ('baclaran','abad santos'): 27 ,
        ('baclaran','blumentrit'): 26 ,
        ('baclaran','tayuman'): 25 ,
        ('baclaran','bambang'): 24 ,
        ('baclaran','doroteo jose'): 23 ,
        ('baclaran','carriedo'): 22 ,
        ('baclaran','central terminal'): 21 ,
        ('baclaran','united nations'): 20 ,
        ('baclaran','pedro gil'): 19 ,
        ('baclaran','quirino'): 18 ,
        ('baclaran','vito cruz'): 17 ,
        ('baclaran','gil puyat'): 16 ,
        ('baclaran','libertad'): 15 ,
        ('baclaran','edsa'): 14 ,
        ('baclaran','baclaran'): 0
    }
    if (source, destination) in fare_prices:
        return fare_prices[(source, destination)]

#SINGLE JOURNEY TICKET
def sjc_get_fare(source, destination):
    fare_prices = {
        ('roosevelt','roosevelt'): 0,
        ('roosevelt','balintawak'): 20,
        ('roosevelt','monumento'): 20,
        ('roosevelt','5th avenue'): 20,
        ('roosevelt','r.papa'): 25,
        ('roosevelt','abad santos'): 25,
        ('roosevelt','blumentrit'): 25,
        ('roosevelt','tayuman'): 25,
        ('roosevelt','bambang'): 25,
        ('roosevelt','doroteo jose'): 25,
        ('roosevelt','carriedo'): 30,
        ('roosevelt','central terminal'): 30,
        ('roosevelt','united nations'): 30,
        ('roosevelt','pedro gil'): 30,
        ('roosevelt','quirino'): 30,
        ('roosevelt','vito cruz'): 35,
        ('roosevelt','gil puyat'): 35,
        ('roosevelt','libertad'): 35,
        ('roosevelt','edsa'): 35,
        ('roosevelt','baclaran'): 35,
        ('balintawak','roosevelt'): 20,
        ('balintawak','balintawak'): 0,
        ('balintawak','monumento'): 20,
        ('balintawak','5th avenue'): 20,
        ('balintawak','r.papa'): 20,
        ('balintawak','abad santos'): 20,
        ('balintawak','blumentrit'): 20,
        ('balintawak','tayuman'): 25,
        ('balintawak','bambang'): 25,
        ('balintawak','doroteo jose'): 25,
        ('balintawak','carriedo'): 25,
        ('balintawak','central terminal'): 25,
        ('balintawak','united nations'): 30 ,
        ('balintawak','pedro gil'): 30 ,
        ('balintawak','quirino'): 30 ,
        ('balintawak','vito cruz'): 30 ,
        ('balintawak','gil puyat'): 30 ,
        ('balintawak','libertad'): 35,
        ('balintawak','edsa'): 35,
        ('balintawak','baclaran'): 35,
        ('monumento','roosevelt'): 20,
        ('monumento','balintawak'): 20,
        ('monumento','monumento'): 0,
        ('monumento','5th avenue'): 15,
        ('monumento','r.papa'): 20,
        ('monumento','abad santos'): 20,
        ('monumento','blumentrit'): 20,
        ('monumento','tayuman'): 20,
        ('monumento','bambang'): 20,
        ('monumento','doroteo jose'): 20,
        ('monumento','carriedo'): 25,
        ('monumento','central terminal'): 25,
        ('monumento','united nations'): 25,
        ('monumento','pedro gil'): 25,
        ('monumento','quirino'): 25,
        ('monumento','vito cruz'): 30 ,
        ('monumento','gil puyat'): 30 ,
        ('monumento','libertad'): 30 ,
        ('monumento','edsa'): 30 ,
        ('monumento','baclaran'): 30 ,
        ('5th avenue','roosevelt'): 20,
        ('5th avenue','balintawak'): 20,
        ('5th avenue','monumento'): 15,
        ('5th avenue','5th avenue'): 0,
        ('5th avenue','r.papa'): 15,
        ('5th avenue','abad santos'): 15,
        ('5th avenue','blumentrit'): 20,
        ('5th avenue','tayuman'): 20,
        ('5th avenue','bambang'): 20,
        ('5th avenue','doroteo jose'): 20,
        ('5th avenue','carriedo'): 20,
        ('5th avenue','central terminal'): 20,
        ('5th avenue','united nations'): 25,
        ('5th avenue','pedro gil'): 25,
        ('5th avenue','quirino'): 25,
        ('5th avenue','vito cruz'): 25,
        ('5th avenue','gil puyat'): 30 ,
        ('5th avenue','libertad'): 30 ,
        ('5th avenue','edsa'): 30 ,
        ('5th avenue','baclaran'): 30 ,
        ('r.papa','roosevelt'): 25,
        ('r.papa','balintawak'): 20,
        ('r.papa','monumento'): 20,
        ('r.papa','5th avenue'): 15,
        ('r.papa','r.papa'): 0,
        ('r.papa','abad santos'): 15,
        ('r.papa','blumentrit'): 15,
        ('r.papa','tayuman'): 20,
        ('r.papa','bambang'): 20,
        ('r.papa','doroteo jose'): 20,
        ('r.papa','carriedo'): 20,
        ('r.papa','central terminal'): 20,
        ('r.papa','united nations'): 25,
        ('r.papa','pedro gil'): 25,
        ('r.papa','quirino'): 25,
        ('r.papa','vito cruz'): 25,
        ('r.papa','gil puyat'): 25,
        ('r.papa','libertad'): 30,
        ('r.papa','edsa'): 30,
        ('r.papa','baclaran'): 30,
        ('abad santos','roosevelt'): 25,
        ('abad santos','balintawak'): 20,
        ('abad santos','monumento'): 20,
        ('abad santos','5th avenue'): 15,
        ('abad santos','r.papa'): 15,
        ('abad santos','abad santos'): 0,
        ('abad santos','blumentrit'): 15,
        ('abad santos','tayuman'): 15,
        ('abad santos','bambang'): 20,
        ('abad santos','doroteo jose'): 20,
        ('abad santos','carriedo'): 20,
        ('abad santos','central terminal'): 20,
        ('abad santos','united nations'): 20,
        ('abad santos','pedro gil'): 25,
        ('abad santos','quirino'): 25,
        ('abad santos','vito cruz'): 25,
        ('abad santos','gil puyat'): 25,
        ('abad santos','libertad'): 25,
        ('abad santos','edsa'): 30 ,
        ('abad santos','baclaran'): 30 ,
        ('blumentrit','roosevelt'): 25,
        ('blumentrit','balintawak'): 20,
        ('blumentrit','monumento'): 20,
        ('blumentrit','5th avenue'): 20,
        ('blumentrit','r.papa'): 15,
        ('blumentrit','abad santos'): 15,
        ('blumentrit','blumentrit'): 0,
        ('blumentrit','tayuman'): 15,
        ('blumentrit','bambang'): 15,
        ('blumentrit','doroteo jose'): 20,
        ('blumentrit','carriedo'): 20,
        ('blumentrit','central terminal'): 20,
        ('blumentrit','united nations'): 20,
        ('blumentrit','pedro gil'): 20,
        ('blumentrit','quirino'): 25,
        ('blumentrit','vito cruz'): 25,
        ('blumentrit','gil puyat'): 25,
        ('blumentrit','libertad'): 25,
        ('blumentrit','edsa'): 25,
        ('blumentrit','baclaran'): 30,
        ('tayuman','roosevelt'): 25,
        ('tayuman','balintawak'): 25,
        ('tayuman','monumento'): 20,
        ('tayuman','5th avenue'): 20,
        ('tayuman','r.papa'): 20,
        ('tayuman','abad santos'): 15,
        ('tayuman','blumentrit'): 15,
        ('tayuman','tayuman'): 0,
        ('tayuman','bambang'): 15,
        ('tayuman','doroteo jose'): 15,
        ('tayuman','carriedo'): 20,
        ('tayuman','central terminal'): 20,
        ('tayuman','united nations'): 20,
        ('tayuman','pedro gil'): 20,
        ('tayuman','quirino'): 20,
        ('tayuman','vito cruz'): 25,
        ('tayuman','gil puyat'): 25,
        ('tayuman','libertad'): 25,
        ('tayuman','edsa'): 25,
        ('tayuman','baclaran'): 25,
        ('bambang','roosevelt'): 25,
        ('bambang','balintawak'): 25,
        ('bambang','monumento'): 20,
        ('bambang','5th avenue'): 20,
        ('bambang','r.papa'): 20,
        ('bambang','abad santos'): 20,
        ('bambang','blumentrit'): 15,
        ('bambang','tayuman'): 15,
        ('bambang','bambang'): 0,
        ('bambang','doroteo jose'): 15,
        ('bambang','carriedo'): 15,
        ('bambang','central terminal'): 20,
        ('bambang','united nations'): 20,
        ('bambang','pedro gil'): 20,
        ('bambang','quirino'): 20,
        ('bambang','vito cruz'): 20,
        ('bambang','gil puyat'): 25,
        ('bambang','libertad'): 25,
        ('bambang','edsa'): 25,
        ('bambang','baclaran'): 25,
        ('doroteo jose','roosevelt'): 25,
        ('doroteo jose','balintawak'): 25,
        ('doroteo jose','monumento'): 20,
        ('doroteo jose','5th avenue'): 20,
        ('doroteo jose','r.papa'): 20,
        ('doroteo jose','abad santos'): 20,
        ('doroteo jose','blumentrit'): 20,
        ('doroteo jose','tayuman'): 15,
        ('doroteo jose','bambang'): 15,
        ('doroteo jose','doroteo jose'): 0,
        ('doroteo jose','carriedo'): 15,
        ('doroteo jose','central terminal'): 15,
        ('doroteo jose','united nations'): 20,
        ('doroteo jose','pedro gil'): 20,
        ('doroteo jose','quirino'): 20,
        ('doroteo jose','vito cruz'): 20,
        ('doroteo jose','gil puyat'): 25,
        ('doroteo jose','libertad'): 25,
        ('doroteo jose','edsa'): 25,
        ('doroteo jose','baclaran'): 25,
        ('carriedo','roosevelt'): 30,
        ('carriedo','balintawak'): 25,
        ('carriedo','monumento'): 25,
        ('carriedo','5th avenue'): 20,
        ('carriedo','r.papa'): 20,
        ('carriedo','abad santos'): 20,
        ('carriedo','blumentrit'): 20,
        ('carriedo','tayuman'): 20,
        ('carriedo','bambang'): 15,
        ('carriedo','doroteo jose'): 15,
        ('carriedo','carriedo'): 0,
        ('carriedo','central terminal'): 15,
        ('carriedo','united nations'): 20,
        ('carriedo','pedro gil'): 20,
        ('carriedo','quirino'): 20,
        ('carriedo','vito cruz'): 20,
        ('carriedo','gil puyat'): 20,
        ('carriedo','libertad'): 25,
        ('carriedo','edsa'): 25,
        ('carriedo','baclaran'): 25,
        ('central terminal','roosevelt'): 30,
        ('central terminal','balintawak'): 25,
        ('central terminal','monumento'): 25,
        ('central terminal','5th avenue'): 20,
        ('central terminal','r.papa'): 20,
        ('central terminal','abad santos'): 20,
        ('central terminal','blumentrit'): 20,
        ('central terminal','tayuman'): 20,
        ('central terminal','bambang'): 20,
        ('central terminal','doroteo jose'): 15,
        ('central terminal','carriedo'): 15,
        ('central terminal','central terminal'): 0,
        ('central terminal','united nations'): 15,
        ('central terminal','pedro gil'): 20,
        ('central terminal','quirino'): 20,
        ('central terminal','vito cruz'): 20,
        ('central terminal','gil puyat'): 20,
        ('central terminal','libertad'): 20,
        ('central terminal','edsa'): 25,
        ('central terminal','baclaran'): 25,
        ('united nations','roosevelt'): 30,
        ('united nations','balintawak'): 30,
        ('united nations','monumento'): 25,
        ('united nations','5th avenue'): 25,
        ('united nations','r.papa'): 25,
        ('united nations','abad santos'): 20,
        ('united nations','blumentrit'): 20,
        ('united nations','tayuman'): 20,
        ('united nations','bambang'): 20,
        ('united nations','doroteo jose'): 20,
        ('united nations','carriedo'): 20,
        ('united nations','central terminal'): 15,
        ('united nations','united nations'): 0,
        ('united nations','pedro gil'): 15,
        ('united nations','quirino'): 15,
        ('united nations','vito cruz'): 20,
        ('united nations','gil puyat'): 20,
        ('united nations','libertad'): 20,
        ('united nations','edsa'): 20,
        ('united nations','baclaran'): 20,
        ('pedro gil','roosevelt'): 30,
        ('pedro gil','balintawak'): 30,
        ('pedro gil','monumento'): 25,
        ('pedro gil','5th avenue'): 25,
        ('pedro gil','r.papa'): 25,
        ('pedro gil','abad santos'): 25,
        ('pedro gil','blumentrit'): 20,
        ('pedro gil','tayuman'): 20,
        ('pedro gil','bambang'): 20,
        ('pedro gil','doroteo jose'): 20,
        ('pedro gil','carriedo'): 20,
        ('pedro gil','central terminal'): 20,
        ('pedro gil','united nations'): 15,
        ('pedro gil','pedro gil'): 0,
        ('pedro gil','quirino'): 15,
        ('pedro gil','vito cruz'): 15,
        ('pedro gil','gil puyat'): 20,
        ('pedro gil','libertad'): 20,
        ('pedro gil','edsa'): 20,
        ('pedro gil','baclaran'): 20,
        ('quirino','roosevelt'): 30,
        ('quirino','balintawak'): 30,
        ('quirino','monumento'): 25,
        ('quirino','5th avenue'): 25,
        ('quirino','r.papa'): 25,
        ('quirino','abad santos'): 25,
        ('quirino','blumentrit'): 25,
        ('quirino','tayuman'): 20,
        ('quirino','bambang'): 20,
        ('quirino','doroteo jose'): 20,
        ('quirino','carriedo'): 20,
        ('quirino','central terminal'): 20,
        ('quirino','united nations'): 15,
        ('quirino','pedro gil'): 15,
        ('quirino','quirino'): 0,
        ('quirino','vito cruz'): 15,
        ('quirino','gil puyat'): 20,
        ('quirino','libertad'): 20,
        ('quirino','edsa'): 20,
        ('quirino','baclaran'): 20,
        ('vito cruz','roosevelt'): 35,
        ('vito cruz','balintawak'): 30,
        ('vito cruz','monumento'): 30,
        ('vito cruz','5th avenue'): 25,
        ('vito cruz','r.papa'): 25,
        ('vito cruz','abad santos'): 25,
        ('vito cruz','blumentrit'): 25,
        ('vito cruz','tayuman'): 25,
        ('vito cruz','bambang'): 20,
        ('vito cruz','doroteo jose'): 20,
        ('vito cruz','carriedo'): 20,
        ('vito cruz','central terminal'): 20,
        ('vito cruz','united nations'): 20,
        ('vito cruz','pedro gil'): 15,
        ('vito cruz','quirino'): 15,
        ('vito cruz','vito cruz'): 0,
        ('vito cruz','gil puyat'): 15,
        ('vito cruz','libertad'): 15,
        ('vito cruz','edsa'): 20,
        ('vito cruz','baclaran'): 20,
        ('gil puyat','roosevelt'): 35,
        ('gil puyat','balintawak'): 30,
        ('gil puyat','monumento'): 30,
        ('gil puyat','5th avenue'): 30,
        ('gil puyat','r.papa'): 25,
        ('gil puyat','abad santos'): 25,
        ('gil puyat','blumentrit'): 25,
        ('gil puyat','tayuman'): 25,
        ('gil puyat','bambang'): 25,
        ('gil puyat','doroteo jose'): 25,
        ('gil puyat','carriedo'): 20,
        ('gil puyat','central terminal'): 20,
        ('gil puyat','united nations'): 20,
        ('gil puyat','pedro gil'): 20,
        ('gil puyat','quirino'): 20,
        ('gil puyat','vito cruz'): 15,
        ('gil puyat','gil puyat'): 0,
        ('gil puyat','libertad'): 15,
        ('gil puyat','edsa'): 15,
        ('gil puyat','baclaran'): 20,
        ('libertad','roosevelt'): 35,
        ('libertad','balintawak'): 35,
        ('libertad','monumento'): 30,
        ('libertad','5th avenue'): 30,
        ('libertad','r.papa'): 30,
        ('libertad','abad santos'): 25,
        ('libertad','blumentrit'): 25,
        ('libertad','tayuman'): 25,
        ('libertad','bambang'): 25,
        ('libertad','doroteo jose'): 25,
        ('libertad','carriedo'): 25,
        ('libertad','central terminal'): 20,
        ('libertad','united nations'): 20,
        ('libertad','pedro gil'): 20,
        ('libertad','quirino'): 20,
        ('libertad','vito cruz'): 15,
        ('libertad','gil puyat'): 15,
        ('libertad','libertad'): 0,
        ('libertad','edsa'): 15,
        ('libertad','baclaran'): 15,
        ('edsa','roosevelt'): 35,
        ('edsa','balintawak'): 35,
        ('edsa','monumento'): 30,
        ('edsa','5th avenue'): 30,
        ('edsa','r.papa'): 30,
        ('edsa','abad santos'): 30,
        ('edsa','blumentrit'): 25,
        ('edsa','tayuman'): 25,
        ('edsa','bambang'): 25,
        ('edsa','doroteo jose'): 25,
        ('edsa','carriedo'): 25,
        ('edsa','central terminal'): 25,
        ('edsa','united nations'): 20,
        ('edsa','pedro gil'): 20,
        ('edsa','quirino'): 20,
        ('edsa','vito cruz'): 20,
        ('edsa','gil puyat'): 15,
        ('edsa','libertad'): 15,
        ('edsa','edsa'): 0,
        ('edsa','baclaran'): 15,
        ('baclaran','roosevelt'): 35,
        ('baclaran','balintawak'): 35,
        ('baclaran','monumento'): 30,
        ('baclaran','5th avenue'): 30,
        ('baclaran','r.papa'): 30,
        ('baclaran','abad santos'): 30,
        ('baclaran','blumentrit'): 30,
        ('baclaran','tayuman'): 25,
        ('baclaran','bambang'): 25,
        ('baclaran','doroteo jose'): 25,
        ('baclaran','carriedo'): 25,
        ('baclaran','central terminal'): 20,
        ('baclaran','united nations'): 20,
        ('baclaran','pedro gil'): 20,
        ('baclaran','quirino'): 20,
        ('baclaran','vito cruz'): 20,
        ('baclaran','gil puyat'): 15,
        ('baclaran','libertad'): 15,
        ('baclaran','edsa'): 15,
        ('baclaran','baclaran'): 0,
    }
    if (source, destination) in fare_prices:
        return fare_prices[(source, destination)]
    
source = input("From: ")
destination = input("To: ")
beep_fare = beep_get_fare(source, destination)
beep_fare = str(beep_fare)
sjc_fare = sjc_get_fare(source, destination)
discounted_fare = sjc_fare - int(sjc_fare)*.20 
sjc_fare = str(sjc_fare)


if beep_get_fare(source, destination) == None:
    print("Invalid Trip")
else:
    print(f"BEEP Card fare {source} to {destination} is ₱{beep_fare}")
    print(f"Single Journey Card fare {source} to {destination} is ₱{sjc_fare}")
    print(f"Single Journey Card fare {source} to {destination} is ₱{int(discounted_fare)}")


# DROP DOWN MENU FOR WHAT START AND END STATION

# DISPLAY BEEP RATE
# DISPLAY STUDENT AND SENIOR RATE
# DISPALY STANDARD

# MAKE ONE FOR LRT 2
# MAKE ONE FOR MRT 3
# MAKE ONE FOR PNR

# COMPARE PRICE TO RAILWAY RATIO
# SHOW SPEED BASED ON PNR AVERAGE
# SHOW SPEED BASED ON LRT AVERAGE
# SHOW SPEED BASED ON MRT AVERAGE
# PORT TO TKINTER

# SHOW POSTS ABOUT WHAT TO DO FROM OTHER PEOPLE IN THE SAME PLACES