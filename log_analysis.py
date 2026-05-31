
""" 
Description: Automatically updates a network allow-list by removing unauthorized or restricted IP addresses.
"""

def update_allowed_ip_list(import_file, remove_list):
    
    # open the file in read mode
    with open(import_file, "r") as file:
        
        # reading the imported file as a string and storing it in a variable
        allowed_ips = file.read()

        # display the imported ips as string
        print(allowed_ips)

    # using `.split()` to convert `allowed_ips` from a string to a list
    allowed_ips = allowed_ips.split()

    # display the imported ips in a list
    print(allowed_ips)

    for ip in allowed_ips:

        if ip in remove_list:
            allowed_ips.remove(ip)

    # display final list of allowed ips     
    print(allowed_ips)

    # converting allowed_ips list to string with one ip per line
    allowed_ips = " \n".join(allowed_ips)

    # display final list of ips to be written to a new file
    print(allowed_ips)

    # write the updated ips to a new file
    with open("updated_allow_list.txt", "w") as w_file:
        
        w_file.write(allowed_ips)

    print("[Success] Restricted IPs have been removed from the updated IPs file")
                


if __name__ == "__main__":

    # the file to be updated
    target_file = "allow_list.txt"

    # the ips that need to be removed from the network
    remove_ips_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

    # function call
    update_allowed_ip_list(target_file, remove_ips_list)


