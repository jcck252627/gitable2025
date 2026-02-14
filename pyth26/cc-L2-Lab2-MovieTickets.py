
# Variables (hardcoded):
movie_name = "Toy Story 4"
adult_tickets_sold = 1215
child_tickets_sold = 666
# Constants:
adult_ticket_price = 10
child_ticket_price= 6
Theater_share = 0.2
Studio_share= 0.8


adult_revenue = adult_tickets_sold * adult_ticket_price
child_revenue = child_tickets_sold * child_ticket_price
adult_revenue = adult_ticket_price * adult_tickets_sold
child_revenue=child_ticket_price* child_tickets_sold
gross_total = adult_revenue + child_revenue
theater_profit = gross_total * 0.20
studio_profit = gross_total * 0.80
gross_profit    = theater_profit + studio_profit

print(f'Movie Name:         {movie_name}')
print(f'Adult Tickets:      {adult_tickets_sold}')          
print(f'Child Tickets:      {child_tickets_sold}')
print(f'Adult Revenue:      ${adult_revenue:,.2f}')
print(f'Child Revenue:      ${child_revenue:,.2f}')
print(f'Total Revenue:      ${gross_total:,.2f}')
print(f'Theater Profit:     ${theater_profit:,.2f}')
print(f'Studio Profit:      ${studio_profit:,.2f}')
print(f'Gross Profit:       ${gross_profit:,.2f}')

