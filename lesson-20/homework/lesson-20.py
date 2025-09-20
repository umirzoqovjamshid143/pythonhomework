Using chinook.db write pandas code.

1.Customer Purchases Analysis:
Find the total amount spent by each customer on purchases (considering invoices).
Identify the top 5 customers with the highest total purchase amounts.
Display the customer ID, name, and the total amount spent for the top 5 customers.

import sqlite3
import pandas as pd

#  Ulanish
conn = sqlite3.connect("chinook.db")
#  Ma'lumotlarni yuklash
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)

#  Har bir mijoz uchun umumiy sarf
customer_spending = invoices.groupby("CustomerId")["Total"].sum().reset_index()
customer_spending.columns = ["CustomerId", "TotalSpent"]


customer_info = customer_spending.merge(customers, on="CustomerId")
customer_info = customer_info[["CustomerId", "FirstName", "LastName", "Country", "TotalSpent"]]

top5_customers = customer_info.sort_values(by="TotalSpent", ascending=False).head(5)
print(top5_customers)



2.Album vs. Individual Track Purchases:
Determine the percentage of customers who prefer to buy individual tracks instead of full albums.
A customer is considered to prefer individual tracks if they have purchased only a subset of tracks from an album.
Provide a summary of the percentage of customers who fall into each category (individual tracks vs. full albums).

import sqlite3
import pandas as pd

# 1. Bazaga ulanamiz
conn = sqlite3.connect("chinook.db")

# 2. Kerakli jadvallarni yuklaymiz
customers = pd.read_sql_query("SELECT * FROM customers", conn)
invoices = pd.read_sql_query("SELECT * FROM invoices", conn)
invoice_items = pd.read_sql_query("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql_query("SELECT * FROM tracks", conn)
albums = pd.read_sql_query("SELECT * FROM albums", conn)

# 3. Albomdagi treklar sonini hisoblaymiz
album_track_counts = tracks.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.columns = ["AlbumId", "TotalTracks"]

# 4. Invoice items ga tracklar jadvalidan AlbumId ni qo‘shamiz
invoice_with_albums = invoice_items.merge(tracks[["TrackId", "AlbumId"]], on="TrackId")

# 5. Har bir mijoz-albom uchun nechta trek sotib olganini topamiz
# Buning uchun avval invoice_with_albums ga invoice va invoice orqali customer qo‘shamiz
invoice_with_albums = invoice_with_albums.merge(invoices[["InvoiceId", "CustomerId"]], on="InvoiceId")

# 6. Endi har bir mijoz va albom uchun nechta trek olganini hisoblaymiz
customer_album_tracks = invoice_with_albums.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
customer_album_tracks.columns = ["CustomerId", "AlbumId", "BoughtTracks"]

# 7. Umumiy trek soni bilan birlashtiramiz
customer_album_tracks = customer_album_tracks.merge(album_track_counts, on="AlbumId")

# 8. Har bir mijoz-albom xarid turini aniqlaymiz
customer_album_tracks["PurchaseType"] = customer_album_tracks.apply(
    lambda x: "Full Album" if x["BoughtTracks"] == x["TotalTracks"] else "Individual Tracks", axis=1
)

# 9. Endi har bir mijozning xarid turini aniqlaymiz
def classify_customer(group):
    types = set(group["PurchaseType"])
    if types == {"Full Album"}:
        return "Full Album"
    elif types == {"Individual Tracks"}:
        return "Individual Tracks"
    else:
        return "Mixed"

customer_types = customer_album_tracks.groupby("CustomerId").apply(classify_customer).reset_index(name="Type")

# 10. Statistik xulosa (foizda)
summary = customer_types["Type"].value_counts(normalize=True) * 100

# 11. Natijalarni chiqaramiz
print(summary)



