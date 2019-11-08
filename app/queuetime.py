
def waiting_time(number):
    while True:
        try:
            num_ppl = int(number)
            wait_time = num_ppl * 3
            return wait_time
            break
        except:
            return False
