import random


def mess_func(lori):
   flag = random.randint(0, 100)
   match random.randint(0, 1):
      case 0:
         lori[0] = random.randint(1, 19) if flag != 0 else random.randint(20, 26)
         lori[1] = random.randint(1, 30)
         lori[2] = random.randint(1, 6)
         lori[3] = random.randint(1, 31)
         lori[4] = random.randint(1, 5)
         lori[5] = random.randint(1, 12)
         lori[6] = random.randint(1, 59) if flag != 0 else random.randint(135, 138)
         lori[7] = random.randint(1, 5)
         lori[8] = random.randint(1, 51)
         lori[9] = random.randint(1, 55) if flag != 0 else random.randint(168, 169)
      case 1:
         lori[0] = random.randint(27, 46) if flag != 0 else random.randint(47, 53)
         lori[1] = random.randint(31, 62)
         lori[2] = random.randint(7, 12)
         lori[3] = random.randint(32, 66)
         lori[4] = random.randint(6, 39)
         lori[5] = random.randint(13, 24)
         lori[6] = random.randint(60, 134) if flag != 0 else random.randint(139, 142)
         lori[7] = random.randint(6, 79)  if flag != 0 else random.randint(80, 83)
         lori[8] = random.randint(52, 155)
         lori[9] = random.randint(56, 167)

   return lori
