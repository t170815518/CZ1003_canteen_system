#Function by Vanessa
def waiting_time(number):  # number: string
    try:
        num_ppl = int(number)
        if num_ppl < 0:
            print("Please enter a non-negative integer.")
        else:
            wait_time = (int(num_ppl) + 1)*3
            print("Estimated waiting time is ", wait_time, " minutes.")
            return wait_time
    except:
        print("Please enter a valid no.")
        return False


#waiting_time()
