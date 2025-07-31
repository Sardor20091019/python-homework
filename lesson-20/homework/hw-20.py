import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')

invoices_df = pd.read_sql_query("SELECT CustomerId, Total FROM Invoice", conn)
customers_df = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
total_spent = invoices_df.groupby("CustomerId")["Total"].sum().reset_index()
total_spent.columns = ["CustomerId", "TotalSpent"]
customer_spending = pd.merge(total_spent, customers_df, on="CustomerId")
customer_spending["Name"] = customer_spending["FirstName"] + " " + customer_spending["LastName"]
top5_customers = customer_spending.sort_values("TotalSpent", ascending=False).head(5)
top5_customers_display = top5_customers[["CustomerId", "Name", "TotalSpent"]]
print("Top 5 Customers by Total Purchase Amount:")
print(top5_customers_display)

invoice_items_df = pd.read_sql_query("SELECT InvoiceLineId, InvoiceId, TrackId FROM InvoiceLine", conn)
invoices_df = pd.read_sql_query("SELECT InvoiceId, CustomerId FROM Invoice", conn)
tracks_df = pd.read_sql_query("SELECT TrackId, AlbumId FROM Track", conn)
purchases = invoice_items_df.merge(invoices_df, on="InvoiceId")
purchases = purchases.merge(tracks_df, on="TrackId")
album_track_counts = tracks_df.groupby("AlbumId")["TrackId"].count().reset_index()
album_track_counts.columns = ["AlbumId", "TotalTracks"]
customer_album_tracks = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
customer_album_tracks.columns = ["CustomerId", "AlbumId", "TracksPurchased"]
comparison = customer_album_tracks.merge(album_track_counts, on="AlbumId")
comparison["FullAlbum"] = comparison["TracksPurchased"] == comparison["TotalTracks"]
customer_pref = comparison.groupby("CustomerId")["FullAlbum"].any().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Album" if x else "Individual Tracks")
preference_summary = customer_pref["Preference"].value_counts(normalize=True) * 100
print("\nCustomer Purchase Preference Summary:")
print(preference_summary)
