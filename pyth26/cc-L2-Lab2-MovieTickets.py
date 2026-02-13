
# Variables (hardcoded):
movie_name = "The Imation Game"
adult_tickets_sold = 215
child_tickets_sold = 76
# Constants:
adult_ticket_price = 10
child_ticket_price= 6
Theater_share = 0.2
Studio_share= 0.8


adult_revenue = adult_tickets_sold * adult_ticket_price
child_revenue = child_tickets_sold * child_ticket_price
gross_total = adult_revenue + child_revenue
theater_profit = gross_total * 0.20
studio_profit = gross_total * 0.80

print("Movie Name:  ")