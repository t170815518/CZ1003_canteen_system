def waiting_time():
    while True:
        try:
            num_ppl = int(input("Enter no. of people in the queue: "))
            wait_time = (int(num_ppl) + 1)*3
            print("Estimated waiting time is ", wait_time, " minutes.")
            break
        except:
            print("Please enter a valid no.")
            continue
waiting_time()
