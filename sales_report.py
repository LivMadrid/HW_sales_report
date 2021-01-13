"""Generate sales report showing total melons each salesperson sold."""
# Here there is no function defined - putting in a function to call will help efficiency by only having to call the function 
#rather than repeating the code below each time we need sales_person info

#Two empty lists created for both sales people and melons sold 
salespeople = [] #salespeople should be changed to sales_people for better readability 
melons_sold = []

# Here we are opening f - meaning file? we could be more descriptive with this variable ex. sales_report_file
f = open('sales-report.txt')
#start a for loop: for each line in the file - scan each line in the file
for line in f:
    # go through each line and strip the whitespace 
    line = line.rstrip()
    #then split each line by the denoted "|" mark 
    # change entries to something more descrptive sales_report_entries
    entries = line.split('|')

    #denotes the index where the variables are  0 sales_person 1 total price of order 2 amount of melons they sold
    salesperson = entries[0] # this again needs to be changed to sales_person and entries could be more descriptive ex. sales_person = sales_report_entries[0]
    melons = int(entries[2]) # this could also be more descriptive melons_amount_sold = int(sales_report_entries[2])

#Creates a conditional loop : looping through each sales_person in sales_people
    if salesperson in salespeople:
        # so I think there would be an issue here because sales_people is just an empty list and we haven't appended anything to it
        # we need to do something line sales_people.append(sales_person)
        #then we can continue on with the next line - positionis also not a great variable name
        position = salespeople.index(salesperson)
        #its hard to understand what is happening: it could change to something like sales_position
        melons_sold[position] += melons # += melon_amount_sold
    else:#why would we do this? what is this conditional loop for? Think we need more of a dictionary or tuple to combine sales_people list and melons_sold list I.e 
        # num_of_melons_sold_sales_report = { "Name Name" : 126, "Name Name":34} etc. 
        # this adds sales_person to sales_people list
        salespeople.append(salesperson) 
        # this adds melons_amount to melons_sold list
        melons_sold.append(melons) 
#if we created a dictionary we could just reference the dictioanry rather than have to iterate through the person and index of lists.... 
#using dictionay.items
# instead of iterating through each sales_person[i] in range len(sales_people) and manually printing {sales_people [i]}
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
